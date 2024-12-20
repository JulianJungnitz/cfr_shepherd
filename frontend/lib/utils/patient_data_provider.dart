import 'package:frontend/utils/api.dart';
import 'package:frontend/utils/model/attention/attention.dart';
import 'package:frontend/utils/model/disease/disease.dart';
import 'package:frontend/utils/model/disease_characterization/disease_characterization.dart';
import 'package:frontend/utils/model/causal_gene_discovery/causal_gene.dart';
import 'package:frontend/utils/model/patient/patient.dart';
import 'package:frontend/utils/model/patient_like_me/patient_like_me.dart';
import 'package:flutter/material.dart';

class PatientDataProvider extends ChangeNotifier {
  List<PatientLikeMe> patientsLikeMe = [];
  List<DiseaseCharacterization> diseaseCharacterization = [];
  List<CausalGene> causalGeneDiscovery = [];

  List<Patient> patientsLikeMeWholeInfo = [];

  List<Attention> patientsLikeMeAttentions = [];
  List<Attention> diseaseCharacterizationAttentions = [];
  List<Attention> causalGeneDiscoveryAttentions = [];

  int defaultShowNumber = 5;

  int shownPatientsLikeMe = 5;
  int shownDiseaseCharacterization = 5;
  int shownCausalGeneDiscovery = 5;

  void setShownPatientsLikeMe(int number) {
    shownPatientsLikeMe = number;
    loadPatientsLikeMeWholeInfo();
    notifyListeners();
  }

  void setShownDiseaseCharacterization(int number) {
    shownDiseaseCharacterization = number;
    notifyListeners();
  }

  void setShownCausalGeneDiscovery(int number) {
    shownCausalGeneDiscovery = number;
    notifyListeners();
  }

  void loadPatientsLikeMeWholeInfo() async {
    patientsLikeMeWholeInfo = [];
    int index = 0;
    for (var patient in patientsLikeMe) {
      print("Loading patient information: ${patient.candidate_patients}");
      var p = await getPatientInformation(patient.candidate_patients!);
      if (p != null) {
        patientsLikeMeWholeInfo.add(p);
      }
      index += 1;
      if (index >= shownPatientsLikeMe) {
        break;
      }
    }
    print(
        "Patients like me whole info loaded: ${patientsLikeMeWholeInfo.length}");
    notifyListeners();
  }

  void getPatientsLikeMe(int patientId) async {
    var response = await API.get('${APIPaths.patientsLikeMe}/$patientId');
    if (response.success) {
      patientsLikeMe = [];
      for (var item in response.data["similar_patients"]) {
        patientsLikeMe.add(PatientLikeMe.fromJson(item));
      }
      patientsLikeMe.sort((a, b) => a.similarities!.compareTo(b.similarities!));
      loadPatientsLikeMeWholeInfo();
      List<int> patientIDs = [];
      for (var item in patientsLikeMe) {
        if(item.candidate_patients == null) continue;
        patientIDs.add(item.candidate_patients!);
      }
      patientIDs.add(patientId);
      getPatientsLikeMeAttention(patientIDs);
      getDiseaseCharacterizationAttention(patientIDs);
      getCausalGeneDiscoveryAttention(patientIDs);

      notifyListeners();
    }
  }

  void getDiseaseCharacterization(int patientId) async {
    var response =
        await API.get('${APIPaths.diseaseCharacterization}/$patientId');
    if (response.success) {
      diseaseCharacterization = [];
      for (var item in response.data["disease_characterization"]) {
        diseaseCharacterization.add(DiseaseCharacterization.fromJson(item));
      }
      diseaseCharacterization
          .sort((a, b) => a.similarities!.compareTo(b.similarities!));
      notifyListeners();
    }
  }

  void getCausalGeneDiscovery(int patientId) async {
    var response = await API.get('${APIPaths.causalGeneDiscovery}/$patientId');
    if (response.success) {
      causalGeneDiscovery = [];
      for (var item in response.data["causal_gene"]) {
        causalGeneDiscovery.add(CausalGene.fromJson(item));
      }
      causalGeneDiscovery
          .sort((a, b) => a.similarities!.compareTo(b.similarities!));
      notifyListeners();
    }
  }

  List<int> getTopKPatientsLikeMe(int k) {
    List<int> patientIDs = [];
    int index = 0;
    for (var item in patientsLikeMe) {
      if(item.candidate_patients == null) continue;
      patientIDs.add(item.candidate_patients!);
      index += 1;
      if (index >= k) {
        break;
      }
    }
    return patientIDs;
  }

  void getPatientsLikeMeAttention(List<int> patientIDs) async {
    var response = await API
        .post(APIPaths.patientsLikeMeAttn, body: {"patient_ids": patientIDs});
    if (response.success) {
      patientsLikeMeAttentions = [];
      for (var item in response.data) {
        patientsLikeMeAttentions.add(Attention.fromJson(item));
      }
      print("Patients like me attentions loaded: ${patientsLikeMeAttentions.length}");
      notifyListeners();
    }
  }
  
  void getDiseaseCharacterizationAttention(List<int> patientIds) async {
    var response = await API.post(
        APIPaths.diseaseCharacterizationAttn, body: {"patient_ids": patientIds});
    if (response.success) {
      diseaseCharacterizationAttentions = [];
      for (var item in response.data) {
        diseaseCharacterizationAttentions.add(Attention.fromJson(item));
      }
      notifyListeners();
    }
  }
  
  void getCausalGeneDiscoveryAttention(List<int> patientIds) async {
    var response = await API.post(
        APIPaths.causalGeneDiscoveryAttn, body: {"patient_ids": patientIds});
    if (response.success) {
      causalGeneDiscoveryAttentions = [];
      for (var item in response.data) {
        causalGeneDiscoveryAttentions.add(Attention.fromJson(item));
      }
      notifyListeners();
    }
  }

  Future<APIResult> queryNeo4J(String query) async {
    var response = await API.post('${APIPaths.query}', body: {"query": query});
    return response;
  }

  Future<Patient?> getPatientInformation(int patientId) async {
    String query = """
    Match (bs:Biological_sample) 
    WHERE id(bs) = $patientId
    Optional Match (bs)-[:HAS_DAMAGE]->(g:Gene)
    Optional Match (bs)-[:HAS_PHENOTYPE]->(p:Phenotype)
    Optional Match (bs)-[:HAS_DISEASE]->(d:Disease)
    Optional Match (bs)-[:BELONGS_TO_SUBJECT]-(s:Subject)
    return bs as biological_sample ,collect(distinct g) as genes, collect(distinct d) as diseases,collect(distinct p) as phenotypes ,id(s) as sample_id limit 1
    """;
    var response = await queryNeo4J(query);
    if (!response.success) {
      return null;
    }

    Patient p = Patient.fromJson(response.data[0]);
    return p;
  }

  Future<Disease?> getDiseaseInformation(String diseaseName) async {
    String query = """
    Match (d:Disease) 
    Optional Match (d)-[:HAS_PHENOTYPE]->(p:Phenotype)
    WHERE d.name = "$diseaseName"
    return d as disease, collect(p) as phenotypes limit 1
    """;
    var response = await queryNeo4J(query);
    if (!response.success) {
      return null;
    }
    Disease d = Disease.fromJson(response.data[0]);
    return d;
  }
}
