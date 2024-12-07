import 'dart:math';

import 'package:fl_chart/fl_chart.dart';
import 'package:flutter/material.dart';
import 'package:frontend/utils/model/disease_characterization/disease_characterization.dart';
import 'package:frontend/utils/model/causal_gene_discovery/causal_gene.dart';
import 'package:frontend/utils/model/patient_like_me/patient_like_me.dart';
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

  @override
  void initState() {
    super.initState();
    context.read<PatientDataProvider>().getPatientsLikeMe(patientId);
    context.read<PatientDataProvider>().getCausalGeneDiscovery(patientId);
    context.read<PatientDataProvider>().getDiseaseCharacterization(patientId);
    context.read<PatientDataProvider>().getPatientInformation(patientId);
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

class RoundedContainer extends StatelessWidget {
  final Color color;
  final bool shadow;
  final Widget child;
  const RoundedContainer(
      {super.key,
      this.color = Colors.white,
      required this.child,
      this.shadow = false});

  @override
  Widget build(BuildContext context) {
    return Container(
      padding: const EdgeInsets.all(16),
      decoration: BoxDecoration(
        color: color,
        borderRadius: BorderRadius.circular(16),
        boxShadow: shadow
            ? [
                BoxShadow(
                  color: Colors.grey.withOpacity(0.5),
                  spreadRadius: 5,
                  blurRadius: 7,
                  offset: const Offset(0, 3), // changes position of shadow
                ),
              ]
            : [],
      ),
      child: child,
    );
  }
}

class SimilarityInfoBox extends StatefulWidget {
  final List<dynamic> data;
  final String title;
  final String firstLabel;
  final String lastLabel;
  final Function(BuildContext, dynamic) labelBuilder;

  const SimilarityInfoBox(
      {super.key,
      required this.data,
      required this.title,
      required this.firstLabel,
      required this.lastLabel,
      required this.labelBuilder});

  @override
  State<SimilarityInfoBox> createState() => _SimilarityInfoBoxState();
}

class _SimilarityInfoBoxState extends State<SimilarityInfoBox> {
  int itemsToShow = 5;
  int _dropDownValue = 5;

  @override
  Widget build(BuildContext context) {
    return Padding(
      padding: const EdgeInsets.only(bottom: 64.0),
      child: RoundedContainer(
        shadow: true,
        child: Column(
          mainAxisSize: MainAxisSize.max,
          mainAxisAlignment: MainAxisAlignment.spaceBetween,
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            Container(
              height: 50,
              child: Row(
                crossAxisAlignment: CrossAxisAlignment.center,
                mainAxisAlignment: MainAxisAlignment.spaceBetween,
                children: [
                  Text(
                    widget.title,
                    style: Theme.of(context).textTheme.headlineMedium,
                  ),
                  DropdownButtonHideUnderline(
                    child: DropdownButton<int>(
                      borderRadius: BorderRadius.circular(8),
                      value: _dropDownValue,
                      items: [3, 5, 10, 15]
                          .map((v) => DropdownMenuItem(
                              value: v,
                              child: Text(
                                '$v',
                                style: Theme.of(context).textTheme.headlineSmall,
                              )))
                          .toList(),
                      onChanged: (val) {
                        setState(() {
                          _dropDownValue = val!;
                        });
                        val = min(val!, widget.data.length);
                        print(val);
                        setState(() {
                          itemsToShow = val!;
                        });
                      },
                    ),
                  )
                ],
              ),
            ),
            Divider(),
            SizedBox(height: 16),
            widget.data.isEmpty
                ? Center(
                    child: Padding(
                      padding: const EdgeInsets.all(128.0),
                      child: const CircularProgressIndicator(),
                    ),
                  )
                : Column(
                    children: [
                      Row(
                        children: [
                          Text(
                            widget.firstLabel,
                            style: Theme.of(context).textTheme.titleMedium,
                          ),
                          Spacer(),
                          Text(
                            'Similarity Score',
                            style: Theme.of(context).textTheme.titleMedium,
                          ),
                          Spacer(),
                          Text(
                            widget.lastLabel,
                            style: Theme.of(context).textTheme.titleMedium,
                          ),
                          Spacer(),
                        ],
                      ),
                      Row(
                        children: [
                          Container(
                            height: barHeight * itemsToShow,
                            child: Padding(
                              padding:
                                  const EdgeInsets.only(top: 10.0, bottom: 34),
                              child: Column(
                                children: List.generate(
                                  itemsToShow,
                                  (index) => Container(
                                    height: barHeight - (44 / itemsToShow),
                                    width: 150,
                                    child: (widget.labelBuilder(
                                        context, widget.data[index])),
                                  ),
                                ),
                              ),
                            ),
                          ),
                          SimilarityChart(
                              data: widget.data, itemsToShow: itemsToShow),
                        ],
                      ),
                    ],
                  ),
          ],
        ),
      ),
    );
  }
}

final double barHeight = 80;

class SimilarityChart extends StatelessWidget {
  final int itemsToShow;
  final List<dynamic> data;
  const SimilarityChart(
      {super.key, required this.data, required this.itemsToShow});

  @override
  Widget build(BuildContext context) {
    List data = List.from(this.data);
    data = data.sublist(data.length - itemsToShow, data.length);
    return AnimatedContainer(
      width: MediaQuery.of(context).size.width / 2,
      duration: const Duration(milliseconds: 500),
      height: data.length * barHeight,
      child: SfCartesianChart(
        legend: Legend(isVisible: true),
        tooltipBehavior: TooltipBehavior(enable: false),
        primaryXAxis: CategoryAxis(
          isVisible: false,
        ),
        primaryYAxis: NumericAxis(
          labelFormat: '{value}',
        ),
        series: <CartesianSeries>[
          StackedBarSeries<dynamic, String>(
            spacing: 0,
            isVisibleInLegend: false,
            dataSource: data,
            xValueMapper: (dynamic data, _) => _.toString(),
            yValueMapper: (dynamic data, _) => data.similarities!,
            color: Colors.blueAccent,
            dataLabelSettings: DataLabelSettings(
              alignment: ChartAlignment.center,
              isVisible: false,
            ),
            markerSettings: MarkerSettings(isVisible: false),
          ),
        ],
      ),
    );
  }
}
