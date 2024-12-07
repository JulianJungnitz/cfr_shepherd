// coverage:ignore-file
// GENERATED CODE - DO NOT MODIFY BY HAND
// ignore_for_file: type=lint
// ignore_for_file: unused_element, deprecated_member_use, deprecated_member_use_from_same_package, use_function_type_syntax_for_parameters, unnecessary_const, avoid_init_to_null, invalid_override_different_default_values_named, prefer_expression_function_bodies, annotate_overrides, invalid_annotation_target, unnecessary_question_mark

part of 'biological_sample.dart';

// **************************************************************************
// FreezedGenerator
// **************************************************************************

T _$identity<T>(T value) => value;

final _privateConstructorUsedError = UnsupportedError(
    'It seems like you constructed your class using `MyClass._()`. This constructor is only meant to be used by freezed and you are not supposed to need it nor use it.\nPlease check the documentation here for more information: https://github.com/rrousselGit/freezed#adding-getters-and-methods-to-our-models');

BiologicalSample _$BiologicalSampleFromJson(Map<String, dynamic> json) {
  return _BiologicalSample.fromJson(json);
}

/// @nodoc
mixin _$BiologicalSample {
  @JsonKey(name: 'external_id')
  String? get externalId => throw _privateConstructorUsedError;
  @JsonKey(name: 'subjectid')
  int? get subjectid => throw _privateConstructorUsedError;

  /// Serializes this BiologicalSample to a JSON map.
  Map<String, dynamic> toJson() => throw _privateConstructorUsedError;

  /// Create a copy of BiologicalSample
  /// with the given fields replaced by the non-null parameter values.
  @JsonKey(includeFromJson: false, includeToJson: false)
  $BiologicalSampleCopyWith<BiologicalSample> get copyWith =>
      throw _privateConstructorUsedError;
}

/// @nodoc
abstract class $BiologicalSampleCopyWith<$Res> {
  factory $BiologicalSampleCopyWith(
          BiologicalSample value, $Res Function(BiologicalSample) then) =
      _$BiologicalSampleCopyWithImpl<$Res, BiologicalSample>;
  @useResult
  $Res call(
      {@JsonKey(name: 'external_id') String? externalId,
      @JsonKey(name: 'subjectid') int? subjectid});
}

/// @nodoc
class _$BiologicalSampleCopyWithImpl<$Res, $Val extends BiologicalSample>
    implements $BiologicalSampleCopyWith<$Res> {
  _$BiologicalSampleCopyWithImpl(this._value, this._then);

  // ignore: unused_field
  final $Val _value;
  // ignore: unused_field
  final $Res Function($Val) _then;

  /// Create a copy of BiologicalSample
  /// with the given fields replaced by the non-null parameter values.
  @pragma('vm:prefer-inline')
  @override
  $Res call({
    Object? externalId = freezed,
    Object? subjectid = freezed,
  }) {
    return _then(_value.copyWith(
      externalId: freezed == externalId
          ? _value.externalId
          : externalId // ignore: cast_nullable_to_non_nullable
              as String?,
      subjectid: freezed == subjectid
          ? _value.subjectid
          : subjectid // ignore: cast_nullable_to_non_nullable
              as int?,
    ) as $Val);
  }
}

/// @nodoc
abstract class _$$BiologicalSampleImplCopyWith<$Res>
    implements $BiologicalSampleCopyWith<$Res> {
  factory _$$BiologicalSampleImplCopyWith(_$BiologicalSampleImpl value,
          $Res Function(_$BiologicalSampleImpl) then) =
      __$$BiologicalSampleImplCopyWithImpl<$Res>;
  @override
  @useResult
  $Res call(
      {@JsonKey(name: 'external_id') String? externalId,
      @JsonKey(name: 'subjectid') int? subjectid});
}

/// @nodoc
class __$$BiologicalSampleImplCopyWithImpl<$Res>
    extends _$BiologicalSampleCopyWithImpl<$Res, _$BiologicalSampleImpl>
    implements _$$BiologicalSampleImplCopyWith<$Res> {
  __$$BiologicalSampleImplCopyWithImpl(_$BiologicalSampleImpl _value,
      $Res Function(_$BiologicalSampleImpl) _then)
      : super(_value, _then);

  /// Create a copy of BiologicalSample
  /// with the given fields replaced by the non-null parameter values.
  @pragma('vm:prefer-inline')
  @override
  $Res call({
    Object? externalId = freezed,
    Object? subjectid = freezed,
  }) {
    return _then(_$BiologicalSampleImpl(
      externalId: freezed == externalId
          ? _value.externalId
          : externalId // ignore: cast_nullable_to_non_nullable
              as String?,
      subjectid: freezed == subjectid
          ? _value.subjectid
          : subjectid // ignore: cast_nullable_to_non_nullable
              as int?,
    ));
  }
}

/// @nodoc
@JsonSerializable()
class _$BiologicalSampleImpl implements _BiologicalSample {
  const _$BiologicalSampleImpl(
      {@JsonKey(name: 'external_id') this.externalId,
      @JsonKey(name: 'subjectid') this.subjectid});

  factory _$BiologicalSampleImpl.fromJson(Map<String, dynamic> json) =>
      _$$BiologicalSampleImplFromJson(json);

  @override
  @JsonKey(name: 'external_id')
  final String? externalId;
  @override
  @JsonKey(name: 'subjectid')
  final int? subjectid;

  @override
  String toString() {
    return 'BiologicalSample(externalId: $externalId, subjectid: $subjectid)';
  }

  @override
  bool operator ==(Object other) {
    return identical(this, other) ||
        (other.runtimeType == runtimeType &&
            other is _$BiologicalSampleImpl &&
            (identical(other.externalId, externalId) ||
                other.externalId == externalId) &&
            (identical(other.subjectid, subjectid) ||
                other.subjectid == subjectid));
  }

  @JsonKey(includeFromJson: false, includeToJson: false)
  @override
  int get hashCode => Object.hash(runtimeType, externalId, subjectid);

  /// Create a copy of BiologicalSample
  /// with the given fields replaced by the non-null parameter values.
  @JsonKey(includeFromJson: false, includeToJson: false)
  @override
  @pragma('vm:prefer-inline')
  _$$BiologicalSampleImplCopyWith<_$BiologicalSampleImpl> get copyWith =>
      __$$BiologicalSampleImplCopyWithImpl<_$BiologicalSampleImpl>(
          this, _$identity);

  @override
  Map<String, dynamic> toJson() {
    return _$$BiologicalSampleImplToJson(
      this,
    );
  }
}

abstract class _BiologicalSample implements BiologicalSample {
  const factory _BiologicalSample(
          {@JsonKey(name: 'external_id') final String? externalId,
          @JsonKey(name: 'subjectid') final int? subjectid}) =
      _$BiologicalSampleImpl;

  factory _BiologicalSample.fromJson(Map<String, dynamic> json) =
      _$BiologicalSampleImpl.fromJson;

  @override
  @JsonKey(name: 'external_id')
  String? get externalId;
  @override
  @JsonKey(name: 'subjectid')
  int? get subjectid;

  /// Create a copy of BiologicalSample
  /// with the given fields replaced by the non-null parameter values.
  @override
  @JsonKey(includeFromJson: false, includeToJson: false)
  _$$BiologicalSampleImplCopyWith<_$BiologicalSampleImpl> get copyWith =>
      throw _privateConstructorUsedError;
}
