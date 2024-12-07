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
  String? get biologicalSample => throw _privateConstructorUsedError;
  @JsonKey(name: 'genes')
  String? get genes => throw _privateConstructorUsedError;
  @JsonKey(name: 'phenotypes')
  String? get phenotypes => throw _privateConstructorUsedError;
  @JsonKey(name: 'subject_id')
  int? get subjectId => throw _privateConstructorUsedError;

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
      {@JsonKey(name: 'biological_sample') String? biologicalSample,
      @JsonKey(name: 'genes') String? genes,
      @JsonKey(name: 'phenotypes') String? phenotypes,
      @JsonKey(name: 'subject_id') int? subjectId});
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
    Object? subjectId = freezed,
  }) {
    return _then(_value.copyWith(
      biologicalSample: freezed == biologicalSample
          ? _value.biologicalSample
          : biologicalSample // ignore: cast_nullable_to_non_nullable
              as String?,
      genes: freezed == genes
          ? _value.genes
          : genes // ignore: cast_nullable_to_non_nullable
              as String?,
      phenotypes: freezed == phenotypes
          ? _value.phenotypes
          : phenotypes // ignore: cast_nullable_to_non_nullable
              as String?,
      subjectId: freezed == subjectId
          ? _value.subjectId
          : subjectId // ignore: cast_nullable_to_non_nullable
              as int?,
    ) as $Val);
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
      {@JsonKey(name: 'biological_sample') String? biologicalSample,
      @JsonKey(name: 'genes') String? genes,
      @JsonKey(name: 'phenotypes') String? phenotypes,
      @JsonKey(name: 'subject_id') int? subjectId});
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
    Object? subjectId = freezed,
  }) {
    return _then(_$PatientImpl(
      biologicalSample: freezed == biologicalSample
          ? _value.biologicalSample
          : biologicalSample // ignore: cast_nullable_to_non_nullable
              as String?,
      genes: freezed == genes
          ? _value.genes
          : genes // ignore: cast_nullable_to_non_nullable
              as String?,
      phenotypes: freezed == phenotypes
          ? _value.phenotypes
          : phenotypes // ignore: cast_nullable_to_non_nullable
              as String?,
      subjectId: freezed == subjectId
          ? _value.subjectId
          : subjectId // ignore: cast_nullable_to_non_nullable
              as int?,
    ));
  }
}

/// @nodoc
@JsonSerializable()
class _$PatientImpl implements _Patient {
  const _$PatientImpl(
      {@JsonKey(name: 'biological_sample') this.biologicalSample,
      @JsonKey(name: 'genes') this.genes,
      @JsonKey(name: 'phenotypes') this.phenotypes,
      @JsonKey(name: 'subject_id') this.subjectId});

  factory _$PatientImpl.fromJson(Map<String, dynamic> json) =>
      _$$PatientImplFromJson(json);

  @override
  @JsonKey(name: 'biological_sample')
  final String? biologicalSample;
  @override
  @JsonKey(name: 'genes')
  final String? genes;
  @override
  @JsonKey(name: 'phenotypes')
  final String? phenotypes;
  @override
  @JsonKey(name: 'subject_id')
  final int? subjectId;

  @override
  String toString() {
    return 'Patient(biologicalSample: $biologicalSample, genes: $genes, phenotypes: $phenotypes, subjectId: $subjectId)';
  }

  @override
  bool operator ==(Object other) {
    return identical(this, other) ||
        (other.runtimeType == runtimeType &&
            other is _$PatientImpl &&
            (identical(other.biologicalSample, biologicalSample) ||
                other.biologicalSample == biologicalSample) &&
            (identical(other.genes, genes) || other.genes == genes) &&
            (identical(other.phenotypes, phenotypes) ||
                other.phenotypes == phenotypes) &&
            (identical(other.subjectId, subjectId) ||
                other.subjectId == subjectId));
  }

  @JsonKey(includeFromJson: false, includeToJson: false)
  @override
  int get hashCode =>
      Object.hash(runtimeType, biologicalSample, genes, phenotypes, subjectId);

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
      {@JsonKey(name: 'biological_sample') final String? biologicalSample,
      @JsonKey(name: 'genes') final String? genes,
      @JsonKey(name: 'phenotypes') final String? phenotypes,
      @JsonKey(name: 'subject_id') final int? subjectId}) = _$PatientImpl;

  factory _Patient.fromJson(Map<String, dynamic> json) = _$PatientImpl.fromJson;

  @override
  @JsonKey(name: 'biological_sample')
  String? get biologicalSample;
  @override
  @JsonKey(name: 'genes')
  String? get genes;
  @override
  @JsonKey(name: 'phenotypes')
  String? get phenotypes;
  @override
  @JsonKey(name: 'subject_id')
  int? get subjectId;

  /// Create a copy of Patient
  /// with the given fields replaced by the non-null parameter values.
  @override
  @JsonKey(includeFromJson: false, includeToJson: false)
  _$$PatientImplCopyWith<_$PatientImpl> get copyWith =>
      throw _privateConstructorUsedError;
}
