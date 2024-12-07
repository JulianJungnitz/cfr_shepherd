import 'package:freezed_annotation/freezed_annotation.dart';

part 'phenotype.freezed.dart';
part 'phenotype.g.dart';

@freezed
class Phenotype with _$Phenotype {
  const factory Phenotype({
    @JsonKey(name: 'identity') int? identity,
    @JsonKey(name: 'labels') List<String>? labels,
    @JsonKey(name: 'properties') Properties? properties,
    @JsonKey(name: 'elementId') String? elementId,
  }) = _Phenotype;

  factory Phenotype.fromJson(Map<String, Object?> json) => _$PhenotypeFromJson(json);
}

@freezed
class Properties with _$Properties {
  const factory Properties({
    @JsonKey(name: 'synonyms') List<String>? synonyms,
    @JsonKey(name: 'name') String? name,
    @JsonKey(name: 'description') String? description,
    @JsonKey(name: 'id') String? id,
    @JsonKey(name: 'type') String? type,
  }) = _Properties;

  factory Properties.fromJson(Map<String, Object?> json) => _$PropertiesFromJson(json);
}

