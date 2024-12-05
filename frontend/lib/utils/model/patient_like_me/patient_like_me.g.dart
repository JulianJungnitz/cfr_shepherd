// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'patient_like_me.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

_$PatientLikeMeImpl _$$PatientLikeMeImplFromJson(Map<String, dynamic> json) =>
    _$PatientLikeMeImpl(
      patient_id: (json['patient_id'] as num?)?.toInt(),
      candidate_patients: (json['candidate_patients'] as num?)?.toInt(),
      similarities: (json['similarities'] as num?)?.toDouble(),
    );

Map<String, dynamic> _$$PatientLikeMeImplToJson(_$PatientLikeMeImpl instance) =>
    <String, dynamic>{
      'patient_id': instance.patient_id,
      'candidate_patients': instance.candidate_patients,
      'similarities': instance.similarities,
    };
