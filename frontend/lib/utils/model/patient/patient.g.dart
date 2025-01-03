// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'patient.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

_$PatientImpl _$$PatientImplFromJson(Map<String, dynamic> json) =>
    _$PatientImpl(
      biologicalSample: json['biological_sample'] == null
          ? null
          : BiologicalSample.fromJson(
              json['biological_sample'] as Map<String, dynamic>),
      genes: (json['genes'] as List<dynamic>?)
          ?.map((e) => Gene.fromJson(e as Map<String, dynamic>))
          .toList(),
      phenotypes: (json['phenotypes'] as List<dynamic>?)
          ?.map((e) => Phenotype.fromJson(e as Map<String, dynamic>))
          .toList(),
      diseases: (json['diseases'] as List<dynamic>?)
          ?.map((e) => Disease.fromJson(e as Map<String, dynamic>))
          .toList(),
      sampleId: (json['sample_id'] as num?)?.toInt(),
    );

Map<String, dynamic> _$$PatientImplToJson(_$PatientImpl instance) =>
    <String, dynamic>{
      'biological_sample': instance.biologicalSample,
      'genes': instance.genes,
      'phenotypes': instance.phenotypes,
      'diseases': instance.diseases,
      'sample_id': instance.sampleId,
    };
