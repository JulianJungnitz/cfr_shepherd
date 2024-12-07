import 'package:freezed_annotation/freezed_annotation.dart';

part 'gene.freezed.dart';
part 'gene.g.dart';

@freezed
class Gene with _$Gene {
  const factory Gene({
    @JsonKey(name: 'taxid') String? taxid,
    @JsonKey(name: 'synonyms') List<String>? synonyms,
    @JsonKey(name: 'name') String? name,
    @JsonKey(name: 'id') String? id,
    @JsonKey(name: 'family') String? family,
  }) = _Gene;

  factory Gene.fromJson(Map<String, Object?> json) => _$GeneFromJson(json);
}

