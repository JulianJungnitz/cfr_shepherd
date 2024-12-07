import 'package:freezed_annotation/freezed_annotation.dart';

part 'disease.freezed.dart';
part 'disease.g.dart';

@freezed
class Disease with _$Disease {
  const factory Disease({
    @JsonKey(name: 'synonyms') List<String>? synonyms,
    @JsonKey(name: 'name') String? name,
    @JsonKey(name: 'description') String? description,
    @JsonKey(name: 'id') String? id,
    @JsonKey(name: 'type') String? type,
  }) = _Disease;

  factory Disease.fromJson(Map<String, Object?> json) => _$DiseaseFromJson(json);
}

