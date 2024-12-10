import 'package:expandable_text/expandable_text.dart';
import 'package:flutter/material.dart';
import 'package:frontend/utils/model/disease_characterization/disease_characterization.dart';
import 'package:frontend/utils/model/causal_gene_discovery/causal_gene.dart';
import 'package:frontend/utils/model/patient/patient.dart';
import 'package:frontend/utils/model/patient_like_me/patient_like_me.dart';
import 'package:frontend/widgets/patient_information_box.dart';
import 'package:frontend/widgets/similarity_info_box.dart';
import 'package:provider/provider.dart';
import 'package:frontend/utils/patient_data_provider.dart';

class PatientAnalysisScreen extends StatefulWidget {
  final int patientId;

  const PatientAnalysisScreen({super.key, required this.patientId});
  @override
  State<PatientAnalysisScreen> createState() => _PatientAnalysisScreenState();
}

class _PatientAnalysisScreenState extends State<PatientAnalysisScreen> {
  late int patientId;
  Patient? patient;

  @override
  void initState() {
    patientId = widget.patientId;
    super.initState();
    context.read<PatientDataProvider>().getPatientsLikeMe(patientId);
    context.read<PatientDataProvider>().getCausalGeneDiscovery(patientId);
    context.read<PatientDataProvider>().getDiseaseCharacterization(patientId);
    loadPatient();
  }

  void loadPatient() async {
    patient = await context
        .read<PatientDataProvider>()
        .getPatientInformation(patientId);
    setState(() {});
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Patient Analysis'),
      ),
      body: SingleChildScrollView(
        child: Padding(
          padding: const EdgeInsets.all(32.0),
          child: Column(
            children: [
              PatientInformationBox(
                patient: patient,
              ),
              SizedBox(
                height: 32,
              ),
              Divider(),
              SizedBox(
                height: 32,
              ),
              SimilarityInfoBox(
                itemsToShow:
                    context.watch<PatientDataProvider>().shownPatientsLikeMe,
                setShown: (val) {
                  context
                      .read<PatientDataProvider>()
                      .setShownPatientsLikeMe(val);
                },
                data: context.watch<PatientDataProvider>().patientsLikeMe,
                title: 'Patients Like Me',
                firstLabel: "Patient ID",
                lastLabel: 'Shared with Patient',
                labelBuilder: (context, dataSet) {
                  dataSet as PatientLikeMe;
                  return Center(
                    child: Text(
                      dataSet.candidate_patients!.toString(),
                      style: Theme.of(context).textTheme.headlineSmall,
                    ),
                  );
                },
                comparisonData: context
                    .watch<PatientDataProvider>()
                    .patientsLikeMeWholeInfo,
                comparisonWidgetBuilder: (context, comparisonPatient) {
                  comparisonPatient as Patient;
                  List<String?> genes =
                      comparisonPatient.genes!.map((e) => e.id).toList();
                  List<String?> sharedGenes = (patient?.genes ?? [])
                      .map((e) => e.id)
                      .where((element) => genes.contains(element))
                      .toList();
                  List<String> sharedPhenotypes = patient!.phenotypes!
                      .map((e) => e.name!)
                      .where((element) => comparisonPatient.phenotypes!
                          .map((e) => e.name!)
                          .contains(element))
                      .toList();
                  List<String> sharedDiseases = patient!.diseases!
                      .map((e) => e.name!)
                      .where((element) => comparisonPatient.diseases!
                          .map((e) => e.name!)
                          .contains(element))
                      .toList();
                  return Column(
                    children: [
                      ExpandableText(
                        'Genes:  ${sharedGenes.isEmpty ? "No Genes shared" : sharedGenes.join(", ")}' +
                            '\nPhenotypes: ${sharedPhenotypes.isEmpty ? "No Phenotypes shared" : sharedPhenotypes.join(", ")}' +
                            '\nDiseases: ${sharedDiseases.isEmpty ? "No Diseases shared" : sharedDiseases.join(", ")}',
                        maxLines: 3,
                        style: Theme.of(context).textTheme.bodyMedium,
                        expandText: 'Show More',
                        collapseText: 'Show Less',
                      ),
                    ],
                  );
                },
              ),
              SimilarityInfoBox(
                itemsToShow: context
                    .watch<PatientDataProvider>()
                    .shownCausalGeneDiscovery,
                setShown: (val) {
                  context
                      .read<PatientDataProvider>()
                      .setShownCausalGeneDiscovery(val);
                },
                data: context.watch<PatientDataProvider>().causalGeneDiscovery,
                title: 'Causal Gene Discovery',
                firstLabel: "Ensamble ID",
                lastLabel: 'Shared with Patients (from patients like me)',
                labelBuilder: (context, dataSet) {
                  dataSet as CausalGene;
                  return Center(
                    child: Text(
                      dataSet.genes!.toString(),
                      style: Theme.of(context).textTheme.titleMedium,
                    ),
                  );
                },
                comparisonData:
                    context.watch<PatientDataProvider>().causalGeneDiscovery,
                comparisonWidgetBuilder: (context, gene) {
                  gene as CausalGene;
                  List<Patient> patientsWithGene = context
                      .watch<PatientDataProvider>()
                      .patientsLikeMeWholeInfo
                      .where((element) => element.genes!
                          .map((e) => e.synonyms![1])
                          .contains(gene.genes))
                      .toList();

                  return Column(
                    mainAxisAlignment: MainAxisAlignment.center,
                    children: [
                      Text(
                        '${patientsWithGene.isEmpty ? "No Patients" : patientsWithGene.map((e) => e.sampleId).join(", ")}',
                        style: Theme.of(context).textTheme.bodyMedium,
                      ),
                    ],
                  );
                },
              ),
              SimilarityInfoBox(
                itemsToShow: context
                    .watch<PatientDataProvider>()
                    .shownDiseaseCharacterization,
                setShown: (val) {
                  context
                      .read<PatientDataProvider>()
                      .setShownDiseaseCharacterization(val);
                },
                data: context
                    .watch<PatientDataProvider>()
                    .diseaseCharacterization,
                title: 'Disease Similarity',
                firstLabel: "Disease",
                lastLabel: 'Shared with Patients (from patients like me)',
                labelBuilder: (context, disease) {
                  disease as DiseaseCharacterization;

                  return Column(
                    mainAxisAlignment: MainAxisAlignment.center,
                    children: [
                      Text(
                        disease.diseases!.toString(),
                        style: Theme.of(context).textTheme.titleSmall,
                        maxLines: 3,
                        overflow: TextOverflow.ellipsis,
                      ),
                    ],
                  );
                },
                comparisonData: context
                    .watch<PatientDataProvider>()
                    .diseaseCharacterization,
                comparisonWidgetBuilder: (context, comparisonDisease) {
                  // print("Disease (dataset): "dataSet.diseases;
                  if (patient == null) return Container();
                  List<Patient> patientsLikeMeAdditionalInfo = context
                      .read<PatientDataProvider>()
                      .patientsLikeMeWholeInfo;
                  List<Patient> patientsWithDisease =
                      patientsLikeMeAdditionalInfo.where((element) {
                    return element.diseases!
                        .map((e) => e.name)
                        .contains(comparisonDisease.diseases);
                  }).toList();
                  return Column(
                    mainAxisAlignment: MainAxisAlignment.center,
                    children: [
                      Text(
                          '${patientsWithDisease.isEmpty ? "No Patients" : patientsWithDisease.map((e) => e.sampleId).join(", ")}',
                          style: Theme.of(context).textTheme.bodyMedium),
                    ],
                  );
                },
              ),
            ],
          ),
        ),
      ),
    );
  }
}
