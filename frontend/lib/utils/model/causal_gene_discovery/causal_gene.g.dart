// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'causal_gene.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

_$CausalGeneImpl _$$CausalGeneImplFromJson(Map<String, dynamic> json) =>
    _$CausalGeneImpl(
      patientId: (json['patient_id'] as num?)?.toInt(),
      genes: json['genes'] as String?,
      similarities: (json['similarities'] as num?)?.toDouble(),
    );

Map<String, dynamic> _$$CausalGeneImplToJson(_$CausalGeneImpl instance) =>
    <String, dynamic>{
      'patient_id': instance.patientId,
      'genes': instance.genes,
      'similarities': instance.similarities,
    };
