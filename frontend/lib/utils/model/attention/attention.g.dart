// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'attention.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

_$AttentionImpl _$$AttentionImplFromJson(Map<String, dynamic> json) =>
    _$AttentionImpl(
      patientId: (json['patient_id'] as num?)?.toInt(),
      phenotypes: json['phenotypes'] as String?,
      attention: (json['attention'] as num?)?.toDouble(),
    );

Map<String, dynamic> _$$AttentionImplToJson(_$AttentionImpl instance) =>
    <String, dynamic>{
      'patient_id': instance.patientId,
      'phenotypes': instance.phenotypes,
      'attention': instance.attention,
    };
