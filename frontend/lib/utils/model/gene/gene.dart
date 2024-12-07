import 'package:freezed_annotation/freezed_annotation.dart';

part 'gene.freezed.dart';
part 'gene.g.dart';

@freezed
class Gene with _$Gene {
  const factory Gene({
    @JsonKey(name: 'identity') int? identity,
    @JsonKey(name: 'labels') List<String>? labels,
    @JsonKey(name: 'properties') Properties? properties,
    @JsonKey(name: 'elementId') String? elementId,
  }) = _Gene;

  factory Gene.fromJson(Map<String, Object?> json) => _$GeneFromJson(json);
}

@freezed
class Properties with _$Properties {
  const factory Properties({
    @JsonKey(name: 'taxid') String? taxid,
    @JsonKey(name: 'synonyms') List<String>? synonyms,
    @JsonKey(name: 'name') String? name,
    @JsonKey(name: 'id') String? id,
  }) = _Properties;

  factory Properties.fromJson(Map<String, Object?> json) => _$PropertiesFromJson(json);
}

