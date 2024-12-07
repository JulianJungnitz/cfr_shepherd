import 'package:freezed_annotation/freezed_annotation.dart';

part 'biological_sample.freezed.dart';
part 'biological_sample.g.dart';

@freezed
class BiologicalSample with _$BiologicalSample {
  const factory BiologicalSample({
    @JsonKey(name: 'identity') int? identity,
    @JsonKey(name: 'labels') List<String>? labels,
    @JsonKey(name: 'properties') Properties? properties,
    @JsonKey(name: 'elementId') String? elementId,
  }) = _BiologicalSample;

  factory BiologicalSample.fromJson(Map<String, Object?> json) => _$BiologicalSampleFromJson(json);
}

@freezed
class Properties with _$Properties {
  const factory Properties({
    @JsonKey(name: 'external_id') String? externalId,
    @JsonKey(name: 'subjectid') int? subjectid,
  }) = _Properties;

  factory Properties.fromJson(Map<String, Object?> json) => _$PropertiesFromJson(json);
}

