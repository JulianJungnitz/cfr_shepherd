import 'dart:math';

import 'package:flutter/material.dart';
import 'package:frontend/utils/api.dart';
import 'package:frontend/utils/model/attention/attention.dart';
import 'package:frontend/utils/patient_data_provider.dart';
import 'package:frontend/widgets/rounded_container.dart';
import 'package:provider/provider.dart';

class PhenotypeAttentionBox extends StatefulWidget {
  final int patientId;
  const PhenotypeAttentionBox({
    super.key,
    required this.patientId,
  });

  @override
  State<PhenotypeAttentionBox> createState() => _PhenotypeAttentionBoxState();
}

class _PhenotypeAttentionBoxState extends State<PhenotypeAttentionBox> {
  List<String> runs = [
    "Patients Like Me",
    "Causal Gene Discovery",
    "Disease Characterization"
  ];
  late String selectedRun;
  int? _dropDownValue = 5;

  @override
  void initState() {
    super.initState();
    selectedRun = runs[0];
  }

  @override
  Widget build(BuildContext context) {
    return RoundedContainer(
      shadow: true,
      child: SizedBox(
        width: double.infinity,
        child: Column(
          children: [
            Row(
              crossAxisAlignment: CrossAxisAlignment.end,
              children: [
                Text(
                  'Phenotype Attention',
                  style: Theme.of(context).textTheme.headlineMedium,
                ),
                // TextButton(
                //     onPressed: () {
                //       // API.post("/attn/patients_like_me/", body: {
                //       //   "patient_ids": [15013032, 15013033, 15013034]
                //       // },debug: true);
                //       context.read<PatientDataProvider>().getPatientsLikeMeAttention([
                //         15013032,
                //         15013033,
                //         15013034
                //       ]);
                //     },
                //     child: Text("test")),
                Spacer(),
                ...runs
                    .map(
                      (e) => CustomToggleButton(
                        label: e,
                        onSelect: (label) {
                          setState(() {
                            selectedRun = label;
                          });
                        },
                        currentSelection: selectedRun,
                      ),
                    )
                    .toList(),
              ],
            ),
            SizedBox(
              height: 8,
            ),
            Divider(),
            Row(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Expanded(
                  child: PhenotypeWeightsGraph(
                    patientIds: [widget.patientId] +
                        context
                            .watch<PatientDataProvider>()
                            .getTopKPatientsLikeMe(_dropDownValue! - 1),
                    attentions: selectedRun == "Causal Gene Discovery"
                        ? context
                            .watch<PatientDataProvider>()
                            .causalGeneDiscoveryAttentions
                        : selectedRun == "Disease Characterization"
                            ? context
                                .watch<PatientDataProvider>()
                                .diseaseCharacterizationAttentions
                            : context
                                .watch<PatientDataProvider>()
                                .patientsLikeMeAttentions,
                  ),
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
                      print("Getting patients like me attention");
                    },
                  ),
                ),
              ],
            ),
          ],
        ),
      ),
    );
  }
}

class PhenotypeWeightsGraph extends StatefulWidget {
  final List<int> patientIds;
  final List<Attention> attentions;
  const PhenotypeWeightsGraph({
    super.key,
    required this.patientIds,
    required this.attentions,
  });

  @override
  State<PhenotypeWeightsGraph> createState() => _PhenotypeWeightsGraphState();
}

class _PhenotypeWeightsGraphState extends State<PhenotypeWeightsGraph> {
  late int selectedPatient;

  @override
  void initState() {
    super.initState();
    selectedPatient = widget.patientIds[0];
  }

  @override
  Widget build(BuildContext context) {
    if (widget.patientIds.length == 0 || widget.attentions.length == 0) {
      return Padding(
        padding: const EdgeInsets.all(128.0),
        child: Center(
          child: SizedBox(
            height: 100,
            width: 100,
            child: CircularProgressIndicator(),
          ),
        ),
      );
    }
    if (widget.patientIds.contains(selectedPatient) == false) {
      selectedPatient = widget.patientIds[0];
    }
    List<Attention> patientsAttention = widget.attentions
        .where((element) => element.patientId == selectedPatient)
        .toList();
    double patientMaxAttention = patientsAttention
        .map((e) => e.attention ?? 0)
        .reduce((value, element) => max(value, element));
    List<String> phenotypes =
        patientsAttention.map((e) => e.phenotypes ?? "--").toSet().toList();
    List<double> correspondingScores =
        List.generate(phenotypes.length, (index) {
      return patientsAttention
          .where((element) => element.phenotypes == phenotypes[index])
          .map((e) => e.attention!)
          .reduce((value, element) => value + element);
    });
    return Container(
      child: ConnectedLists(
        patientMaxAttention: patientMaxAttention,
        attentions: patientsAttention,
        scores: correspondingScores,
        selectedRightWord: selectedPatient,
        onSelectionChanged: (s) {
          setState(() {
            selectedPatient = s;
          });
        },
        leftWords: phenotypes,
        rightWords: widget.patientIds.map((e) => e.toString()).toList(),
      ),
    );
  }
}

class CustomToggleButton extends StatelessWidget {
  final bool noPadding;
  final String label;
  final Function(String) onSelect;
  final String? currentSelection;
  final TextStyle? textStyle;

  const CustomToggleButton({
    super.key,
    required this.label,
    required this.onSelect,
    this.currentSelection,
    this.textStyle,
    this.noPadding = false,
  });

  @override
  Widget build(BuildContext context) {
    bool isSelected = currentSelection == label;
    return Padding(
      padding: noPadding ? EdgeInsets.zero : EdgeInsets.only(left: 16.0),
      child: InkWell(
        onTap: () {
          onSelect(label);
        },
        child: Container(
          // height: 60,
          padding: const EdgeInsets.symmetric(horizontal: 16, vertical: 8),
          decoration: BoxDecoration(
            boxShadow: isSelected
                ? []
                : [
                    BoxShadow(
                      color: Colors.grey.withOpacity(0.5),
                      spreadRadius: 3,
                      blurRadius: 3,
                      offset: const Offset(0, 2), // changes position of shadow
                    ),
                  ],
            color: isSelected ? Theme.of(context).primaryColor : Colors.white,
            borderRadius: BorderRadius.circular(16),
            border: Border.all(color: Theme.of(context).primaryColor),
          ),
          child: Text(
            label,
            style: textStyle ??
                Theme.of(context)
                    .textTheme
                    .titleLarge
                    ?.copyWith(color: isSelected ? Colors.white : Colors.black),
          ),
        ),
      ),
    );
  }
}

class ConnectedLists extends StatefulWidget {
  final List<String> leftWords;
  final List<String> rightWords;
  final int selectedRightWord;
  final Function(int)? onSelectionChanged;
  final List<Attention> attentions;
  final List<double> scores;
  final double patientMaxAttention;
  const ConnectedLists({
    Key? key,
    required this.patientMaxAttention,
    required this.leftWords,
    required this.rightWords,
    required this.selectedRightWord,
    this.onSelectionChanged,
    required this.scores,
    required this.attentions, // constructor parameter
  }) : super(key: key);

  @override
  State<ConnectedLists> createState() => _ConnectedListsState();
}

class _ConnectedListsState extends State<ConnectedLists> {
  final List<GlobalKey> _leftKeys = [];
  final List<GlobalKey> _rightKeys = [];
  final GlobalKey _parentKey = GlobalKey();

  List<Offset> _leftPositions = [];
  List<Offset> _rightPositions = [];
  List<Size> _leftSizes = [];
  List<Size> _rightSizes = [];
  int? _selectedRightIndex;

  @override
  void initState() {
    super.initState();

    WidgetsBinding.instance.addPostFrameCallback((_) {
      _calculatePositions();
    });
  }

  void _calculatePositions() {
    _leftKeys
        .addAll(List.generate(widget.leftWords.length, (_) => GlobalKey()));
    _rightKeys
        .addAll(List.generate(widget.rightWords.length, (_) => GlobalKey()));
    if (_parentKey.currentContext == null) return;
    final parentBox =
        _parentKey.currentContext!.findRenderObject() as RenderBox;
    final parentOffset = parentBox.localToGlobal(Offset.zero);

    final leftPositions = <Offset>[];
    final rightPositions = <Offset>[];
    final leftSizes = <Size>[];
    final rightSizes = <Size>[];

    for (var key in _leftKeys) {
      if (key.currentContext == null) continue;
      final box = key.currentContext!.findRenderObject() as RenderBox;
      final globalPos = box.localToGlobal(Offset.zero);
      leftPositions.add(globalPos - parentOffset);
      leftSizes.add(box.size);
    }

    for (var key in _rightKeys) {
      if (key.currentContext == null) continue;
      final box = key.currentContext!.findRenderObject() as RenderBox;
      final globalPos = box.localToGlobal(Offset.zero);
      rightPositions.add(globalPos - parentOffset);
      rightSizes.add(box.size);
    }

    int selectedRightIndex = 0;
    selectedRightIndex =
        widget.rightWords.indexOf(widget.selectedRightWord!.toString());
    if (selectedRightIndex == -1) {
      selectedRightIndex = 0; // If not found, no filtering
    }

    setState(() {
      _leftPositions = leftPositions;
      _rightPositions = rightPositions;
      _leftSizes = leftSizes;
      _rightSizes = rightSizes;
      _selectedRightIndex = selectedRightIndex;
    });
  }

  @override
  Widget build(BuildContext context) {
    return Stack(
      key: _parentKey,
      children: [
        CustomPaint(
          painter: _LinePainter(
            patientMaxAttention: widget.patientMaxAttention,
            scores: widget.scores,
            baseColor: Theme.of(context).primaryColor!,
            leftPositions: _leftPositions,
            rightPositions: _rightPositions,
            leftSizes: _leftSizes,
            rightSizes: _rightSizes,
            selectedRightIndex: _selectedRightIndex,
          ),
          child: Container(),
        ),
        Row(
          mainAxisAlignment: MainAxisAlignment.spaceEvenly,
          children: [
            Column(
              mainAxisSize: MainAxisSize.min,
              crossAxisAlignment: CrossAxisAlignment.end,
              children: List.generate(widget.leftWords.length, (index) {
                Attention? attention = widget.attentions.firstWhere(
                    (element) => element.phenotypes == widget.leftWords[index],
                    orElse: () => Attention());
                if (_leftKeys.length <= index) return Container();
                return Container(
                  key: _leftKeys[index],
                  decoration: BoxDecoration(
                    borderRadius: BorderRadius.circular(2),
                    color: attention.attention != null
                        ? Theme.of(context).primaryColor!.withOpacity(
                            attention.attention! / widget.patientMaxAttention)
                        : Colors.white,
                    border: Border.all(
                      color: Theme.of(context).primaryColor!,
                    ),
                  ),
                  margin: const EdgeInsets.only(right: 16.0),
                  child: SizedBox(
                    width: 300,
                    child: Column(
                      crossAxisAlignment: CrossAxisAlignment.start,
                      children: [
                        Padding(
                          padding: const EdgeInsets.all(4.0),
                          child: Text(
                            widget.leftWords[index],
                            style: Theme.of(context)
                                .textTheme
                                .bodyMedium
                                ?.copyWith(
                                    color: attention.attention! /
                                                widget.patientMaxAttention >
                                            0.5
                                        ? Colors.white
                                        : Colors.black),
                            maxLines: 3,
                          ),
                        ),
                      ],
                    ),
                  ),
                );
              }),
            ),
            Column(
              mainAxisSize: MainAxisSize.min,
              crossAxisAlignment: CrossAxisAlignment.start,
              children: List.generate(widget.rightWords.length, (index) {
                bool isSelected = widget.selectedRightWord.toString() ==
                    widget.rightWords[index].toString();
                return Padding(
                  padding: const EdgeInsets.all(8.0),
                  child: Container(
                    key: _rightKeys[index],
                    margin: const EdgeInsets.only(left: 16.0),
                    child: CustomToggleButton(
                      noPadding: true,
                      label: widget.rightWords[index],
                      onSelect: (label) {
                        widget.onSelectionChanged?.call(int.parse(label));
                        WidgetsBinding.instance!.addPostFrameCallback((_) {
                          _calculatePositions();
                        });
                      },
                      currentSelection: widget.selectedRightWord.toString(),
                      textStyle: TextStyle(
                        color: isSelected ? Colors.white : Colors.black,
                      ),
                    ),
                  ),
                );
              }),
            ),
          ],
        ),
      ],
    );
  }
}

class _LinePainter extends CustomPainter {
  final Color baseColor;
  final List<Offset> leftPositions;
  final List<Offset> rightPositions;
  final List<Size> leftSizes;
  final List<Size> rightSizes;
  final int? selectedRightIndex;
  final List<double> scores;
  final double patientMaxAttention;

  _LinePainter({
    required this.scores,
    required this.baseColor,
    required this.leftPositions,
    required this.rightPositions,
    required this.leftSizes,
    required this.rightSizes,
    required this.patientMaxAttention,
    this.selectedRightIndex,
  });

  @override
  void paint(Canvas canvas, Size size) {
    if (leftPositions.isEmpty || rightPositions.isEmpty) return;

    for (int i = 0; i < leftPositions.length; i++) {
      if (selectedRightIndex != null) {
        final start = Offset(
          leftPositions[i].dx + leftSizes[i].width,
          leftPositions[i].dy + leftSizes[i].height / 2,
        );
        final end = Offset(
          rightPositions[selectedRightIndex!].dx,
          rightPositions[selectedRightIndex!].dy +
              rightSizes[selectedRightIndex!].height / 2,
        );
        double score;
        if (scores.length > i) {
          score = scores[i] / patientMaxAttention;
        } else {
          score = 0;
        }

        Color color = baseColor.withOpacity(score);

        final paint = Paint()
          ..color = color
          ..strokeWidth = 1.5;
        canvas.drawLine(start, end, paint);
      } else {
        for (int j = 0; j < rightPositions.length; j++) {
          final start = Offset(
            leftPositions[i].dx + leftSizes[i].width / 2,
            leftPositions[i].dy + leftSizes[i].height / 2,
          );
          final end = Offset(
            rightPositions[j].dx + rightSizes[j].width / 2,
            rightPositions[j].dy + rightSizes[j].height / 2,
          );
          double score = 0;
          if (scores.length > i) {
            score = scores[i];
          }
          Color color = baseColor.withOpacity(score);
          final paint = Paint()
            ..color = color
            ..strokeWidth = 1.5;
          canvas.drawLine(start, end, paint);
        }
      }
    }
  }

  @override
  bool shouldRepaint(covariant _LinePainter oldDelegate) {
    return oldDelegate.leftPositions != leftPositions ||
        oldDelegate.rightPositions != rightPositions ||
        oldDelegate.leftSizes != leftSizes ||
        oldDelegate.rightSizes != rightSizes ||
        oldDelegate.selectedRightIndex != selectedRightIndex;
  }
}
