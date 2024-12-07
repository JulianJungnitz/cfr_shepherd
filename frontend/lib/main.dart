import 'package:flutter/material.dart';
import 'package:frontend/screens/patient_analysis_screen.dart';
import 'package:frontend/utils/api.dart';
import 'package:frontend/utils/patient_data_provider.dart';
import 'package:provider/provider.dart';

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
        colorScheme: ColorScheme.fromSeed(seedColor:Colors.indigo),
        useMaterial3: true,
      ),
      home: MultiProvider(
        providers: [
          ChangeNotifierProvider(create: (context) => PatientDataProvider()),
        ],
        child: PatientAnalysisScreen()),
    );
  }
}
