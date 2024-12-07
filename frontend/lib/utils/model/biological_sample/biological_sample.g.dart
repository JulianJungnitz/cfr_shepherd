// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'biological_sample.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

_$BiologicalSampleImpl _$$BiologicalSampleImplFromJson(
        Map<String, dynamic> json) =>
    _$BiologicalSampleImpl(
      externalId: json['external_id'] as String?,
      subjectid: (json['subjectid'] as num?)?.toInt(),
    );

Map<String, dynamic> _$$BiologicalSampleImplToJson(
        _$BiologicalSampleImpl instance) =>
    <String, dynamic>{
      'external_id': instance.externalId,
      'subjectid': instance.subjectid,
    };
