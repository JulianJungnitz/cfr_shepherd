import 'dart:math';
import 'package:flutter/material.dart';
import 'package:frontend/widgets/patient_information_box.dart';
import 'package:frontend/widgets/rounded_container.dart';
import 'package:syncfusion_flutter_charts/charts.dart';

class SimilarityInfoBox extends StatefulWidget {
  final List<dynamic> data;
  final List<dynamic> comparisonData;
  final String title;
  final String firstLabel;
  final String lastLabel;
  final int itemsToShow;
  final Function(int) setShown;
  final Function(BuildContext, dynamic) labelBuilder;
  final Function(BuildContext, dynamic) comparisonWidgetBuilder;

  const SimilarityInfoBox(
      {super.key,
      required this.data,
      required this.title,
      required this.firstLabel,
      required this.lastLabel,
      required this.labelBuilder,
      required this.itemsToShow,
      required this.setShown,
      required this.comparisonWidgetBuilder,
      required this.comparisonData});

  @override
  State<SimilarityInfoBox> createState() => _SimilarityInfoBoxState();
}

class _SimilarityInfoBoxState extends State<SimilarityInfoBox> {
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
            InformationBoxHeader(
              title: widget.title,
              trailing: DropdownButtonHideUnderline(
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
                    widget.setShown(val);
                  },
                ),
              ),
            ),
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
                          Expanded(
                            child: Center(
                              child: Text(
                                'Similarity Score',
                                style: Theme.of(context).textTheme.titleMedium,
                              ),
                            ),
                          ),
                          Expanded(
                            child: Center(
                              child: Text(
                                widget.lastLabel,
                                style: Theme.of(context).textTheme.titleMedium,
                              ),
                            ),
                          ),
                        ],
                      ),
                      Row(
                        children: [
                          Container(
                            height: barHeight * widget.itemsToShow,
                            child: Padding(
                              padding:
                                  const EdgeInsets.only(top: 10.0, bottom: 34),
                              child: Column(
                                children: List.generate(
                                  widget.itemsToShow,
                                  (index) => Container(
                                    height:
                                        barHeight - (44 / widget.itemsToShow),
                                    width: 150,
                                    child: (widget.labelBuilder(
                                        context, widget.data[index])),
                                  ),
                                ),
                              ),
                            ),
                          ),
                          Expanded(
                            child: SimilarityChart(
                                data: widget.data,
                                itemsToShow: widget.itemsToShow),
                          ),
                          Expanded(
                            child: Container(
                              height: barHeight * widget.itemsToShow,
                              child: Padding(
                                padding: const EdgeInsets.only(
                                    top: 10.0, bottom: 34),
                                child: Column(
                                  crossAxisAlignment: CrossAxisAlignment.start,
                                  children: List.generate(
                                    widget.itemsToShow,
                                    (index) => Container(
                                        height: barHeight -
                                            (44 / widget.itemsToShow),
                                        child: widget.comparisonData.length <=
                                                index
                                            ? Container(
                                                child: Center(
                                                  child:
                                                      CircularProgressIndicator(),
                                                ),
                                              )
                                            : (widget.comparisonWidgetBuilder(
                                                context,
                                                widget.comparisonData[index]))),
                                  ),
                                ),
                              ),
                            ),
                          ),
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
