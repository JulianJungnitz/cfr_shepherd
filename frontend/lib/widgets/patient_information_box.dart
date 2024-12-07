import 'package:expandable_text/expandable_text.dart';
import 'package:flutter/material.dart';
import 'package:frontend/utils/model/patient/patient.dart';
import 'package:frontend/widgets/rounded_container.dart';

class PatientInformationBox extends StatelessWidget {
  final Patient? patient;
  const PatientInformationBox({
    super.key, this.patient,
  });

  @override
  Widget build(BuildContext context) {
    return RoundedContainer(
        shadow: true,
        child: Container(
          width: double.infinity,
          child: Column(
            children: [
              InformationBoxHeader(
                title: 'Patient Information',
              ),
              patient == null
                  ? Container(
                height: 200,
                child: Center(
                  child: CircularProgressIndicator(),
                ),
              )
                  : Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  Text(
                    'Subject ID: ${patient!.biologicalSample?.subjectid}',
                    style: Theme.of(context).textTheme.headlineSmall,
                  ),
                  Text(
                    'Biological Sample ID: ${patient!.sampleId}',
                    style: Theme.of(context).textTheme.headlineSmall,
                  ),
                  Divider(),
                  SizedBox(
                    height: 16,
                  ),
                  ExpandableTextSection(
                    title: 'Genes',
                    text: patient!.genes!
                        .map((e) =>
                    "${e.id}"+ " ("+(e.synonyms?.sublist(1,).firstOrNull ?? "--")+ ")")
                        .fold(
                      "",
                          (previousValue, element) {
                        return previousValue += element + ", ";
                      },
                    ),
                  ),
                  ExpandableTextSection(
                    title: 'Phenotypes',
                    text: patient!.phenotypes!
                        .map((e) => e.name??"--").fold(
                      "",
                          (previousValue, element) {
                        return previousValue += element + ", ";
                      },
                    )
                        .toString(),
                  ),
                  ExpandableTextSection(
                    title: 'Diseases',
                    text: patient!.diseases!.map((e)=>e.name??"--").fold(
                      "",
                          (previousValue, element) {
                        return previousValue += element+ ", ";
                      },
                    ).toString(),
                    isLast: true,
                  ),
                ],
              ),
            ],
          ),
        ));
  }
}

class ExpandableTextSection extends StatefulWidget {
  final String title;
  final String text;
  final bool isLast;
  const ExpandableTextSection({
    super.key,
    required this.title,
    required this.text,
    this.isLast = false,
  });

  @override
  State<ExpandableTextSection> createState() => _ExpandableTextSectionState();
}

class _ExpandableTextSectionState extends State<ExpandableTextSection> {
  @override
  Widget build(BuildContext context) {
    return Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: [
        Text(
          widget.title,
          style: Theme.of(context).textTheme.headlineSmall,
        ),
        ExpandableText(
          widget.text,
          expandText: 'Show more',
          collapseText: 'Show less',
          maxLines: 3,
          linkColor: Theme.of(context).primaryColor,
          style: Theme.of(context).textTheme.bodyMedium
        ),
        if(!widget.isLast) Divider(),
        if (!widget.isLast) SizedBox(height: 8),

      ],
    );
  }
}

class InformationBoxHeader extends StatelessWidget {
  final Widget? trailing;
  final String title;
  const InformationBoxHeader({
    super.key,
    this.trailing,
    required this.title,
  });

  @override
  Widget build(BuildContext context) {
    return Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: [
        SizedBox(
          height: 50,
          child: Row(
            mainAxisAlignment: MainAxisAlignment.spaceBetween,
            children: [
              Text(
                title,
                style: Theme.of(context).textTheme.headlineMedium,
              ),
              trailing ?? Container(),
            ],
          ),
        ),
        Divider(),
        SizedBox(
          height: 16,
        ),
      ],
    );
  }
}
