import json

from decouple import config
from flask import Flask, Response, request
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import NoResultFound

from auth import valid_auth
from db_utils import get_all_employee, create_employee, get_employee, delete_employee, update_employee
from func_utils import missing_attributes, no_result_found, general_exception, validate_email, validate_phone

app = Flask(__name__)
app.config[
    'SQLALCHEMY_DATABASE_URI'] = config("SQL_DATABASE_URI")

api = Api(app)


@app.route('/')
def hello_world():
    return "Hello"


class Employee(Resource):
    @valid_auth
    def post(self):
        """
                POST: /employee-management/employee

                Create new employee

                Request Body:
                    - `name` (str) -> employee_name
                    - `phone` (str)
                    - `email` (str)
                    - `country` (str)
                    - `department` (str)

                Response Body:
                    - `employee_id` (int)

                Response Code:
                    - `201`: Created
                    - `400`: Invalid request
                """
        try:
            data = request.get_json()
            name = data.get('name')
            phone = data.get('phone')
            email = data.get('email')
            country = data.get('country')
            department = data.get('department')
            validate_email(email)
            validate_phone(phone)
            non_nullable = ['name', 'phone', 'email', 'country', 'department']
            missing_attributes(data, non_nullable)

            employee_data = create_employee(name, phone, email, country, department)
            return Response(response=json.dumps({"project_id": employee_data}), status=201,
                            mimetype='application/json')
        except NoResultFound:
            return no_result_found()
        except Exception:
            return general_exception()

    @valid_auth
    def get(self):
        """
                GET: /employee-management/employee

                Get list of all employees

                Response Body: (list)
                    - `employee_id` (int)
                    - `employee_name` (str)
                    - `phone` (str)
                    - `email` (str)
                    - `country` (str)
                    - `department` (str)

                Response Code:
                    - `200`: Success
                    - `400`: Invalid request
                """
        try:
            employee_data = get_all_employee()
            result = []
            if employee_data:
                for employee in employee_data:
                    out = {
                        "employee_id": employee.id,
                        "employee_name": employee.name,
                        "phone": employee.phone,
                        "email": employee.email,
                        "country": employee.country,
                        "department": employee.department
                    }
                    result.append(out)
            return Response(response=json.dumps(result), status=200,
                            mimetype='application/json')
        except NoResultFound:
            return no_result_found()
        except Exception:
            return general_exception()


api.add_resource(Employee, '/employee-management/employee')


class EmployeeManagement(Resource):
    @valid_auth
    def get(self, employee_id):
        """
                GET: /employee-management/employee/<int:employee_id>

                Get employee details

                Response Body:
                    - `employee_id` (int)
                    - `employee_name` (str)
                    - `phone` (str)
                    - `email` (str)
                    - `country` (str)
                    - `department` (str)

                Response Code:
                    - `200`: Success
                    - `400`: Invalid request
                """
        try:
            employee_data = get_employee(employee_id)
            result = {
                "employee_id": employee_data.id,
                "employee_name": employee_data.name,
                "phone": employee_data.phone,
                "email": employee_data.email,
                "country": employee_data.country,
                "department": employee_data.department
            }
            return Response(response=json.dumps(result), status=200,
                            mimetype='application/json')
        except NoResultFound:
            return no_result_found()
        except Exception:
            return general_exception()

    @valid_auth
    def put(self, employee_id):
        """
                PUT: /employee-management/employee/<int:employee_id>

                Update employee details

                Response Body:
                    - `message` (str): Employee updated successfully

                Response Code:
                    - `200`: Success
                    - `400`: Invalid request
                """
        try:
            data = request.get_json()
            non_nullable = ['name', 'phone', 'email', 'country', 'department']
            missing_attributes(data, non_nullable)
            validate_email(data["email"])
            validate_phone(data["phone"])
            update_employee(employee_id, data)
            return Response(response=json.dumps({"message": "Updated successfully!"}), status=200,
                            mimetype='application/json')
        except NoResultFound:
            return no_result_found()
        except Exception:
            return general_exception()

    @valid_auth
    def delete(self, employee_id):
        """
                DELETE: /employee-management/employee/<int:employee_id>

                Delete employee from list of all Employee

                Response Body:
                    - `message` (str): Employee deleted from the list

                Response Code:
                    - `200`: Success
                    - `400`: Invalid request
                """
        try:
            delete_employee(employee_id)
            return Response(response=json.dumps({"message": "Employee deleted successfully!"}), status=200,
                            mimetype='application/json')
        except NoResultFound:
            return no_result_found()
        except Exception:
            return general_exception()


api.add_resource(EmployeeManagement, '/employee-management/employee/<int:employee_id>')

if __name__ == '__main__':
    app.run(debug=True)
