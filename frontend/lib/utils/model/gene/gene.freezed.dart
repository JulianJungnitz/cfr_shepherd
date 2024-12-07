// coverage:ignore-file
// GENERATED CODE - DO NOT MODIFY BY HAND
// ignore_for_file: type=lint
// ignore_for_file: unused_element, deprecated_member_use, deprecated_member_use_from_same_package, use_function_type_syntax_for_parameters, unnecessary_const, avoid_init_to_null, invalid_override_different_default_values_named, prefer_expression_function_bodies, annotate_overrides, invalid_annotation_target, unnecessary_question_mark

part of 'gene.dart';

// **************************************************************************
// FreezedGenerator
// **************************************************************************

T _$identity<T>(T value) => value;

final _privateConstructorUsedError = UnsupportedError(
    'It seems like you constructed your class using `MyClass._()`. This constructor is only meant to be used by freezed and you are not supposed to need it nor use it.\nPlease check the documentation here for more information: https://github.com/rrousselGit/freezed#adding-getters-and-methods-to-our-models');

Gene _$GeneFromJson(Map<String, dynamic> json) {
  return _Gene.fromJson(json);
}

/// @nodoc
mixin _$Gene {
  @JsonKey(name: 'identity')
  int? get identity => throw _privateConstructorUsedError;
  @JsonKey(name: 'labels')
  List<String>? get labels => throw _privateConstructorUsedError;
  @JsonKey(name: 'properties')
  Properties? get properties => throw _privateConstructorUsedError;
  @JsonKey(name: 'elementId')
  String? get elementId => throw _privateConstructorUsedError;

  /// Serializes this Gene to a JSON map.
  Map<String, dynamic> toJson() => throw _privateConstructorUsedError;

  /// Create a copy of Gene
  /// with the given fields replaced by the non-null parameter values.
  @JsonKey(includeFromJson: false, includeToJson: false)
  $GeneCopyWith<Gene> get copyWith => throw _privateConstructorUsedError;
}

/// @nodoc
abstract class $GeneCopyWith<$Res> {
  factory $GeneCopyWith(Gene value, $Res Function(Gene) then) =
      _$GeneCopyWithImpl<$Res, Gene>;
  @useResult
  $Res call(
      {@JsonKey(name: 'identity') int? identity,
      @JsonKey(name: 'labels') List<String>? labels,
      @JsonKey(name: 'properties') Properties? properties,
      @JsonKey(name: 'elementId') String? elementId});

  $PropertiesCopyWith<$Res>? get properties;
}

/// @nodoc
class _$GeneCopyWithImpl<$Res, $Val extends Gene>
    implements $GeneCopyWith<$Res> {
  _$GeneCopyWithImpl(this._value, this._then);

  // ignore: unused_field
  final $Val _value;
  // ignore: unused_field
  final $Res Function($Val) _then;

  /// Create a copy of Gene
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

  /// Create a copy of Gene
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
abstract class _$$GeneImplCopyWith<$Res> implements $GeneCopyWith<$Res> {
  factory _$$GeneImplCopyWith(
          _$GeneImpl value, $Res Function(_$GeneImpl) then) =
      __$$GeneImplCopyWithImpl<$Res>;
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
class __$$GeneImplCopyWithImpl<$Res>
    extends _$GeneCopyWithImpl<$Res, _$GeneImpl>
    implements _$$GeneImplCopyWith<$Res> {
  __$$GeneImplCopyWithImpl(_$GeneImpl _value, $Res Function(_$GeneImpl) _then)
      : super(_value, _then);

  /// Create a copy of Gene
  /// with the given fields replaced by the non-null parameter values.
  @pragma('vm:prefer-inline')
  @override
  $Res call({
    Object? identity = freezed,
    Object? labels = freezed,
    Object? properties = freezed,
    Object? elementId = freezed,
  }) {
    return _then(_$GeneImpl(
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
class _$GeneImpl implements _Gene {
  const _$GeneImpl(
      {@JsonKey(name: 'identity') this.identity,
      @JsonKey(name: 'labels') final List<String>? labels,
      @JsonKey(name: 'properties') this.properties,
      @JsonKey(name: 'elementId') this.elementId})
      : _labels = labels;

  factory _$GeneImpl.fromJson(Map<String, dynamic> json) =>
      _$$GeneImplFromJson(json);

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
    return 'Gene(identity: $identity, labels: $labels, properties: $properties, elementId: $elementId)';
  }

  @override
  bool operator ==(Object other) {
    return identical(this, other) ||
        (other.runtimeType == runtimeType &&
            other is _$GeneImpl &&
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

  /// Create a copy of Gene
  /// with the given fields replaced by the non-null parameter values.
  @JsonKey(includeFromJson: false, includeToJson: false)
  @override
  @pragma('vm:prefer-inline')
  _$$GeneImplCopyWith<_$GeneImpl> get copyWith =>
      __$$GeneImplCopyWithImpl<_$GeneImpl>(this, _$identity);

  @override
  Map<String, dynamic> toJson() {
    return _$$GeneImplToJson(
      this,
    );
  }
}

abstract class _Gene implements Gene {
  const factory _Gene(
      {@JsonKey(name: 'identity') final int? identity,
      @JsonKey(name: 'labels') final List<String>? labels,
      @JsonKey(name: 'properties') final Properties? properties,
      @JsonKey(name: 'elementId') final String? elementId}) = _$GeneImpl;

  factory _Gene.fromJson(Map<String, dynamic> json) = _$GeneImpl.fromJson;

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

  /// Create a copy of Gene
  /// with the given fields replaced by the non-null parameter values.
  @override
  @JsonKey(includeFromJson: false, includeToJson: false)
  _$$GeneImplCopyWith<_$GeneImpl> get copyWith =>
      throw _privateConstructorUsedError;
}

Properties _$PropertiesFromJson(Map<String, dynamic> json) {
  return _Properties.fromJson(json);
}

/// @nodoc
mixin _$Properties {
  @JsonKey(name: 'taxid')
  String? get taxid => throw _privateConstructorUsedError;
  @JsonKey(name: 'synonyms')
  List<String>? get synonyms => throw _privateConstructorUsedError;
  @JsonKey(name: 'name')
  String? get name => throw _privateConstructorUsedError;
  @JsonKey(name: 'id')
  String? get id => throw _privateConstructorUsedError;

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
      {@JsonKey(name: 'taxid') String? taxid,
      @JsonKey(name: 'synonyms') List<String>? synonyms,
      @JsonKey(name: 'name') String? name,
      @JsonKey(name: 'id') String? id});
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
    Object? taxid = freezed,
    Object? synonyms = freezed,
    Object? name = freezed,
    Object? id = freezed,
  }) {
    return _then(_value.copyWith(
      taxid: freezed == taxid
          ? _value.taxid
          : taxid // ignore: cast_nullable_to_non_nullable
              as String?,
      synonyms: freezed == synonyms
          ? _value.synonyms
          : synonyms // ignore: cast_nullable_to_non_nullable
              as List<String>?,
      name: freezed == name
          ? _value.name
          : name // ignore: cast_nullable_to_non_nullable
              as String?,
      id: freezed == id
          ? _value.id
          : id // ignore: cast_nullable_to_non_nullable
              as String?,
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
      {@JsonKey(name: 'taxid') String? taxid,
      @JsonKey(name: 'synonyms') List<String>? synonyms,
      @JsonKey(name: 'name') String? name,
      @JsonKey(name: 'id') String? id});
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
    Object? taxid = freezed,
    Object? synonyms = freezed,
    Object? name = freezed,
    Object? id = freezed,
  }) {
    return _then(_$PropertiesImpl(
      taxid: freezed == taxid
          ? _value.taxid
          : taxid // ignore: cast_nullable_to_non_nullable
              as String?,
      synonyms: freezed == synonyms
          ? _value._synonyms
          : synonyms // ignore: cast_nullable_to_non_nullable
              as List<String>?,
      name: freezed == name
          ? _value.name
          : name // ignore: cast_nullable_to_non_nullable
              as String?,
      id: freezed == id
          ? _value.id
          : id // ignore: cast_nullable_to_non_nullable
              as String?,
    ));
  }
}

/// @nodoc
@JsonSerializable()
class _$PropertiesImpl implements _Properties {
  const _$PropertiesImpl(
      {@JsonKey(name: 'taxid') this.taxid,
      @JsonKey(name: 'synonyms') final List<String>? synonyms,
      @JsonKey(name: 'name') this.name,
      @JsonKey(name: 'id') this.id})
      : _synonyms = synonyms;

  factory _$PropertiesImpl.fromJson(Map<String, dynamic> json) =>
      _$$PropertiesImplFromJson(json);

  @override
  @JsonKey(name: 'taxid')
  final String? taxid;
  final List<String>? _synonyms;
  @override
  @JsonKey(name: 'synonyms')
  List<String>? get synonyms {
    final value = _synonyms;
    if (value == null) return null;
    if (_synonyms is EqualUnmodifiableListView) return _synonyms;
    // ignore: implicit_dynamic_type
    return EqualUnmodifiableListView(value);
  }

  @override
  @JsonKey(name: 'name')
  final String? name;
  @override
  @JsonKey(name: 'id')
  final String? id;

  @override
  String toString() {
    return 'Properties(taxid: $taxid, synonyms: $synonyms, name: $name, id: $id)';
  }

  @override
  bool operator ==(Object other) {
    return identical(this, other) ||
        (other.runtimeType == runtimeType &&
            other is _$PropertiesImpl &&
            (identical(other.taxid, taxid) || other.taxid == taxid) &&
            const DeepCollectionEquality().equals(other._synonyms, _synonyms) &&
            (identical(other.name, name) || other.name == name) &&
            (identical(other.id, id) || other.id == id));
  }

  @JsonKey(includeFromJson: false, includeToJson: false)
  @override
  int get hashCode => Object.hash(runtimeType, taxid,
      const DeepCollectionEquality().hash(_synonyms), name, id);

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
      {@JsonKey(name: 'taxid') final String? taxid,
      @JsonKey(name: 'synonyms') final List<String>? synonyms,
      @JsonKey(name: 'name') final String? name,
      @JsonKey(name: 'id') final String? id}) = _$PropertiesImpl;

  factory _Properties.fromJson(Map<String, dynamic> json) =
      _$PropertiesImpl.fromJson;

  @override
  @JsonKey(name: 'taxid')
  String? get taxid;
  @override
  @JsonKey(name: 'synonyms')
  List<String>? get synonyms;
  @override
  @JsonKey(name: 'name')
  String? get name;
  @override
  @JsonKey(name: 'id')
  String? get id;

  /// Create a copy of Properties
  /// with the given fields replaced by the non-null parameter values.
  @override
  @JsonKey(includeFromJson: false, includeToJson: false)
  _$$PropertiesImplCopyWith<_$PropertiesImpl> get copyWith =>
      throw _privateConstructorUsedError;
}
