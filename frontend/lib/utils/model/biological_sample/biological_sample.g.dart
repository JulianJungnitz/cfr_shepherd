// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'biological_sample.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

_$BiologicalSampleImpl _$$BiologicalSampleImplFromJson(
        Map<String, dynamic> json) =>
    _$BiologicalSampleImpl(
      identity: (json['identity'] as num?)?.toInt(),
      labels:
          (json['labels'] as List<dynamic>?)?.map((e) => e as String).toList(),
      properties: json['properties'] == null
          ? null
          : Properties.fromJson(json['properties'] as Map<String, dynamic>),
      elementId: json['elementId'] as String?,
    );

Map<String, dynamic> _$$BiologicalSampleImplToJson(
        _$BiologicalSampleImpl instance) =>
    <String, dynamic>{
      'identity': instance.identity,
      'labels': instance.labels,
      'properties': instance.properties,
      'elementId': instance.elementId,
    };

_$PropertiesImpl _$$PropertiesImplFromJson(Map<String, dynamic> json) =>
    _$PropertiesImpl(
      externalId: json['external_id'] as String?,
      subjectid: (json['subjectid'] as num?)?.toInt(),
    );

Map<String, dynamic> _$$PropertiesImplToJson(_$PropertiesImpl instance) =>
    <String, dynamic>{
      'external_id': instance.externalId,
      'subjectid': instance.subjectid,
    };
