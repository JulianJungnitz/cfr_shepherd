// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'phenotype.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

_$PhenotypeImpl _$$PhenotypeImplFromJson(Map<String, dynamic> json) =>
    _$PhenotypeImpl(
      identity: (json['identity'] as num?)?.toInt(),
      labels:
          (json['labels'] as List<dynamic>?)?.map((e) => e as String).toList(),
      properties: json['properties'] == null
          ? null
          : Properties.fromJson(json['properties'] as Map<String, dynamic>),
      elementId: json['elementId'] as String?,
    );

Map<String, dynamic> _$$PhenotypeImplToJson(_$PhenotypeImpl instance) =>
    <String, dynamic>{
      'identity': instance.identity,
      'labels': instance.labels,
      'properties': instance.properties,
      'elementId': instance.elementId,
    };

_$PropertiesImpl _$$PropertiesImplFromJson(Map<String, dynamic> json) =>
    _$PropertiesImpl(
      synonyms: (json['synonyms'] as List<dynamic>?)
          ?.map((e) => e as String)
          .toList(),
      name: json['name'] as String?,
      description: json['description'] as String?,
      id: json['id'] as String?,
      type: json['type'] as String?,
    );

Map<String, dynamic> _$$PropertiesImplToJson(_$PropertiesImpl instance) =>
    <String, dynamic>{
      'synonyms': instance.synonyms,
      'name': instance.name,
      'description': instance.description,
      'id': instance.id,
      'type': instance.type,
    };
