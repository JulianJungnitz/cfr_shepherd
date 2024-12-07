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
  @JsonKey(name: 'identity')
  int? get identity => throw _privateConstructorUsedError;
  @JsonKey(name: 'labels')
  List<String>? get labels => throw _privateConstructorUsedError;
  @JsonKey(name: 'properties')
  Properties? get properties => throw _privateConstructorUsedError;
  @JsonKey(name: 'elementId')
  String? get elementId => throw _privateConstructorUsedError;

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
      {@JsonKey(name: 'identity') int? identity,
      @JsonKey(name: 'labels') List<String>? labels,
      @JsonKey(name: 'properties') Properties? properties,
      @JsonKey(name: 'elementId') String? elementId});

  $PropertiesCopyWith<$Res>? get properties;
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
    Object? identity = freezed,
    Object? labels = freezed,
    Object? properties = freezed,
    Object? elementId = freezed,
  }) {
    return _then(_value.copyWith(
      identity: freezed == identity
          ? _value.identity
          : identity // ignore: cast_nullable_to_non_nullable
              as int?,
      labels: freezed == labels
          ? _value.labels
          : labels // ignore: cast_nullable_to_non_nullable
              as List<String>?,
      properties: freezed == properties
          ? _value.properties
          : properties // ignore: cast_nullable_to_non_nullable
              as Properties?,
      elementId: freezed == elementId
          ? _value.elementId
          : elementId // ignore: cast_nullable_to_non_nullable
              as String?,
    ) as $Val);
  }

  /// Create a copy of BiologicalSample
  /// with the given fields replaced by the non-null parameter values.
  @override
  @pragma('vm:prefer-inline')
  $PropertiesCopyWith<$Res>? get properties {
    if (_value.properties == null) {
      return null;
    }

    return $PropertiesCopyWith<$Res>(_value.properties!, (value) {
      return _then(_value.copyWith(properties: value) as $Val);
    });
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
      {@JsonKey(name: 'identity') int? identity,
      @JsonKey(name: 'labels') List<String>? labels,
      @JsonKey(name: 'properties') Properties? properties,
      @JsonKey(name: 'elementId') String? elementId});

  @override
  $PropertiesCopyWith<$Res>? get properties;
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
    Object? identity = freezed,
    Object? labels = freezed,
    Object? properties = freezed,
    Object? elementId = freezed,
  }) {
    return _then(_$BiologicalSampleImpl(
      identity: freezed == identity
          ? _value.identity
          : identity // ignore: cast_nullable_to_non_nullable
              as int?,
      labels: freezed == labels
          ? _value._labels
          : labels // ignore: cast_nullable_to_non_nullable
              as List<String>?,
      properties: freezed == properties
          ? _value.properties
          : properties // ignore: cast_nullable_to_non_nullable
              as Properties?,
      elementId: freezed == elementId
          ? _value.elementId
          : elementId // ignore: cast_nullable_to_non_nullable
              as String?,
    ));
  }
}

/// @nodoc
@JsonSerializable()
class _$BiologicalSampleImpl implements _BiologicalSample {
  const _$BiologicalSampleImpl(
      {@JsonKey(name: 'identity') this.identity,
      @JsonKey(name: 'labels') final List<String>? labels,
      @JsonKey(name: 'properties') this.properties,
      @JsonKey(name: 'elementId') this.elementId})
      : _labels = labels;

  factory _$BiologicalSampleImpl.fromJson(Map<String, dynamic> json) =>
      _$$BiologicalSampleImplFromJson(json);

  @override
  @JsonKey(name: 'identity')
  final int? identity;
  final List<String>? _labels;
  @override
  @JsonKey(name: 'labels')
  List<String>? get labels {
    final value = _labels;
    if (value == null) return null;
    if (_labels is EqualUnmodifiableListView) return _labels;
    // ignore: implicit_dynamic_type
    return EqualUnmodifiableListView(value);
  }

  @override
  @JsonKey(name: 'properties')
  final Properties? properties;
  @override
  @JsonKey(name: 'elementId')
  final String? elementId;

  @override
  String toString() {
    return 'BiologicalSample(identity: $identity, labels: $labels, properties: $properties, elementId: $elementId)';
  }

  @override
  bool operator ==(Object other) {
    return identical(this, other) ||
        (other.runtimeType == runtimeType &&
            other is _$BiologicalSampleImpl &&
            (identical(other.identity, identity) ||
                other.identity == identity) &&
            const DeepCollectionEquality().equals(other._labels, _labels) &&
            (identical(other.properties, properties) ||
                other.properties == properties) &&
            (identical(other.elementId, elementId) ||
                other.elementId == elementId));
  }

  @JsonKey(includeFromJson: false, includeToJson: false)
  @override
  int get hashCode => Object.hash(runtimeType, identity,
      const DeepCollectionEquality().hash(_labels), properties, elementId);

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
          {@JsonKey(name: 'identity') final int? identity,
          @JsonKey(name: 'labels') final List<String>? labels,
          @JsonKey(name: 'properties') final Properties? properties,
          @JsonKey(name: 'elementId') final String? elementId}) =
      _$BiologicalSampleImpl;

  factory _BiologicalSample.fromJson(Map<String, dynamic> json) =
      _$BiologicalSampleImpl.fromJson;

  @override
  @JsonKey(name: 'identity')
  int? get identity;
  @override
  @JsonKey(name: 'labels')
  List<String>? get labels;
  @override
  @JsonKey(name: 'properties')
  Properties? get properties;
  @override
  @JsonKey(name: 'elementId')
  String? get elementId;

  /// Create a copy of BiologicalSample
  /// with the given fields replaced by the non-null parameter values.
  @override
  @JsonKey(includeFromJson: false, includeToJson: false)
  _$$BiologicalSampleImplCopyWith<_$BiologicalSampleImpl> get copyWith =>
      throw _privateConstructorUsedError;
}

Properties _$PropertiesFromJson(Map<String, dynamic> json) {
  return _Properties.fromJson(json);
}

/// @nodoc
mixin _$Properties {
  @JsonKey(name: 'external_id')
  String? get externalId => throw _privateConstructorUsedError;
  @JsonKey(name: 'subjectid')
  int? get subjectid => throw _privateConstructorUsedError;

  /// Serializes this Properties to a JSON map.
  Map<String, dynamic> toJson() => throw _privateConstructorUsedError;

  /// Create a copy of Properties
  /// with the given fields replaced by the non-null parameter values.
  @JsonKey(includeFromJson: false, includeToJson: false)
  $PropertiesCopyWith<Properties> get copyWith =>
      throw _privateConstructorUsedError;
}

/// @nodoc
abstract class $PropertiesCopyWith<$Res> {
  factory $PropertiesCopyWith(
          Properties value, $Res Function(Properties) then) =
      _$PropertiesCopyWithImpl<$Res, Properties>;
  @useResult
  $Res call(
      {@JsonKey(name: 'external_id') String? externalId,
      @JsonKey(name: 'subjectid') int? subjectid});
}

/// @nodoc
class _$PropertiesCopyWithImpl<$Res, $Val extends Properties>
    implements $PropertiesCopyWith<$Res> {
  _$PropertiesCopyWithImpl(this._value, this._then);

  // ignore: unused_field
  final $Val _value;
  // ignore: unused_field
  final $Res Function($Val) _then;

  /// Create a copy of Properties
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
abstract class _$$PropertiesImplCopyWith<$Res>
    implements $PropertiesCopyWith<$Res> {
  factory _$$PropertiesImplCopyWith(
          _$PropertiesImpl value, $Res Function(_$PropertiesImpl) then) =
      __$$PropertiesImplCopyWithImpl<$Res>;
  @override
  @useResult
  $Res call(
      {@JsonKey(name: 'external_id') String? externalId,
      @JsonKey(name: 'subjectid') int? subjectid});
}

/// @nodoc
class __$$PropertiesImplCopyWithImpl<$Res>
    extends _$PropertiesCopyWithImpl<$Res, _$PropertiesImpl>
    implements _$$PropertiesImplCopyWith<$Res> {
  __$$PropertiesImplCopyWithImpl(
      _$PropertiesImpl _value, $Res Function(_$PropertiesImpl) _then)
      : super(_value, _then);

  /// Create a copy of Properties
  /// with the given fields replaced by the non-null parameter values.
  @pragma('vm:prefer-inline')
  @override
  $Res call({
    Object? externalId = freezed,
    Object? subjectid = freezed,
  }) {
    return _then(_$PropertiesImpl(
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
class _$PropertiesImpl implements _Properties {
  const _$PropertiesImpl(
      {@JsonKey(name: 'external_id') this.externalId,
      @JsonKey(name: 'subjectid') this.subjectid});

  factory _$PropertiesImpl.fromJson(Map<String, dynamic> json) =>
      _$$PropertiesImplFromJson(json);

  @override
  @JsonKey(name: 'external_id')
  final String? externalId;
  @override
  @JsonKey(name: 'subjectid')
  final int? subjectid;

  @override
  String toString() {
    return 'Properties(externalId: $externalId, subjectid: $subjectid)';
  }

  @override
  bool operator ==(Object other) {
    return identical(this, other) ||
        (other.runtimeType == runtimeType &&
            other is _$PropertiesImpl &&
            (identical(other.externalId, externalId) ||
                other.externalId == externalId) &&
            (identical(other.subjectid, subjectid) ||
                other.subjectid == subjectid));
  }

  @JsonKey(includeFromJson: false, includeToJson: false)
  @override
  int get hashCode => Object.hash(runtimeType, externalId, subjectid);

  /// Create a copy of Properties
  /// with the given fields replaced by the non-null parameter values.
  @JsonKey(includeFromJson: false, includeToJson: false)
  @override
  @pragma('vm:prefer-inline')
  _$$PropertiesImplCopyWith<_$PropertiesImpl> get copyWith =>
      __$$PropertiesImplCopyWithImpl<_$PropertiesImpl>(this, _$identity);

  @override
  Map<String, dynamic> toJson() {
    return _$$PropertiesImplToJson(
      this,
    );
  }
}

abstract class _Properties implements Properties {
  const factory _Properties(
      {@JsonKey(name: 'external_id') final String? externalId,
      @JsonKey(name: 'subjectid') final int? subjectid}) = _$PropertiesImpl;

  factory _Properties.fromJson(Map<String, dynamic> json) =
      _$PropertiesImpl.fromJson;

  @override
  @JsonKey(name: 'external_id')
  String? get externalId;
  @override
  @JsonKey(name: 'subjectid')
  int? get subjectid;

  /// Create a copy of Properties
  /// with the given fields replaced by the non-null parameter values.
  @override
  @JsonKey(includeFromJson: false, includeToJson: false)
  _$$PropertiesImplCopyWith<_$PropertiesImpl> get copyWith =>
      throw _privateConstructorUsedError;
}
