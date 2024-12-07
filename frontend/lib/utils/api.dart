import 'dart:convert';
import 'package:dio/dio.dart';
import 'package:http/http.dart' as http;

abstract class APIPaths {
  static const patientsLikeMe = '/patients_like_me';
  static const causalGeneDiscovery = '/causal_gene_discovery';
  static const diseaseCharacterization = '/disease_characterization';
  static const query = '/query';
  static const hasPatientsLikeMeResults = '/has_patients_like_me';
  static const hasCausalGeneDiscoveryResults = '/has_causal_gene_discovery';
  static const hasDiseaseCharacterizationResults = '/has_disease_characterization';
}

class API {
  static const String baseUrl = 'http://0.0.0.0:9001/cfr_api';

  static Future<APIResult> post(String path,
      {Map<String, dynamic> body = const {},
      bool rawString = false,
      bool debug = false}) async {
    var headers = {
      'Content-Type': 'application/json',
      'Access-Control-Allow-Origin': '*',
    };

    String apiPath = baseUrl + path;

    printBody(apiPath, body: body);
    try {
      var dio = Dio();
      var response = await dio.request(
        apiPath,
        options: Options(
          method: 'POST',
          headers: headers,
        ),
        data: json.encode(body),
      );
      if (debug) print("API $path: response: " + response.data.toString());

      if (response.statusCode != 200) {
        return APIResult(false, null, message: response.statusMessage);
      }

      if (rawString) {
        return APIResult(true, response.data);
      }

      var tmp = response.data;
      String? message = tmp["message"];
      dynamic data = tmp["data"];
      return APIResult(true, data, message: message);
    } catch (e) {
      print("APIError: " + e.toString());
      return APIResult(false, null, message: 'Error while sending request');
    }
  }

  static Future<APIResult> get(String path,
      {bool asUint8List = false,
      bool noPrint = true,
      bool rawString = false}) async {
    var headers = {
      if (rawString == false) 'Content-Type': 'application/json',
      'Access-Control-Allow-Origin': '*',
    };

    String apiPath = baseUrl + path;

    try {
      http.Response response =
          await http.get(Uri.parse(apiPath), headers: headers);

      if (!noPrint) print("API $path: response: " + response.body.toString());
      if (response.statusCode != 200) {
        print("APIError: " + response.reasonPhrase.toString());
        return APIResult(false, null, message: response.reasonPhrase);
      }
      if (asUint8List) {
        return APIResult(true, response.bodyBytes);
      }

      if(rawString) {
        return APIResult(true, response.body);
      }
      var tmp = json.decode(response.body);
      String? message = tmp["message"];
      dynamic data = tmp["data"];
      return APIResult(true, data, message: message);
    } catch (e) {
      print("APIError: " + e.toString());
      return APIResult(false, null, message: 'Error while sending request');
    }
  }

  static void printBody(String path, {Map<String, dynamic> body = const {}}) {
    Map<String, String> bodyCopy = {};
    for (var key in body.keys) {
      String valueString = "";
      if (body[key] is String) {
        valueString = "\"${body[key]}\"";
      } else {
        valueString = body[key].toString();
      }
      bodyCopy["\"$key\""] = valueString;
    }
    print("API: path: " + path + " body: " + bodyCopy.toString());
  }
}

class APIResult {
  final bool success;
  final dynamic data;
  final String? message;

  APIResult(this.success, this.data, {this.message});
}
