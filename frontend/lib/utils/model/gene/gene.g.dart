// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'gene.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

_$GeneImpl _$$GeneImplFromJson(Map<String, dynamic> json) => _$GeneImpl(
      identity: (json['identity'] as num?)?.toInt(),
      labels:
          (json['labels'] as List<dynamic>?)?.map((e) => e as String).toList(),
      properties: json['properties'] == null
          ? null
          : Properties.fromJson(json['properties'] as Map<String, dynamic>),
      elementId: json['elementId'] as String?,
    );

Map<String, dynamic> _$$GeneImplToJson(_$GeneImpl instance) =>
    <String, dynamic>{
      'identity': instance.identity,
      'labels': instance.labels,
      'properties': instance.properties,
      'elementId': instance.elementId,
    };

_$PropertiesImpl _$$PropertiesImplFromJson(Map<String, dynamic> json) =>
    _$PropertiesImpl(
      taxid: json['taxid'] as String?,
      synonyms: (json['synonyms'] as List<dynamic>?)
          ?.map((e) => e as String)
          .toList(),
      name: json['name'] as String?,
      id: json['id'] as String?,
    );

Map<String, dynamic> _$$PropertiesImplToJson(_$PropertiesImpl instance) =>
    <String, dynamic>{
      'taxid': instance.taxid,
      'synonyms': instance.synonyms,
      'name': instance.name,
      'id': instance.id,
    };
