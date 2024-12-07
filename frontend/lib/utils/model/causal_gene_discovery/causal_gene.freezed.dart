// coverage:ignore-file
// GENERATED CODE - DO NOT MODIFY BY HAND
// ignore_for_file: type=lint
// ignore_for_file: unused_element, deprecated_member_use, deprecated_member_use_from_same_package, use_function_type_syntax_for_parameters, unnecessary_const, avoid_init_to_null, invalid_override_different_default_values_named, prefer_expression_function_bodies, annotate_overrides, invalid_annotation_target, unnecessary_question_mark

part of 'causal_gene.dart';

// **************************************************************************
// FreezedGenerator
// **************************************************************************

T _$identity<T>(T value) => value;

final _privateConstructorUsedError = UnsupportedError(
    'It seems like you constructed your class using `MyClass._()`. This constructor is only meant to be used by freezed and you are not supposed to need it nor use it.\nPlease check the documentation here for more information: https://github.com/rrousselGit/freezed#adding-getters-and-methods-to-our-models');

CausalGene _$CausalGeneFromJson(Map<String, dynamic> json) {
  return _CausalGene.fromJson(json);
}

/// @nodoc
mixin _$CausalGene {
  @JsonKey(name: 'patient_id')
  int? get patientId => throw _privateConstructorUsedError;
  @JsonKey(name: 'genes')
  String? get genes => throw _privateConstructorUsedError;
  @JsonKey(name: 'similarities')
  double? get similarities => throw _privateConstructorUsedError;

  /// Serializes this CausalGene to a JSON map.
  Map<String, dynamic> toJson() => throw _privateConstructorUsedError;

  /// Create a copy of CausalGene
  /// with the given fields replaced by the non-null parameter values.
  @JsonKey(includeFromJson: false, includeToJson: false)
  $CausalGeneCopyWith<CausalGene> get copyWith =>
      throw _privateConstructorUsedError;
}

/// @nodoc
abstract class $CausalGeneCopyWith<$Res> {
  factory $CausalGeneCopyWith(
          CausalGene value, $Res Function(CausalGene) then) =
      _$CausalGeneCopyWithImpl<$Res, CausalGene>;
  @useResult
  $Res call(
      {@JsonKey(name: 'patient_id') int? patientId,
      @JsonKey(name: 'genes') String? genes,
      @JsonKey(name: 'similarities') double? similarities});
}

/// @nodoc
class _$CausalGeneCopyWithImpl<$Res, $Val extends CausalGene>
    implements $CausalGeneCopyWith<$Res> {
  _$CausalGeneCopyWithImpl(this._value, this._then);

  // ignore: unused_field
  final $Val _value;
  // ignore: unused_field
  final $Res Function($Val) _then;

  /// Create a copy of CausalGene
  /// with the given fields replaced by the non-null parameter values.
  @pragma('vm:prefer-inline')
  @override
  $Res call({
    Object? patientId = freezed,
    Object? genes = freezed,
    Object? similarities = freezed,
  }) {
    return _then(_value.copyWith(
      patientId: freezed == patientId
          ? _value.patientId
          : patientId // ignore: cast_nullable_to_non_nullable
              as int?,
      genes: freezed == genes
          ? _value.genes
          : genes // ignore: cast_nullable_to_non_nullable
              as String?,
      similarities: freezed == similarities
          ? _value.similarities
          : similarities // ignore: cast_nullable_to_non_nullable
              as double?,
    ) as $Val);
  }
}

/// @nodoc
abstract class _$$CausalGeneImplCopyWith<$Res>
    implements $CausalGeneCopyWith<$Res> {
  factory _$$CausalGeneImplCopyWith(
          _$CausalGeneImpl value, $Res Function(_$CausalGeneImpl) then) =
      __$$CausalGeneImplCopyWithImpl<$Res>;
  @override
  @useResult
  $Res call(
      {@JsonKey(name: 'patient_id') int? patientId,
      @JsonKey(name: 'genes') String? genes,
      @JsonKey(name: 'similarities') double? similarities});
}

/// @nodoc
class __$$CausalGeneImplCopyWithImpl<$Res>
    extends _$CausalGeneCopyWithImpl<$Res, _$CausalGeneImpl>
    implements _$$CausalGeneImplCopyWith<$Res> {
  __$$CausalGeneImplCopyWithImpl(
      _$CausalGeneImpl _value, $Res Function(_$CausalGeneImpl) _then)
      : super(_value, _then);

  /// Create a copy of CausalGene
  /// with the given fields replaced by the non-null parameter values.
  @pragma('vm:prefer-inline')
  @override
  $Res call({
    Object? patientId = freezed,
    Object? genes = freezed,
    Object? similarities = freezed,
  }) {
    return _then(_$CausalGeneImpl(
      patientId: freezed == patientId
          ? _value.patientId
          : patientId // ignore: cast_nullable_to_non_nullable
              as int?,
      genes: freezed == genes
          ? _value.genes
          : genes // ignore: cast_nullable_to_non_nullable
              as String?,
      similarities: freezed == similarities
          ? _value.similarities
          : similarities // ignore: cast_nullable_to_non_nullable
              as double?,
    ));
  }
}

/// @nodoc
@JsonSerializable()
class _$CausalGeneImpl implements _CausalGene {
  const _$CausalGeneImpl(
      {@JsonKey(name: 'patient_id') this.patientId,
      @JsonKey(name: 'genes') this.genes,
      @JsonKey(name: 'similarities') this.similarities});

  factory _$CausalGeneImpl.fromJson(Map<String, dynamic> json) =>
      _$$CausalGeneImplFromJson(json);

  @override
  @JsonKey(name: 'patient_id')
  final int? patientId;
  @override
  @JsonKey(name: 'genes')
  final String? genes;
  @override
  @JsonKey(name: 'similarities')
  final double? similarities;

  @override
  String toString() {
    return 'CausalGene(patientId: $patientId, genes: $genes, similarities: $similarities)';
  }

  @override
  bool operator ==(Object other) {
    return identical(this, other) ||
        (other.runtimeType == runtimeType &&
            other is _$CausalGeneImpl &&
            (identical(other.patientId, patientId) ||
                other.patientId == patientId) &&
            (identical(other.genes, genes) || other.genes == genes) &&
            (identical(other.similarities, similarities) ||
                other.similarities == similarities));
  }

  @JsonKey(includeFromJson: false, includeToJson: false)
  @override
  int get hashCode => Object.hash(runtimeType, patientId, genes, similarities);

  /// Create a copy of CausalGene
  /// with the given fields replaced by the non-null parameter values.
  @JsonKey(includeFromJson: false, includeToJson: false)
  @override
  @pragma('vm:prefer-inline')
  _$$CausalGeneImplCopyWith<_$CausalGeneImpl> get copyWith =>
      __$$CausalGeneImplCopyWithImpl<_$CausalGeneImpl>(this, _$identity);

  @override
  Map<String, dynamic> toJson() {
    return _$$CausalGeneImplToJson(
      this,
    );
  }
}

abstract class _CausalGene implements CausalGene {
  const factory _CausalGene(
          {@JsonKey(name: 'patient_id') final int? patientId,
          @JsonKey(name: 'genes') final String? genes,
          @JsonKey(name: 'similarities') final double? similarities}) =
      _$CausalGeneImpl;

  factory _CausalGene.fromJson(Map<String, dynamic> json) =
      _$CausalGeneImpl.fromJson;

  @override
  @JsonKey(name: 'patient_id')
  int? get patientId;
  @override
  @JsonKey(name: 'genes')
  String? get genes;
  @override
  @JsonKey(name: 'similarities')
  double? get similarities;

  /// Create a copy of CausalGene
  /// with the given fields replaced by the non-null parameter values.
  @override
  @JsonKey(includeFromJson: false, includeToJson: false)
  _$$CausalGeneImplCopyWith<_$CausalGeneImpl> get copyWith =>
      throw _privateConstructorUsedError;
}
