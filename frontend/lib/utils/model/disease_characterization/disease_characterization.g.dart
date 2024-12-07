// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'disease_characterization.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

_$DiseaseCharacterizationImpl _$$DiseaseCharacterizationImplFromJson(
        Map<String, dynamic> json) =>
    _$DiseaseCharacterizationImpl(
      patientId: (json['patient_id'] as num?)?.toInt(),
      diseases: json['diseases'] as String?,
      similarities: (json['similarities'] as num?)?.toDouble(),
    );

Map<String, dynamic> _$$DiseaseCharacterizationImplToJson(
        _$DiseaseCharacterizationImpl instance) =>
    <String, dynamic>{
      'patient_id': instance.patientId,
      'diseases': instance.diseases,
      'similarities': instance.similarities,
    };
