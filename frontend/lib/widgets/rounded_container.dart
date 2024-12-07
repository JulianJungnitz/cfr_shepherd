
import 'package:flutter/material.dart';

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
