from flask_sqlalchemy import SQLAlchemy
from models import Employee

db = SQLAlchemy()


def get_all_employee():
    try:
        employee_data = Employee.query.filter_by().all()
        return employee_data
    except Exception as e:
        raise e


def get_employee(employee_id):
    try:
        employee = Employee.query.filter_by(id=employee_id).one()
        return employee
    except Exception as e:
        raise e


def create_employee(name, phone, email, country, department):
    try:
        employee = Employee(name=name)
        employee.phone = phone
        employee.email = email
        employee.country = country
        employee.department = department
        db.session.add(employee)
        db.session.flush()
        db.session.commit()
        return employee.id
    except Exception as e:
        db.session.rollback()
        raise e


def update_employee(employee_id, data):
    try:
        employee_data = Employee.query.filter_by(id=employee_id).first()
        if employee_data:
            employee_data.name = data["name"]
            employee_data.phone = data["phone"]
            employee_data.email = data["email"]
            employee_data.country = data["country"]
            employee_data.department = data["department"]
            db.session.merge(employee_data)
            db.session.commit()
        return True
    except Exception as e:
        db.session.rollback()
        raise e


def delete_employee(employee_id):
    try:
        employee_data = Employee.query.filter_by(id=employee_id).one()
        obj = db.session.merge(employee_data)
        db.session.delete(obj)
        db.session.commit()
        return True
    except Exception as e:
        raise e
