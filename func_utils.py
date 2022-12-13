import json
import re
from flask import Response


def missing_attributes(data, non_nullable):
    missing_attributes = []
    for i in non_nullable:
        if i not in data.keys():
            missing_attributes.append(i)
    missing_attributes = ", ".join(missing_attributes)
    if len(missing_attributes) > 0:
        return Response(response=json.dumps({"message": f"{missing_attributes} are missing!"}), status=400,
                        mimetype='application/json')
    return True


def validate_email(email):
    email_validate_pattern = r"^\S+@\S+\.\S+$"
    if re.match(email_validate_pattern, email):
        return True
    else:
        return Response(response=json.dumps({"message": "Invalid email!"}), status=403,
                        mimetype='application/json')


def validate_phone(phone):
    Pattern = re.compile("(0|91)?[6-9][0-9]{9}")
    if Pattern.match(phone):
        return True
    else:
        return Response(response=json.dumps({"message": "Invalid phone number!"}), status=403,
                        mimetype='application/json')


def no_result_found():
    return Response(response=json.dumps({"message": "No Result Found!"}), status=404,
                    mimetype='application/json')


def general_exception():
    return Response(response=json.dumps({"message": "Server Error!"}), status=500,
                    mimetype='application/json')
