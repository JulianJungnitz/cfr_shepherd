// coverage:ignore-file
// GENERATED CODE - DO NOT MODIFY BY HAND
// ignore_for_file: type=lint
// ignore_for_file: unused_element, deprecated_member_use, deprecated_member_use_from_same_package, use_function_type_syntax_for_parameters, unnecessary_const, avoid_init_to_null, invalid_override_different_default_values_named, prefer_expression_function_bodies, annotate_overrides, invalid_annotation_target, unnecessary_question_mark

part of 'attention.dart';

// **************************************************************************
// FreezedGenerator
// **************************************************************************

T _$identity<T>(T value) => value;

final _privateConstructorUsedError = UnsupportedError(
    'It seems like you constructed your class using `MyClass._()`. This constructor is only meant to be used by freezed and you are not supposed to need it nor use it.\nPlease check the documentation here for more information: https://github.com/rrousselGit/freezed#adding-getters-and-methods-to-our-models');

Attention _$AttentionFromJson(Map<String, dynamic> json) {
  return _Attention.fromJson(json);
}

/// @nodoc
mixin _$Attention {
  @JsonKey(name: 'patient_id')
  int? get patientId => throw _privateConstructorUsedError;
  @JsonKey(name: 'phenotypes')
  String? get phenotypes => throw _privateConstructorUsedError;
  @JsonKey(name: 'attention')
  double? get attention => throw _privateConstructorUsedError;

  /// Serializes this Attention to a JSON map.
  Map<String, dynamic> toJson() => throw _privateConstructorUsedError;

  /// Create a copy of Attention
  /// with the given fields replaced by the non-null parameter values.
  @JsonKey(includeFromJson: false, includeToJson: false)
  $AttentionCopyWith<Attention> get copyWith =>
      throw _privateConstructorUsedError;
}

/// @nodoc
abstract class $AttentionCopyWith<$Res> {
  factory $AttentionCopyWith(Attention value, $Res Function(Attention) then) =
      _$AttentionCopyWithImpl<$Res, Attention>;
  @useResult
  $Res call(
      {@JsonKey(name: 'patient_id') int? patientId,
      @JsonKey(name: 'phenotypes') String? phenotypes,
      @JsonKey(name: 'attention') double? attention});
}

/// @nodoc
class _$AttentionCopyWithImpl<$Res, $Val extends Attention>
    implements $AttentionCopyWith<$Res> {
  _$AttentionCopyWithImpl(this._value, this._then);

  // ignore: unused_field
  final $Val _value;
  // ignore: unused_field
  final $Res Function($Val) _then;

  /// Create a copy of Attention
  /// with the given fields replaced by the non-null parameter values.
  @pragma('vm:prefer-inline')
  @override
  $Res call({
    Object? patientId = freezed,
    Object? phenotypes = freezed,
    Object? attention = freezed,
  }) {
    return _then(_value.copyWith(
      patientId: freezed == patientId
          ? _value.patientId
          : patientId // ignore: cast_nullable_to_non_nullable
              as int?,
      phenotypes: freezed == phenotypes
          ? _value.phenotypes
          : phenotypes // ignore: cast_nullable_to_non_nullable
              as String?,
      attention: freezed == attention
          ? _value.attention
          : attention // ignore: cast_nullable_to_non_nullable
              as double?,
    ) as $Val);
  }
}

/// @nodoc
abstract class _$$AttentionImplCopyWith<$Res>
    implements $AttentionCopyWith<$Res> {
  factory _$$AttentionImplCopyWith(
          _$AttentionImpl value, $Res Function(_$AttentionImpl) then) =
      __$$AttentionImplCopyWithImpl<$Res>;
  @override
  @useResult
  $Res call(
      {@JsonKey(name: 'patient_id') int? patientId,
      @JsonKey(name: 'phenotypes') String? phenotypes,
      @JsonKey(name: 'attention') double? attention});
}

/// @nodoc
class __$$AttentionImplCopyWithImpl<$Res>
    extends _$AttentionCopyWithImpl<$Res, _$AttentionImpl>
    implements _$$AttentionImplCopyWith<$Res> {
  __$$AttentionImplCopyWithImpl(
      _$AttentionImpl _value, $Res Function(_$AttentionImpl) _then)
      : super(_value, _then);

  /// Create a copy of Attention
  /// with the given fields replaced by the non-null parameter values.
  @pragma('vm:prefer-inline')
  @override
  $Res call({
    Object? patientId = freezed,
    Object? phenotypes = freezed,
    Object? attention = freezed,
  }) {
    return _then(_$AttentionImpl(
      patientId: freezed == patientId
          ? _value.patientId
          : patientId // ignore: cast_nullable_to_non_nullable
              as int?,
      phenotypes: freezed == phenotypes
          ? _value.phenotypes
          : phenotypes // ignore: cast_nullable_to_non_nullable
              as String?,
      attention: freezed == attention
          ? _value.attention
          : attention // ignore: cast_nullable_to_non_nullable
              as double?,
    ));
  }
}

/// @nodoc
@JsonSerializable()
class _$AttentionImpl implements _Attention {
  const _$AttentionImpl(
      {@JsonKey(name: 'patient_id') this.patientId,
      @JsonKey(name: 'phenotypes') this.phenotypes,
      @JsonKey(name: 'attention') this.attention});

  factory _$AttentionImpl.fromJson(Map<String, dynamic> json) =>
      _$$AttentionImplFromJson(json);

  @override
  @JsonKey(name: 'patient_id')
  final int? patientId;
  @override
  @JsonKey(name: 'phenotypes')
  final String? phenotypes;
  @override
  @JsonKey(name: 'attention')
  final double? attention;

  @override
  String toString() {
    return 'Attention(patientId: $patientId, phenotypes: $phenotypes, attention: $attention)';
  }

  @override
  bool operator ==(Object other) {
    return identical(this, other) ||
        (other.runtimeType == runtimeType &&
            other is _$AttentionImpl &&
            (identical(other.patientId, patientId) ||
                other.patientId == patientId) &&
            (identical(other.phenotypes, phenotypes) ||
                other.phenotypes == phenotypes) &&
            (identical(other.attention, attention) ||
                other.attention == attention));
  }

  @JsonKey(includeFromJson: false, includeToJson: false)
  @override
  int get hashCode =>
      Object.hash(runtimeType, patientId, phenotypes, attention);

  /// Create a copy of Attention
  /// with the given fields replaced by the non-null parameter values.
  @JsonKey(includeFromJson: false, includeToJson: false)
  @override
  @pragma('vm:prefer-inline')
  _$$AttentionImplCopyWith<_$AttentionImpl> get copyWith =>
      __$$AttentionImplCopyWithImpl<_$AttentionImpl>(this, _$identity);

  @override
  Map<String, dynamic> toJson() {
    return _$$AttentionImplToJson(
      this,
    );
  }
}

abstract class _Attention implements Attention {
  const factory _Attention(
      {@JsonKey(name: 'patient_id') final int? patientId,
      @JsonKey(name: 'phenotypes') final String? phenotypes,
      @JsonKey(name: 'attention') final double? attention}) = _$AttentionImpl;

  factory _Attention.fromJson(Map<String, dynamic> json) =
      _$AttentionImpl.fromJson;

  @override
  @JsonKey(name: 'patient_id')
  int? get patientId;
  @override
  @JsonKey(name: 'phenotypes')
  String? get phenotypes;
  @override
  @JsonKey(name: 'attention')
  double? get attention;

  /// Create a copy of Attention
  /// with the given fields replaced by the non-null parameter values.
  @override
  @JsonKey(includeFromJson: false, includeToJson: false)
  _$$AttentionImplCopyWith<_$AttentionImpl> get copyWith =>
      throw _privateConstructorUsedError;
}
