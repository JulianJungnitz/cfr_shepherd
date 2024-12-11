import 'package:freezed_annotation/freezed_annotation.dart';

part 'attention.freezed.dart';
part 'attention.g.dart';

@freezed
class Attention with _$Attention {
  const factory Attention({
    @JsonKey(name: 'patient_id') int? patientId,
    @JsonKey(name: 'phenotypes') String? phenotypes,
    @JsonKey(name: 'attention') double? attention,
  }) = _Attention;

  factory Attention.fromJson(Map<String, Object?> json) => _$AttentionFromJson(json);
}

