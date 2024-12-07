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
  @JsonKey(name: 'taxid')
  String? get taxid => throw _privateConstructorUsedError;
  @JsonKey(name: 'synonyms')
  List<String>? get synonyms => throw _privateConstructorUsedError;
  @JsonKey(name: 'name')
  String? get name => throw _privateConstructorUsedError;
  @JsonKey(name: 'id')
  String? get id => throw _privateConstructorUsedError;
  @JsonKey(name: 'family')
  String? get family => throw _privateConstructorUsedError;

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
      {@JsonKey(name: 'taxid') String? taxid,
      @JsonKey(name: 'synonyms') List<String>? synonyms,
      @JsonKey(name: 'name') String? name,
      @JsonKey(name: 'id') String? id,
      @JsonKey(name: 'family') String? family});
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
    Object? taxid = freezed,
    Object? synonyms = freezed,
    Object? name = freezed,
    Object? id = freezed,
    Object? family = freezed,
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
      family: freezed == family
          ? _value.family
          : family // ignore: cast_nullable_to_non_nullable
              as String?,
    ) as $Val);
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
      {@JsonKey(name: 'taxid') String? taxid,
      @JsonKey(name: 'synonyms') List<String>? synonyms,
      @JsonKey(name: 'name') String? name,
      @JsonKey(name: 'id') String? id,
      @JsonKey(name: 'family') String? family});
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
    Object? taxid = freezed,
    Object? synonyms = freezed,
    Object? name = freezed,
    Object? id = freezed,
    Object? family = freezed,
  }) {
    return _then(_$GeneImpl(
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
      family: freezed == family
          ? _value.family
          : family // ignore: cast_nullable_to_non_nullable
              as String?,
    ));
  }
}

/// @nodoc
@JsonSerializable()
class _$GeneImpl implements _Gene {
  const _$GeneImpl(
      {@JsonKey(name: 'taxid') this.taxid,
      @JsonKey(name: 'synonyms') final List<String>? synonyms,
      @JsonKey(name: 'name') this.name,
      @JsonKey(name: 'id') this.id,
      @JsonKey(name: 'family') this.family})
      : _synonyms = synonyms;

  factory _$GeneImpl.fromJson(Map<String, dynamic> json) =>
      _$$GeneImplFromJson(json);

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
  @JsonKey(name: 'family')
  final String? family;

  @override
  String toString() {
    return 'Gene(taxid: $taxid, synonyms: $synonyms, name: $name, id: $id, family: $family)';
  }

  @override
  bool operator ==(Object other) {
    return identical(this, other) ||
        (other.runtimeType == runtimeType &&
            other is _$GeneImpl &&
            (identical(other.taxid, taxid) || other.taxid == taxid) &&
            const DeepCollectionEquality().equals(other._synonyms, _synonyms) &&
            (identical(other.name, name) || other.name == name) &&
            (identical(other.id, id) || other.id == id) &&
            (identical(other.family, family) || other.family == family));
  }

  @JsonKey(includeFromJson: false, includeToJson: false)
  @override
  int get hashCode => Object.hash(runtimeType, taxid,
      const DeepCollectionEquality().hash(_synonyms), name, id, family);

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
      {@JsonKey(name: 'taxid') final String? taxid,
      @JsonKey(name: 'synonyms') final List<String>? synonyms,
      @JsonKey(name: 'name') final String? name,
      @JsonKey(name: 'id') final String? id,
      @JsonKey(name: 'family') final String? family}) = _$GeneImpl;

  factory _Gene.fromJson(Map<String, dynamic> json) = _$GeneImpl.fromJson;

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
  @override
  @JsonKey(name: 'family')
  String? get family;

  /// Create a copy of Gene
  /// with the given fields replaced by the non-null parameter values.
  @override
  @JsonKey(includeFromJson: false, includeToJson: false)
  _$$GeneImplCopyWith<_$GeneImpl> get copyWith =>
      throw _privateConstructorUsedError;
}
