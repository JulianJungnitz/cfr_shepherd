// coverage:ignore-file
// GENERATED CODE - DO NOT MODIFY BY HAND
// ignore_for_file: type=lint
// ignore_for_file: unused_element, deprecated_member_use, deprecated_member_use_from_same_package, use_function_type_syntax_for_parameters, unnecessary_const, avoid_init_to_null, invalid_override_different_default_values_named, prefer_expression_function_bodies, annotate_overrides, invalid_annotation_target, unnecessary_question_mark

part of 'patient_like_me.dart';

// **************************************************************************
// FreezedGenerator
// **************************************************************************

T _$identity<T>(T value) => value;

final _privateConstructorUsedError = UnsupportedError(
    'It seems like you constructed your class using `MyClass._()`. This constructor is only meant to be used by freezed and you are not supposed to need it nor use it.\nPlease check the documentation here for more information: https://github.com/rrousselGit/freezed#adding-getters-and-methods-to-our-models');

PatientLikeMe _$PatientLikeMeFromJson(Map<String, dynamic> json) {
  return _PatientLikeMe.fromJson(json);
}

/// @nodoc
mixin _$PatientLikeMe {
  int? get patient_id => throw _privateConstructorUsedError;
  int? get candidate_patients => throw _privateConstructorUsedError;
  double? get similarities => throw _privateConstructorUsedError;

  /// Serializes this PatientLikeMe to a JSON map.
  Map<String, dynamic> toJson() => throw _privateConstructorUsedError;

  /// Create a copy of PatientLikeMe
  /// with the given fields replaced by the non-null parameter values.
  @JsonKey(includeFromJson: false, includeToJson: false)
  $PatientLikeMeCopyWith<PatientLikeMe> get copyWith =>
      throw _privateConstructorUsedError;
}

/// @nodoc
abstract class $PatientLikeMeCopyWith<$Res> {
  factory $PatientLikeMeCopyWith(
          PatientLikeMe value, $Res Function(PatientLikeMe) then) =
      _$PatientLikeMeCopyWithImpl<$Res, PatientLikeMe>;
  @useResult
  $Res call({int? patient_id, int? candidate_patients, double? similarities});
}

/// @nodoc
class _$PatientLikeMeCopyWithImpl<$Res, $Val extends PatientLikeMe>
    implements $PatientLikeMeCopyWith<$Res> {
  _$PatientLikeMeCopyWithImpl(this._value, this._then);

  // ignore: unused_field
  final $Val _value;
  // ignore: unused_field
  final $Res Function($Val) _then;

  /// Create a copy of PatientLikeMe
  /// with the given fields replaced by the non-null parameter values.
  @pragma('vm:prefer-inline')
  @override
  $Res call({
    Object? patient_id = freezed,
    Object? candidate_patients = freezed,
    Object? similarities = freezed,
  }) {
    return _then(_value.copyWith(
      patient_id: freezed == patient_id
          ? _value.patient_id
          : patient_id // ignore: cast_nullable_to_non_nullable
              as int?,
      candidate_patients: freezed == candidate_patients
          ? _value.candidate_patients
          : candidate_patients // ignore: cast_nullable_to_non_nullable
              as int?,
      similarities: freezed == similarities
          ? _value.similarities
          : similarities // ignore: cast_nullable_to_non_nullable
              as double?,
    ) as $Val);
  }
}

/// @nodoc
abstract class _$$PatientLikeMeImplCopyWith<$Res>
    implements $PatientLikeMeCopyWith<$Res> {
  factory _$$PatientLikeMeImplCopyWith(
          _$PatientLikeMeImpl value, $Res Function(_$PatientLikeMeImpl) then) =
      __$$PatientLikeMeImplCopyWithImpl<$Res>;
  @override
  @useResult
  $Res call({int? patient_id, int? candidate_patients, double? similarities});
}

/// @nodoc
class __$$PatientLikeMeImplCopyWithImpl<$Res>
    extends _$PatientLikeMeCopyWithImpl<$Res, _$PatientLikeMeImpl>
    implements _$$PatientLikeMeImplCopyWith<$Res> {
  __$$PatientLikeMeImplCopyWithImpl(
      _$PatientLikeMeImpl _value, $Res Function(_$PatientLikeMeImpl) _then)
      : super(_value, _then);

  /// Create a copy of PatientLikeMe
  /// with the given fields replaced by the non-null parameter values.
  @pragma('vm:prefer-inline')
  @override
  $Res call({
    Object? patient_id = freezed,
    Object? candidate_patients = freezed,
    Object? similarities = freezed,
  }) {
    return _then(_$PatientLikeMeImpl(
      patient_id: freezed == patient_id
          ? _value.patient_id
          : patient_id // ignore: cast_nullable_to_non_nullable
              as int?,
      candidate_patients: freezed == candidate_patients
          ? _value.candidate_patients
          : candidate_patients // ignore: cast_nullable_to_non_nullable
              as int?,
      similarities: freezed == similarities
          ? _value.similarities
          : similarities // ignore: cast_nullable_to_non_nullable
              as double?,
    ));
  }
}

/// @nodoc
@JsonSerializable()
class _$PatientLikeMeImpl implements _PatientLikeMe {
  const _$PatientLikeMeImpl(
      {this.patient_id, this.candidate_patients, this.similarities});

  factory _$PatientLikeMeImpl.fromJson(Map<String, dynamic> json) =>
      _$$PatientLikeMeImplFromJson(json);

  @override
  final int? patient_id;
  @override
  final int? candidate_patients;
  @override
  final double? similarities;

  @override
  String toString() {
    return 'PatientLikeMe(patient_id: $patient_id, candidate_patients: $candidate_patients, similarities: $similarities)';
  }

  @override
  bool operator ==(Object other) {
    return identical(this, other) ||
        (other.runtimeType == runtimeType &&
            other is _$PatientLikeMeImpl &&
            (identical(other.patient_id, patient_id) ||
                other.patient_id == patient_id) &&
            (identical(other.candidate_patients, candidate_patients) ||
                other.candidate_patients == candidate_patients) &&
            (identical(other.similarities, similarities) ||
                other.similarities == similarities));
  }

  @JsonKey(includeFromJson: false, includeToJson: false)
  @override
  int get hashCode =>
      Object.hash(runtimeType, patient_id, candidate_patients, similarities);

  /// Create a copy of PatientLikeMe
  /// with the given fields replaced by the non-null parameter values.
  @JsonKey(includeFromJson: false, includeToJson: false)
  @override
  @pragma('vm:prefer-inline')
  _$$PatientLikeMeImplCopyWith<_$PatientLikeMeImpl> get copyWith =>
      __$$PatientLikeMeImplCopyWithImpl<_$PatientLikeMeImpl>(this, _$identity);

  @override
  Map<String, dynamic> toJson() {
    return _$$PatientLikeMeImplToJson(
      this,
    );
  }
}

abstract class _PatientLikeMe implements PatientLikeMe {
  const factory _PatientLikeMe(
      {final int? patient_id,
      final int? candidate_patients,
      final double? similarities}) = _$PatientLikeMeImpl;

  factory _PatientLikeMe.fromJson(Map<String, dynamic> json) =
      _$PatientLikeMeImpl.fromJson;

  @override
  int? get patient_id;
  @override
  int? get candidate_patients;
  @override
  double? get similarities;

  /// Create a copy of PatientLikeMe
  /// with the given fields replaced by the non-null parameter values.
  @override
  @JsonKey(includeFromJson: false, includeToJson: false)
  _$$PatientLikeMeImplCopyWith<_$PatientLikeMeImpl> get copyWith =>
      throw _privateConstructorUsedError;
}
