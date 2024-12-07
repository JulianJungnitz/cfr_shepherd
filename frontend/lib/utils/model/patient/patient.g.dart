// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'patient.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

_$PatientImpl _$$PatientImplFromJson(Map<String, dynamic> json) =>
    _$PatientImpl(
      biologicalSample: json['biological_sample'] as String?,
      genes: json['genes'] as String?,
      phenotypes: json['phenotypes'] as String?,
      subjectId: (json['subject_id'] as num?)?.toInt(),
    );

Map<String, dynamic> _$$PatientImplToJson(_$PatientImpl instance) =>
    <String, dynamic>{
      'biological_sample': instance.biologicalSample,
      'genes': instance.genes,
      'phenotypes': instance.phenotypes,
      'subject_id': instance.subjectId,
    };
