import 'package:freezed_annotation/freezed_annotation.dart';

part 'biological_sample.freezed.dart';
part 'biological_sample.g.dart';

@freezed
class BiologicalSample with _$BiologicalSample {
  const factory BiologicalSample({
    @JsonKey(name: 'external_id') String? externalId,
    @JsonKey(name: 'subjectid') int? subjectid,
  }) = _BiologicalSample;

  factory BiologicalSample.fromJson(Map<String, Object?> json) => _$BiologicalSampleFromJson(json);
}

