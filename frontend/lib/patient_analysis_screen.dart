
import 'package:flutter/material.dart';

class PatientAnalysisScreen extends StatelessWidget {
  const PatientAnalysisScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Patient Analysis'),
      ),
      body: const Center(
        child: Text('Patient Analysis Screen'),
      ),
    );
  }
}