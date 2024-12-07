// coverage:ignore-file
// GENERATED CODE - DO NOT MODIFY BY HAND
// ignore_for_file: type=lint
// ignore_for_file: unused_element, deprecated_member_use, deprecated_member_use_from_same_package, use_function_type_syntax_for_parameters, unnecessary_const, avoid_init_to_null, invalid_override_different_default_values_named, prefer_expression_function_bodies, annotate_overrides, invalid_annotation_target, unnecessary_question_mark

part of 'disease_characterization.dart';

// **************************************************************************
// FreezedGenerator
// **************************************************************************

T _$identity<T>(T value) => value;

final _privateConstructorUsedError = UnsupportedError(
    'It seems like you constructed your class using `MyClass._()`. This constructor is only meant to be used by freezed and you are not supposed to need it nor use it.\nPlease check the documentation here for more information: https://github.com/rrousselGit/freezed#adding-getters-and-methods-to-our-models');

DiseaseCharacterization _$DiseaseCharacterizationFromJson(
    Map<String, dynamic> json) {
  return _DiseaseCharacterization.fromJson(json);
}

/// @nodoc
mixin _$DiseaseCharacterization {
  @JsonKey(name: 'patient_id')
  int? get patientId => throw _privateConstructorUsedError;
  @JsonKey(name: 'diseases')
  String? get diseases => throw _privateConstructorUsedError;
  @JsonKey(name: 'similarities')
  double? get similarities => throw _privateConstructorUsedError;

  /// Serializes this DiseaseCharacterization to a JSON map.
  Map<String, dynamic> toJson() => throw _privateConstructorUsedError;

  /// Create a copy of DiseaseCharacterization
  /// with the given fields replaced by the non-null parameter values.
  @JsonKey(includeFromJson: false, includeToJson: false)
  $DiseaseCharacterizationCopyWith<DiseaseCharacterization> get copyWith =>
      throw _privateConstructorUsedError;
}

/// @nodoc
abstract class $DiseaseCharacterizationCopyWith<$Res> {
  factory $DiseaseCharacterizationCopyWith(DiseaseCharacterization value,
          $Res Function(DiseaseCharacterization) then) =
      _$DiseaseCharacterizationCopyWithImpl<$Res, DiseaseCharacterization>;
  @useResult
  $Res call(
      {@JsonKey(name: 'patient_id') int? patientId,
      @JsonKey(name: 'diseases') String? diseases,
      @JsonKey(name: 'similarities') double? similarities});
}

/// @nodoc
class _$DiseaseCharacterizationCopyWithImpl<$Res,
        $Val extends DiseaseCharacterization>
    implements $DiseaseCharacterizationCopyWith<$Res> {
  _$DiseaseCharacterizationCopyWithImpl(this._value, this._then);

  // ignore: unused_field
  final $Val _value;
  // ignore: unused_field
  final $Res Function($Val) _then;

  /// Create a copy of DiseaseCharacterization
  /// with the given fields replaced by the non-null parameter values.
  @pragma('vm:prefer-inline')
  @override
  $Res call({
    Object? patientId = freezed,
    Object? diseases = freezed,
    Object? similarities = freezed,
  }) {
    return _then(_value.copyWith(
      patientId: freezed == patientId
          ? _value.patientId
          : patientId // ignore: cast_nullable_to_non_nullable
              as int?,
      diseases: freezed == diseases
          ? _value.diseases
          : diseases // ignore: cast_nullable_to_non_nullable
              as String?,
      similarities: freezed == similarities
          ? _value.similarities
          : similarities // ignore: cast_nullable_to_non_nullable
              as double?,
    ) as $Val);
  }
}

/// @nodoc
abstract class _$$DiseaseCharacterizationImplCopyWith<$Res>
    implements $DiseaseCharacterizationCopyWith<$Res> {
  factory _$$DiseaseCharacterizationImplCopyWith(
          _$DiseaseCharacterizationImpl value,
          $Res Function(_$DiseaseCharacterizationImpl) then) =
      __$$DiseaseCharacterizationImplCopyWithImpl<$Res>;
  @override
  @useResult
  $Res call(
      {@JsonKey(name: 'patient_id') int? patientId,
      @JsonKey(name: 'diseases') String? diseases,
      @JsonKey(name: 'similarities') double? similarities});
}

/// @nodoc
class __$$DiseaseCharacterizationImplCopyWithImpl<$Res>
    extends _$DiseaseCharacterizationCopyWithImpl<$Res,
        _$DiseaseCharacterizationImpl>
    implements _$$DiseaseCharacterizationImplCopyWith<$Res> {
  __$$DiseaseCharacterizationImplCopyWithImpl(
      _$DiseaseCharacterizationImpl _value,
      $Res Function(_$DiseaseCharacterizationImpl) _then)
      : super(_value, _then);

  /// Create a copy of DiseaseCharacterization
  /// with the given fields replaced by the non-null parameter values.
  @pragma('vm:prefer-inline')
  @override
  $Res call({
    Object? patientId = freezed,
    Object? diseases = freezed,
    Object? similarities = freezed,
  }) {
    return _then(_$DiseaseCharacterizationImpl(
      patientId: freezed == patientId
          ? _value.patientId
          : patientId // ignore: cast_nullable_to_non_nullable
              as int?,
      diseases: freezed == diseases
          ? _value.diseases
          : diseases // ignore: cast_nullable_to_non_nullable
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
class _$DiseaseCharacterizationImpl implements _DiseaseCharacterization {
  const _$DiseaseCharacterizationImpl(
      {@JsonKey(name: 'patient_id') this.patientId,
      @JsonKey(name: 'diseases') this.diseases,
      @JsonKey(name: 'similarities') this.similarities});

  factory _$DiseaseCharacterizationImpl.fromJson(Map<String, dynamic> json) =>
      _$$DiseaseCharacterizationImplFromJson(json);

  @override
  @JsonKey(name: 'patient_id')
  final int? patientId;
  @override
  @JsonKey(name: 'diseases')
  final String? diseases;
  @override
  @JsonKey(name: 'similarities')
  final double? similarities;

  @override
  String toString() {
    return 'DiseaseCharacterization(patientId: $patientId, diseases: $diseases, similarities: $similarities)';
  }

  @override
  bool operator ==(Object other) {
    return identical(this, other) ||
        (other.runtimeType == runtimeType &&
            other is _$DiseaseCharacterizationImpl &&
            (identical(other.patientId, patientId) ||
                other.patientId == patientId) &&
            (identical(other.diseases, diseases) ||
                other.diseases == diseases) &&
            (identical(other.similarities, similarities) ||
                other.similarities == similarities));
  }

  @JsonKey(includeFromJson: false, includeToJson: false)
  @override
  int get hashCode =>
      Object.hash(runtimeType, patientId, diseases, similarities);

  /// Create a copy of DiseaseCharacterization
  /// with the given fields replaced by the non-null parameter values.
  @JsonKey(includeFromJson: false, includeToJson: false)
  @override
  @pragma('vm:prefer-inline')
  _$$DiseaseCharacterizationImplCopyWith<_$DiseaseCharacterizationImpl>
      get copyWith => __$$DiseaseCharacterizationImplCopyWithImpl<
          _$DiseaseCharacterizationImpl>(this, _$identity);

  @override
  Map<String, dynamic> toJson() {
    return _$$DiseaseCharacterizationImplToJson(
      this,
    );
  }
}

abstract class _DiseaseCharacterization implements DiseaseCharacterization {
  const factory _DiseaseCharacterization(
          {@JsonKey(name: 'patient_id') final int? patientId,
          @JsonKey(name: 'diseases') final String? diseases,
          @JsonKey(name: 'similarities') final double? similarities}) =
      _$DiseaseCharacterizationImpl;

  factory _DiseaseCharacterization.fromJson(Map<String, dynamic> json) =
      _$DiseaseCharacterizationImpl.fromJson;

  @override
  @JsonKey(name: 'patient_id')
  int? get patientId;
  @override
  @JsonKey(name: 'diseases')
  String? get diseases;
  @override
  @JsonKey(name: 'similarities')
  double? get similarities;

  /// Create a copy of DiseaseCharacterization
  /// with the given fields replaced by the non-null parameter values.
  @override
  @JsonKey(includeFromJson: false, includeToJson: false)
  _$$DiseaseCharacterizationImplCopyWith<_$DiseaseCharacterizationImpl>
      get copyWith => throw _privateConstructorUsedError;
}
