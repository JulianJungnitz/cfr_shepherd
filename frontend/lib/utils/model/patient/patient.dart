import 'package:freezed_annotation/freezed_annotation.dart';

part 'patient.freezed.dart';
part 'patient.g.dart';

@freezed
class Patient with _$Patient {
  const factory Patient({
    @JsonKey(name: 'biological_sample') String? biologicalSample,
    @JsonKey(name: 'genes') String? genes,
    @JsonKey(name: 'phenotypes') String? phenotypes,
    @JsonKey(name: 'subject_id') int? subjectId,
  }) = _Patient;

  factory Patient.fromJson(Map<String, Object?> json) => _$PatientFromJson(json);
}

