// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'gene.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

_$GeneImpl _$$GeneImplFromJson(Map<String, dynamic> json) => _$GeneImpl(
      taxid: json['taxid'] as String?,
      synonyms: (json['synonyms'] as List<dynamic>?)
          ?.map((e) => e as String)
          .toList(),
      name: json['name'] as String?,
      id: json['id'] as String?,
      family: json['family'] as String?,
    );

Map<String, dynamic> _$$GeneImplToJson(_$GeneImpl instance) =>
    <String, dynamic>{
      'taxid': instance.taxid,
      'synonyms': instance.synonyms,
      'name': instance.name,
      'id': instance.id,
      'family': instance.family,
    };
