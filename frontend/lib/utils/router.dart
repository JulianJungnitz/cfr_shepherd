import 'package:flutter/material.dart';
import 'package:frontend/screens/home_screen.dart';
import 'package:frontend/screens/patient_analysis_screen.dart';
import 'package:go_router/go_router.dart';

class Routes {
  static const home = '/';
  static const patientAnalysis = '/patients';
}

final GoRouter router = GoRouter(
  routes: <RouteBase>[
    GoRoute(
      path: Routes.home,
      builder: (BuildContext context, GoRouterState state) {
        return const HomeScreen();
      },

    ),
    GoRoute(
      path: Routes.patientAnalysis + '/:patientId',
      builder: (BuildContext context, GoRouterState state) {
        var patientIdString = state.pathParameters['patientId']!;
        var patientId = int.tryParse(patientIdString) ?? 0;
        return PatientAnalysisScreen(
          patientId: patientId,
        );
      },
    ),
    GoRoute(path: "test", builder: (context, state) {
      return const Text("Test");
    }),

  ],
  errorBuilder: (context, state) {
    return Scaffold(
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            Text(
              "404",
              style: Theme.of(context).textTheme.headlineLarge,
            ),
            Text(
              "Page not found",
              style: Theme.of(context).textTheme.headlineMedium,
            ),
            TextButton(
                onPressed: () {
                  context.go(Routes.home);
                },
                child: Text("Go back to main screen"))
          ],
        ),
      ),
    );
  },
);
