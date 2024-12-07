import 'package:freezed_annotation/freezed_annotation.dart';
import 'package:frontend/utils/model/biological_sample/biological_sample.dart';
import 'package:frontend/utils/model/disease/disease.dart';
import 'package:frontend/utils/model/gene/gene.dart';
import 'package:frontend/utils/model/phenotype/phenotype.dart';

part 'patient.freezed.dart';
part 'patient.g.dart';

@freezed
class Patient with _$Patient {
  const factory Patient({
    @JsonKey(name: 'biological_sample') BiologicalSample? biologicalSample,
    @JsonKey(name: 'genes') List<Gene>? genes,
    @JsonKey(name: 'phenotypes') List<Phenotype>? phenotypes,
    @JsonKey(name: 'diseases') List<Disease>? diseases,
    @JsonKey(name: 'sample_id') int? sampleId,
  }) = _Patient;

  factory Patient.fromJson(Map<String, Object?> json) => _$PatientFromJson(json);
}

