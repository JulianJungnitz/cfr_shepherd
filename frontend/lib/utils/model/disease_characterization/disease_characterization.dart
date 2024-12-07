import 'package:freezed_annotation/freezed_annotation.dart';

part 'disease_characterization.freezed.dart';
part 'disease_characterization.g.dart';

@freezed
class DiseaseCharacterization with _$DiseaseCharacterization {
  const factory DiseaseCharacterization({
    @JsonKey(name: 'patient_id') int? patientId,
    @JsonKey(name: 'diseases') String? diseases,
    @JsonKey(name: 'similarities') double? similarities,
  }) = _DiseaseCharacterization;

  factory DiseaseCharacterization.fromJson(Map<String, Object?> json) => _$DiseaseCharacterizationFromJson(json);
}

