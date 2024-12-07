// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'phenotype.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

_$PhenotypeImpl _$$PhenotypeImplFromJson(Map<String, dynamic> json) =>
    _$PhenotypeImpl(
      synonyms: (json['synonyms'] as List<dynamic>?)
          ?.map((e) => e as String)
          .toList(),
      name: json['name'] as String?,
      description: json['description'] as String?,
      id: json['id'] as String?,
      type: json['type'] as String?,
    );

Map<String, dynamic> _$$PhenotypeImplToJson(_$PhenotypeImpl instance) =>
    <String, dynamic>{
      'synonyms': instance.synonyms,
      'name': instance.name,
      'description': instance.description,
      'id': instance.id,
      'type': instance.type,
    };
