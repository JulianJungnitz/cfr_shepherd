// coverage:ignore-file
// GENERATED CODE - DO NOT MODIFY BY HAND
// ignore_for_file: type=lint
// ignore_for_file: unused_element, deprecated_member_use, deprecated_member_use_from_same_package, use_function_type_syntax_for_parameters, unnecessary_const, avoid_init_to_null, invalid_override_different_default_values_named, prefer_expression_function_bodies, annotate_overrides, invalid_annotation_target, unnecessary_question_mark

part of 'disease.dart';

// **************************************************************************
// FreezedGenerator
// **************************************************************************

T _$identity<T>(T value) => value;

final _privateConstructorUsedError = UnsupportedError(
    'It seems like you constructed your class using `MyClass._()`. This constructor is only meant to be used by freezed and you are not supposed to need it nor use it.\nPlease check the documentation here for more information: https://github.com/rrousselGit/freezed#adding-getters-and-methods-to-our-models');

Disease _$DiseaseFromJson(Map<String, dynamic> json) {
  return _Disease.fromJson(json);
}

/// @nodoc
mixin _$Disease {
  @JsonKey(name: 'synonyms')
  List<String>? get synonyms => throw _privateConstructorUsedError;
  @JsonKey(name: 'name')
  String? get name => throw _privateConstructorUsedError;
  @JsonKey(name: 'description')
  String? get description => throw _privateConstructorUsedError;
  @JsonKey(name: 'id')
  String? get id => throw _privateConstructorUsedError;
  @JsonKey(name: 'type')
  String? get type => throw _privateConstructorUsedError;

  /// Serializes this Disease to a JSON map.
  Map<String, dynamic> toJson() => throw _privateConstructorUsedError;

  /// Create a copy of Disease
  /// with the given fields replaced by the non-null parameter values.
  @JsonKey(includeFromJson: false, includeToJson: false)
  $DiseaseCopyWith<Disease> get copyWith => throw _privateConstructorUsedError;
}

/// @nodoc
abstract class $DiseaseCopyWith<$Res> {
  factory $DiseaseCopyWith(Disease value, $Res Function(Disease) then) =
      _$DiseaseCopyWithImpl<$Res, Disease>;
  @useResult
  $Res call(
      {@JsonKey(name: 'synonyms') List<String>? synonyms,
      @JsonKey(name: 'name') String? name,
      @JsonKey(name: 'description') String? description,
      @JsonKey(name: 'id') String? id,
      @JsonKey(name: 'type') String? type});
}

/// @nodoc
class _$DiseaseCopyWithImpl<$Res, $Val extends Disease>
    implements $DiseaseCopyWith<$Res> {
  _$DiseaseCopyWithImpl(this._value, this._then);

  // ignore: unused_field
  final $Val _value;
  // ignore: unused_field
  final $Res Function($Val) _then;

  /// Create a copy of Disease
  /// with the given fields replaced by the non-null parameter values.
  @pragma('vm:prefer-inline')
  @override
  $Res call({
    Object? synonyms = freezed,
    Object? name = freezed,
    Object? description = freezed,
    Object? id = freezed,
    Object? type = freezed,
  }) {
    return _then(_value.copyWith(
      synonyms: freezed == synonyms
          ? _value.synonyms
          : synonyms // ignore: cast_nullable_to_non_nullable
              as List<String>?,
      name: freezed == name
          ? _value.name
          : name // ignore: cast_nullable_to_non_nullable
              as String?,
      description: freezed == description
          ? _value.description
          : description // ignore: cast_nullable_to_non_nullable
              as String?,
      id: freezed == id
          ? _value.id
          : id // ignore: cast_nullable_to_non_nullable
              as String?,
      type: freezed == type
          ? _value.type
          : type // ignore: cast_nullable_to_non_nullable
              as String?,
    ) as $Val);
  }
}

/// @nodoc
abstract class _$$DiseaseImplCopyWith<$Res> implements $DiseaseCopyWith<$Res> {
  factory _$$DiseaseImplCopyWith(
          _$DiseaseImpl value, $Res Function(_$DiseaseImpl) then) =
      __$$DiseaseImplCopyWithImpl<$Res>;
  @override
  @useResult
  $Res call(
      {@JsonKey(name: 'synonyms') List<String>? synonyms,
      @JsonKey(name: 'name') String? name,
      @JsonKey(name: 'description') String? description,
      @JsonKey(name: 'id') String? id,
      @JsonKey(name: 'type') String? type});
}

/// @nodoc
class __$$DiseaseImplCopyWithImpl<$Res>
    extends _$DiseaseCopyWithImpl<$Res, _$DiseaseImpl>
    implements _$$DiseaseImplCopyWith<$Res> {
  __$$DiseaseImplCopyWithImpl(
      _$DiseaseImpl _value, $Res Function(_$DiseaseImpl) _then)
      : super(_value, _then);

  /// Create a copy of Disease
  /// with the given fields replaced by the non-null parameter values.
  @pragma('vm:prefer-inline')
  @override
  $Res call({
    Object? synonyms = freezed,
    Object? name = freezed,
    Object? description = freezed,
    Object? id = freezed,
    Object? type = freezed,
  }) {
    return _then(_$DiseaseImpl(
      synonyms: freezed == synonyms
          ? _value._synonyms
          : synonyms // ignore: cast_nullable_to_non_nullable
              as List<String>?,
      name: freezed == name
          ? _value.name
          : name // ignore: cast_nullable_to_non_nullable
              as String?,
      description: freezed == description
          ? _value.description
          : description // ignore: cast_nullable_to_non_nullable
              as String?,
      id: freezed == id
          ? _value.id
          : id // ignore: cast_nullable_to_non_nullable
              as String?,
      type: freezed == type
          ? _value.type
          : type // ignore: cast_nullable_to_non_nullable
              as String?,
    ));
  }
}

/// @nodoc
@JsonSerializable()
class _$DiseaseImpl implements _Disease {
  const _$DiseaseImpl(
      {@JsonKey(name: 'synonyms') final List<String>? synonyms,
      @JsonKey(name: 'name') this.name,
      @JsonKey(name: 'description') this.description,
      @JsonKey(name: 'id') this.id,
      @JsonKey(name: 'type') this.type})
      : _synonyms = synonyms;

  factory _$DiseaseImpl.fromJson(Map<String, dynamic> json) =>
      _$$DiseaseImplFromJson(json);

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
  @JsonKey(name: 'description')
  final String? description;
  @override
  @JsonKey(name: 'id')
  final String? id;
  @override
  @JsonKey(name: 'type')
  final String? type;

  @override
  String toString() {
    return 'Disease(synonyms: $synonyms, name: $name, description: $description, id: $id, type: $type)';
  }

  @override
  bool operator ==(Object other) {
    return identical(this, other) ||
        (other.runtimeType == runtimeType &&
            other is _$DiseaseImpl &&
            const DeepCollectionEquality().equals(other._synonyms, _synonyms) &&
            (identical(other.name, name) || other.name == name) &&
            (identical(other.description, description) ||
                other.description == description) &&
            (identical(other.id, id) || other.id == id) &&
            (identical(other.type, type) || other.type == type));
  }

  @JsonKey(includeFromJson: false, includeToJson: false)
  @override
  int get hashCode => Object.hash(
      runtimeType,
      const DeepCollectionEquality().hash(_synonyms),
      name,
      description,
      id,
      type);

  /// Create a copy of Disease
  /// with the given fields replaced by the non-null parameter values.
  @JsonKey(includeFromJson: false, includeToJson: false)
  @override
  @pragma('vm:prefer-inline')
  _$$DiseaseImplCopyWith<_$DiseaseImpl> get copyWith =>
      __$$DiseaseImplCopyWithImpl<_$DiseaseImpl>(this, _$identity);

  @override
  Map<String, dynamic> toJson() {
    return _$$DiseaseImplToJson(
      this,
    );
  }
}

abstract class _Disease implements Disease {
  const factory _Disease(
      {@JsonKey(name: 'synonyms') final List<String>? synonyms,
      @JsonKey(name: 'name') final String? name,
      @JsonKey(name: 'description') final String? description,
      @JsonKey(name: 'id') final String? id,
      @JsonKey(name: 'type') final String? type}) = _$DiseaseImpl;

  factory _Disease.fromJson(Map<String, dynamic> json) = _$DiseaseImpl.fromJson;

  @override
  @JsonKey(name: 'synonyms')
  List<String>? get synonyms;
  @override
  @JsonKey(name: 'name')
  String? get name;
  @override
  @JsonKey(name: 'description')
  String? get description;
  @override
  @JsonKey(name: 'id')
  String? get id;
  @override
  @JsonKey(name: 'type')
  String? get type;

  /// Create a copy of Disease
  /// with the given fields replaced by the non-null parameter values.
  @override
  @JsonKey(includeFromJson: false, includeToJson: false)
  _$$DiseaseImplCopyWith<_$DiseaseImpl> get copyWith =>
      throw _privateConstructorUsedError;
}
