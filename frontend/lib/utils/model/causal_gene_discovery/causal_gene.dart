import 'package:freezed_annotation/freezed_annotation.dart';

part 'causal_gene.freezed.dart';
part 'causal_gene.g.dart';

@freezed
class CausalGene with _$CausalGene {
  const factory CausalGene({
    @JsonKey(name: 'patient_id') int? patientId,
    @JsonKey(name: 'genes') String? genes,
    @JsonKey(name: 'similarities') double? similarities,
  }) = _CausalGene;

  factory CausalGene.fromJson(Map<String, Object?> json) => _$CausalGeneFromJson(json);
}

