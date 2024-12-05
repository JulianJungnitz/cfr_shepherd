import 'package:flutter/material.dart';
import 'package:frontend/patient_analysis_screen.dart';
import 'package:frontend/utils/api.dart';

void main() {
  runApp(const ShepherdApp());
}

class ShepherdApp extends StatelessWidget{
  const ShepherdApp({super.key,});


  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      title: 'Care For Rare - SHEPHERD',
      theme: ThemeData(
        colorScheme: ColorScheme.fromSeed(seedColor: Colors.deepPurple),
        useMaterial3: true,
      ),
      home: PatientAnalysisScreen(),
    );
  }
}
