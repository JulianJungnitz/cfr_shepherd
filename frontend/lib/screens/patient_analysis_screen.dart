import 'dart:math';

import 'package:expandable_text/expandable_text.dart';
import 'package:fl_chart/fl_chart.dart';
import 'package:flutter/material.dart';
import 'package:frontend/utils/model/disease_characterization/disease_characterization.dart';
import 'package:frontend/utils/model/causal_gene_discovery/causal_gene.dart';
import 'package:frontend/utils/model/patient/patient.dart';
import 'package:frontend/utils/model/patient_like_me/patient_like_me.dart';
import 'package:frontend/widgets/patient_information_box.dart';
import 'package:frontend/widgets/rounded_container.dart';
import 'package:frontend/widgets/similarity_info_box.dart';
import 'package:provider/provider.dart';
import 'package:frontend/utils/patient_data_provider.dart';

import 'package:flutter_charts/flutter_charts.dart';
import 'package:syncfusion_flutter_charts/charts.dart';

class PatientAnalysisScreen extends StatefulWidget {
  @override
  State<PatientAnalysisScreen> createState() => _PatientAnalysisScreenState();
}

class _PatientAnalysisScreenState extends State<PatientAnalysisScreen> {
  int patientId = 15013028;
  Patient? patient;

  @override
  void initState() {
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
              SimilarityInfoBox(
                data: context.watch<PatientDataProvider>().patientsLikeMe,
                title: 'Patients Like Me',
                firstLabel: "Patient ID",
                lastLabel: 'Patient Information',
                labelBuilder: (context, dataSet) {
                  dataSet as PatientLikeMe;
                  return Center(
                    child: Text(
                      dataSet.candidate_patients!.toString(),
                      style: Theme.of(context).textTheme.headlineSmall,
                    ),
                  );
                },
              ),
              SimilarityInfoBox(
                data: context.watch<PatientDataProvider>().causalGeneDiscovery,
                title: 'Causal Gene Discovery',
                firstLabel: "Ensamble ID",
                lastLabel: 'Shared with Patient',
                labelBuilder: (context, dataSet) {
                  dataSet as CausalGene;
                  return Center(
                    child: Text(
                      dataSet.genes!.toString(),
                      style: Theme.of(context).textTheme.titleMedium,
                    ),
                  );
                },
              ),
              SimilarityInfoBox(
                data: context
                    .watch<PatientDataProvider>()
                    .diseaseCharacterization,
                title: 'Disease Similarity',
                firstLabel: "Disease",
                lastLabel: 'Shared with Patient',
                labelBuilder: (context, dataSet) {
                  dataSet as DiseaseCharacterization;
                  return Column(
                    mainAxisAlignment: MainAxisAlignment.center,
                    children: [
                      Text(
                        dataSet.diseases!.toString(),
                        style: Theme.of(context).textTheme.titleSmall,
                        maxLines: 3,
                        overflow: TextOverflow.ellipsis,
                      ),
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
