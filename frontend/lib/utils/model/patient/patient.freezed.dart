// coverage:ignore-file
// GENERATED CODE - DO NOT MODIFY BY HAND
// ignore_for_file: type=lint
// ignore_for_file: unused_element, deprecated_member_use, deprecated_member_use_from_same_package, use_function_type_syntax_for_parameters, unnecessary_const, avoid_init_to_null, invalid_override_different_default_values_named, prefer_expression_function_bodies, annotate_overrides, invalid_annotation_target, unnecessary_question_mark

part of 'patient.dart';

// **************************************************************************
// FreezedGenerator
// **************************************************************************

T _$identity<T>(T value) => value;

final _privateConstructorUsedError = UnsupportedError(
    'It seems like you constructed your class using `MyClass._()`. This constructor is only meant to be used by freezed and you are not supposed to need it nor use it.\nPlease check the documentation here for more information: https://github.com/rrousselGit/freezed#adding-getters-and-methods-to-our-models');

Patient _$PatientFromJson(Map<String, dynamic> json) {
  return _Patient.fromJson(json);
}

/// @nodoc
mixin _$Patient {
  @JsonKey(name: 'biological_sample')
  BiologicalSample? get biologicalSample => throw _privateConstructorUsedError;
  @JsonKey(name: 'genes')
  List<Gene>? get genes => throw _privateConstructorUsedError;
  @JsonKey(name: 'phenotypes')
  List<Phenotype>? get phenotypes => throw _privateConstructorUsedError;
  @JsonKey(name: 'diseases')
  List<Disease>? get diseases => throw _privateConstructorUsedError;
  @JsonKey(name: 'sample_id')
  int? get sampleId => throw _privateConstructorUsedError;

  /// Serializes this Patient to a JSON map.
  Map<String, dynamic> toJson() => throw _privateConstructorUsedError;

  /// Create a copy of Patient
  /// with the given fields replaced by the non-null parameter values.
  @JsonKey(includeFromJson: false, includeToJson: false)
  $PatientCopyWith<Patient> get copyWith => throw _privateConstructorUsedError;
}

/// @nodoc
abstract class $PatientCopyWith<$Res> {
  factory $PatientCopyWith(Patient value, $Res Function(Patient) then) =
      _$PatientCopyWithImpl<$Res, Patient>;
  @useResult
  $Res call(
      {@JsonKey(name: 'biological_sample') BiologicalSample? biologicalSample,
      @JsonKey(name: 'genes') List<Gene>? genes,
      @JsonKey(name: 'phenotypes') List<Phenotype>? phenotypes,
      @JsonKey(name: 'diseases') List<Disease>? diseases,
      @JsonKey(name: 'sample_id') int? sampleId});

  $BiologicalSampleCopyWith<$Res>? get biologicalSample;
}

/// @nodoc
class _$PatientCopyWithImpl<$Res, $Val extends Patient>
    implements $PatientCopyWith<$Res> {
  _$PatientCopyWithImpl(this._value, this._then);

  // ignore: unused_field
  final $Val _value;
  // ignore: unused_field
  final $Res Function($Val) _then;

  /// Create a copy of Patient
  /// with the given fields replaced by the non-null parameter values.
  @pragma('vm:prefer-inline')
  @override
  $Res call({
    Object? biologicalSample = freezed,
    Object? genes = freezed,
    Object? phenotypes = freezed,
    Object? diseases = freezed,
    Object? sampleId = freezed,
  }) {
    return _then(_value.copyWith(
      biologicalSample: freezed == biologicalSample
          ? _value.biologicalSample
          : biologicalSample // ignore: cast_nullable_to_non_nullable
              as BiologicalSample?,
      genes: freezed == genes
          ? _value.genes
          : genes // ignore: cast_nullable_to_non_nullable
              as List<Gene>?,
      phenotypes: freezed == phenotypes
          ? _value.phenotypes
          : phenotypes // ignore: cast_nullable_to_non_nullable
              as List<Phenotype>?,
      diseases: freezed == diseases
          ? _value.diseases
          : diseases // ignore: cast_nullable_to_non_nullable
              as List<Disease>?,
      sampleId: freezed == sampleId
          ? _value.sampleId
          : sampleId // ignore: cast_nullable_to_non_nullable
              as int?,
    ) as $Val);
  }

  /// Create a copy of Patient
  /// with the given fields replaced by the non-null parameter values.
  @override
  @pragma('vm:prefer-inline')
  $BiologicalSampleCopyWith<$Res>? get biologicalSample {
    if (_value.biologicalSample == null) {
      return null;
    }

    return $BiologicalSampleCopyWith<$Res>(_value.biologicalSample!, (value) {
      return _then(_value.copyWith(biologicalSample: value) as $Val);
    });
  }
}

/// @nodoc
abstract class _$$PatientImplCopyWith<$Res> implements $PatientCopyWith<$Res> {
  factory _$$PatientImplCopyWith(
          _$PatientImpl value, $Res Function(_$PatientImpl) then) =
      __$$PatientImplCopyWithImpl<$Res>;
  @override
  @useResult
  $Res call(
      {@JsonKey(name: 'biological_sample') BiologicalSample? biologicalSample,
      @JsonKey(name: 'genes') List<Gene>? genes,
      @JsonKey(name: 'phenotypes') List<Phenotype>? phenotypes,
      @JsonKey(name: 'diseases') List<Disease>? diseases,
      @JsonKey(name: 'sample_id') int? sampleId});

  @override
  $BiologicalSampleCopyWith<$Res>? get biologicalSample;
}

/// @nodoc
class __$$PatientImplCopyWithImpl<$Res>
    extends _$PatientCopyWithImpl<$Res, _$PatientImpl>
    implements _$$PatientImplCopyWith<$Res> {
  __$$PatientImplCopyWithImpl(
      _$PatientImpl _value, $Res Function(_$PatientImpl) _then)
      : super(_value, _then);

  /// Create a copy of Patient
  /// with the given fields replaced by the non-null parameter values.
  @pragma('vm:prefer-inline')
  @override
  $Res call({
    Object? biologicalSample = freezed,
    Object? genes = freezed,
    Object? phenotypes = freezed,
    Object? diseases = freezed,
    Object? sampleId = freezed,
  }) {
    return _then(_$PatientImpl(
      biologicalSample: freezed == biologicalSample
          ? _value.biologicalSample
          : biologicalSample // ignore: cast_nullable_to_non_nullable
              as BiologicalSample?,
      genes: freezed == genes
          ? _value._genes
          : genes // ignore: cast_nullable_to_non_nullable
              as List<Gene>?,
      phenotypes: freezed == phenotypes
          ? _value._phenotypes
          : phenotypes // ignore: cast_nullable_to_non_nullable
              as List<Phenotype>?,
      diseases: freezed == diseases
          ? _value._diseases
          : diseases // ignore: cast_nullable_to_non_nullable
              as List<Disease>?,
      sampleId: freezed == sampleId
          ? _value.sampleId
          : sampleId // ignore: cast_nullable_to_non_nullable
              as int?,
    ));
  }
}

/// @nodoc
@JsonSerializable()
class _$PatientImpl implements _Patient {
  const _$PatientImpl(
      {@JsonKey(name: 'biological_sample') this.biologicalSample,
      @JsonKey(name: 'genes') final List<Gene>? genes,
      @JsonKey(name: 'phenotypes') final List<Phenotype>? phenotypes,
      @JsonKey(name: 'diseases') final List<Disease>? diseases,
      @JsonKey(name: 'sample_id') this.sampleId})
      : _genes = genes,
        _phenotypes = phenotypes,
        _diseases = diseases;

  factory _$PatientImpl.fromJson(Map<String, dynamic> json) =>
      _$$PatientImplFromJson(json);

  @override
  @JsonKey(name: 'biological_sample')
  final BiologicalSample? biologicalSample;
  final List<Gene>? _genes;
  @override
  @JsonKey(name: 'genes')
  List<Gene>? get genes {
    final value = _genes;
    if (value == null) return null;
    if (_genes is EqualUnmodifiableListView) return _genes;
    // ignore: implicit_dynamic_type
    return EqualUnmodifiableListView(value);
  }

  final List<Phenotype>? _phenotypes;
  @override
  @JsonKey(name: 'phenotypes')
  List<Phenotype>? get phenotypes {
    final value = _phenotypes;
    if (value == null) return null;
    if (_phenotypes is EqualUnmodifiableListView) return _phenotypes;
    // ignore: implicit_dynamic_type
    return EqualUnmodifiableListView(value);
  }

  final List<Disease>? _diseases;
  @override
  @JsonKey(name: 'diseases')
  List<Disease>? get diseases {
    final value = _diseases;
    if (value == null) return null;
    if (_diseases is EqualUnmodifiableListView) return _diseases;
    // ignore: implicit_dynamic_type
    return EqualUnmodifiableListView(value);
  }

  @override
  @JsonKey(name: 'sample_id')
  final int? sampleId;

  @override
  String toString() {
    return 'Patient(biologicalSample: $biologicalSample, genes: $genes, phenotypes: $phenotypes, diseases: $diseases, sampleId: $sampleId)';
  }

  @override
  bool operator ==(Object other) {
    return identical(this, other) ||
        (other.runtimeType == runtimeType &&
            other is _$PatientImpl &&
            (identical(other.biologicalSample, biologicalSample) ||
                other.biologicalSample == biologicalSample) &&
            const DeepCollectionEquality().equals(other._genes, _genes) &&
            const DeepCollectionEquality()
                .equals(other._phenotypes, _phenotypes) &&
            const DeepCollectionEquality().equals(other._diseases, _diseases) &&
            (identical(other.sampleId, sampleId) ||
                other.sampleId == sampleId));
  }

  @JsonKey(includeFromJson: false, includeToJson: false)
  @override
  int get hashCode => Object.hash(
      runtimeType,
      biologicalSample,
      const DeepCollectionEquality().hash(_genes),
      const DeepCollectionEquality().hash(_phenotypes),
      const DeepCollectionEquality().hash(_diseases),
      sampleId);

  /// Create a copy of Patient
  /// with the given fields replaced by the non-null parameter values.
  @JsonKey(includeFromJson: false, includeToJson: false)
  @override
  @pragma('vm:prefer-inline')
  _$$PatientImplCopyWith<_$PatientImpl> get copyWith =>
      __$$PatientImplCopyWithImpl<_$PatientImpl>(this, _$identity);

  @override
  Map<String, dynamic> toJson() {
    return _$$PatientImplToJson(
      this,
    );
  }
}

abstract class _Patient implements Patient {
  const factory _Patient(
      {@JsonKey(name: 'biological_sample')
      final BiologicalSample? biologicalSample,
      @JsonKey(name: 'genes') final List<Gene>? genes,
      @JsonKey(name: 'phenotypes') final List<Phenotype>? phenotypes,
      @JsonKey(name: 'diseases') final List<Disease>? diseases,
      @JsonKey(name: 'sample_id') final int? sampleId}) = _$PatientImpl;

  factory _Patient.fromJson(Map<String, dynamic> json) = _$PatientImpl.fromJson;

  @override
  @JsonKey(name: 'biological_sample')
  BiologicalSample? get biologicalSample;
  @override
  @JsonKey(name: 'genes')
  List<Gene>? get genes;
  @override
  @JsonKey(name: 'phenotypes')
  List<Phenotype>? get phenotypes;
  @override
  @JsonKey(name: 'diseases')
  List<Disease>? get diseases;
  @override
  @JsonKey(name: 'sample_id')
  int? get sampleId;

  /// Create a copy of Patient
  /// with the given fields replaced by the non-null parameter values.
  @override
  @JsonKey(includeFromJson: false, includeToJson: false)
  _$$PatientImplCopyWith<_$PatientImpl> get copyWith =>
      throw _privateConstructorUsedError;
}
