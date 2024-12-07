import 'package:flutter/material.dart';
import 'package:frontend/utils/patient_data_provider.dart';
import 'package:frontend/utils/router.dart';
import 'package:provider/provider.dart';
import 'package:url_strategy/url_strategy.dart';

void main() {
  setPathUrlStrategy();
  runApp(MultiProvider(
    providers: [
      ChangeNotifierProvider(create: (context) => PatientDataProvider()),
    ],
  child: const ShepherdApp()));
}

class ShepherdApp extends StatelessWidget{
  const ShepherdApp({super.key,});


  @override
  Widget build(BuildContext context) {
    return MaterialApp.router(
      debugShowCheckedModeBanner: false,
      title: 'Care For Rare - SHEPHERD',
      theme: ThemeData(
        colorScheme: ColorScheme.fromSeed(seedColor:Colors.indigo),
        useMaterial3: true,
      ),
      routerConfig: router,
    );
  }
}
