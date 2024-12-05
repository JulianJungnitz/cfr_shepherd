import 'package:freezed_annotation/freezed_annotation.dart'; 

part 'patient_like_me.freezed.dart';
part 'patient_like_me.g.dart';

@freezed
class PatientLikeMe with _$PatientLikeMe {
	const factory PatientLikeMe({
int? patient_id,
int? candidate_patients,
double? similarities,
	}) = _PatientLikeMe;

	factory PatientLikeMe.fromJson(Map<String, dynamic> json) => _$PatientLikeMeFromJson(json);
}