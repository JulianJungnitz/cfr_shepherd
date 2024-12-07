import 'dart:math';

import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:frontend/utils/api.dart';
import 'package:frontend/utils/patient_data_provider.dart';
import 'package:frontend/utils/router.dart';
import 'package:frontend/widgets/rounded_container.dart';
import 'package:go_router/go_router.dart';
import 'package:provider/provider.dart';

class HomeScreen extends StatefulWidget {
  const HomeScreen({super.key});

  @override
  State<HomeScreen> createState() => _HomeScreenState();
}

class _HomeScreenState extends State<HomeScreen> {
  TextEditingController patientIdController = TextEditingController();
  GlobalKey<FormState> formKey = GlobalKey<FormState>();

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Home'),
      ),
      body: Center(
        child: Padding(
          padding: const EdgeInsets.all(32.0),
          child: Column(
            mainAxisAlignment: MainAxisAlignment.center,
            children: [
              RoundedContainer(
                shadow: true,
                child: SizedBox(
                  width: min(600, MediaQuery.of(context).size.width - 32),
                  child: Column(
                    crossAxisAlignment: CrossAxisAlignment.start,
                    children: [
                      Text(
                        'Care For Rare - SHEPHERD',
                        style: Theme.of(context).textTheme.headlineLarge,
                      ),
                      const SizedBox(height: 16),
                      Text(
                        'Please enter the patient ID to view the patient analysis',
                        style: Theme.of(context).textTheme.bodyMedium,
                      ),
                      SizedBox(height: 12),
                      Form(
                        key: formKey,
                        child: TextFormField(
                          validator: (value) {
                            if (value == null || value.isEmpty) {
                              return 'Please enter a patient ID';
                            }
                            return null;
                          },
                          controller: patientIdController,
                          decoration: InputDecoration(
                            border: OutlineInputBorder(),
                            labelText: 'Patient ID',
                            suffixIcon: Padding(
                              padding: const EdgeInsets.all(4.0),
                              child: Container(
                                width: 48,
                                height: 48,
                                decoration: BoxDecoration(
                                  color: Colors.blue,
                                  borderRadius: BorderRadius.circular(8),
                                ),
                                child: IconButton(
                                  icon: const Icon(Icons.search,
                                      color: Colors.white),
                                  onPressed: () {
                                    if (!formKey.currentState!.validate())
                                      return;
                                    pushToPatientAnalysisScreen(context,
                                        int.parse(patientIdController.text));
                                  },
                                ),
                              ),
                            ),
                          ),
                          keyboardType: TextInputType.number,
                          inputFormatters: <TextInputFormatter>[
                            FilteringTextInputFormatter.digitsOnly
                          ],
                          onEditingComplete: () {
                            if (!formKey.currentState!.validate()) return;
                            pushToPatientAnalysisScreen(
                                context, int.parse(patientIdController.text));
                          },
                        ),
                      ),
                      SizedBox(height: 32),
                      Divider(
                        color: Colors.grey.shade300,
                      ),
                      SizedBox(height: 16),
                      Text(
                        'System Checks',
                        style: Theme.of(context).textTheme.headlineMedium,
                      ),
                      StatusCheckBox(
                        text: 'API Connection',
                        check: () async {
                          APIResult res = await API.get("/", rawString: true);
                          return res.success;
                        },
                      ),
                      StatusCheckBox(
                        text: 'Database Connection',
                        check: () async {
                          var res = await context
                              .read<PatientDataProvider>()
                              .queryNeo4J("MATCH (n) RETURN count(n) as count");
                          if (res.success) {
                            if (res.data.length > 0) {
                              return true;
                            }
                          }
                          return false;
                        },
                      ),
                      StatusCheckBox(
                        text: 'Has results for Patients Like Me',
                        check: () async {
                          var res = await API.get(APIPaths.hasPatientsLikeMeResults);
                          return res.success;
                        },
                      ),
                      StatusCheckBox(
                        text: 'Has results for Causal Gene Discovery',
                        check: () async {
                          var res = await API.get(APIPaths.hasCausalGeneDiscoveryResults);
                          return res.success;
                        },
                      ),
                      StatusCheckBox(
                        text: 'Has results for Disease Characterization',
                        check: () async {
                          var res = await API.get(APIPaths.hasDiseaseCharacterizationResults);
                          return res.success;
                        },
                      ),
                    ],
                  ),
                ),
              ),
            ],
          ),
        ),
      ),
    );
  }

  void pushToPatientAnalysisScreen(BuildContext context, int patientId) {
    context.go("${Routes.patientAnalysis}/$patientId");
  }
}

class StatusCheckBox extends StatefulWidget {
  final Future<bool> Function() check;
  final String text;
  const StatusCheckBox({super.key, required this.check, required this.text});

  @override
  State<StatusCheckBox> createState() => _StatusCheckBoxState();
}

class _StatusCheckBoxState extends State<StatusCheckBox> {
  bool? checked;

  @override
  void initState() {
    super.initState();
    widget.check().then((value) {
      setState(() {
        checked = value;
      });
    });
  }

  @override
  Widget build(BuildContext context) {
    return Padding(
      padding: const EdgeInsets.symmetric(vertical: 8.0),
      child: Container(
        height: 64,
        decoration: BoxDecoration(
          color: Colors.white,
          borderRadius: BorderRadius.circular(8),
          boxShadow: [
            BoxShadow(
              color: Colors.grey.withOpacity(0.5),
              spreadRadius: 1,
              blurRadius: 2,
              offset: const Offset(0, 0),
            ),
          ],
        ),
        child: ClipRRect(
          borderRadius: BorderRadius.circular(6),
          child: Row(
            children: [
              Container(
                width: 64,
                height: 64,
                decoration: BoxDecoration(
                  color: checked == null
                      ? Colors.grey
                      : checked!
                          ? Colors.green
                          : Colors.red,
                  borderRadius: BorderRadius.only(),
                ),
                child: checked == null
                    ? Center(
                        child: SizedBox(
                            width: 24,
                            height: 24,
                            child: CircularProgressIndicator(
                              color: Colors.white,
                              strokeWidth: 2,
                              strokeCap: StrokeCap.round,
                            )),
                      )
                    : checked!
                        ? const Icon(
                            Icons.check,
                            color: Colors.white,
                          )
                        : const Icon(
                            Icons.close,
                            color: Colors.white,
                          ),
              ),
              Padding(
                padding: const EdgeInsets.all(8.0),
                child: Text(
                  widget.text,
                  style: Theme.of(context).textTheme.titleMedium,
                ),
              ),
              Spacer(),
              Padding(
                padding: const EdgeInsets.all(8.0),
                child: IconButton(
                  icon: const Icon(
                    Icons.refresh,
                    color: Colors.grey,
                  ),
                  onPressed: () {
                    setState(() {
                      checked = null;
                    });
                    widget.check().then((value) {
                      setState(() {
                        checked = value;
                      });
                    });
                  },
                ),
              ),
            ],
          ),
        ),
      ),
    );
  }
}
