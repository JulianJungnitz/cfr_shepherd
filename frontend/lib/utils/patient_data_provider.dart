import 'package:frontend/utils/api.dart';
import 'package:frontend/utils/model/disease_characterization/disease_characterization.dart';
import 'package:frontend/utils/model/causal_gene_discovery/causal_gene.dart';
import 'package:frontend/utils/model/patient/patient.dart';
import 'package:frontend/utils/model/patient_like_me/patient_like_me.dart';
import 'package:provider/provider.dart';
import 'package:flutter/material.dart';

class PatientDataProvider extends ChangeNotifier {
  List<PatientLikeMe> patientsLikeMe = [];
  List<DiseaseCharacterization> diseaseCharacterization = [];
  List<CausalGene> causalGeneDiscovery = [];

  void getPatientsLikeMe(int patientId) async {
    var response = await API.get('${APIPaths.patientsLikeMe}/$patientId');
    if (response.success) {
      patientsLikeMe = [];
      for (var item in response.data["similar_patients"]) {
        patientsLikeMe.add(PatientLikeMe.fromJson(item));
      }
      patientsLikeMe.sort((a, b) => a.similarities!.compareTo(b.similarities!));
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

  Future<APIResult> _queryNeo4J(String query) async {
    var response = await API.post('${APIPaths.query}', body: {"query": query});
    return response;
  }

  void getPatientInformation(int patientId) async {
    String query = """
    Match (bs:Biological_sample) 
    Optional Match (bs)-[:HAS_DAMAGE]->(g:Gene)
    Optional Match (bs)-[:HAS_PHENOTYPE]->(p:Phenotype)
    Optional Match (bs)-[:HAS_DISEASE]->(d:Disease)
    Optional Match (bs)-[:BELONGS_TO_SUBJECT]-(s:Subject)
    WHERE id(bs) = $patientId
    return bs as biological_sample ,collect(g) as genes,collect(p) as phenotypes ,id(s) as subject_id limit 1
    """;
    var response = await _queryNeo4J(query);
    if (response.success) {
      // print(response.data);
      Patient p = Patient.fromJson(response.data[0]);
      print(p.subjectId);
    }
  }
}
