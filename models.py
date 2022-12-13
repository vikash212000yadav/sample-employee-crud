from enum import Enum

from extensions import db, ma


class DepartmentType(Enum):
    Technology = 'Technology'
    Marketing = 'Marketing'
    Sales = 'Sales'
    HR = 'HR'
    Business = 'Business'
    Management = 'Management'


class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(100), nullable=False)
    email = db.Column(db.Integer(), nullable=False)
    country = db.Column(db.String(100), nullable=False)
    department = db.Column(db.Enum(DepartmentType), nullable=False)

    def __init__(self, name):
        self.name = name


class EmployeeSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Employee
        load_instance = True

    id = ma.auto_field()
    name = ma.auto_field()
    phone = ma.auto_field()
    email = ma.auto_field()
    country = ma.auto_field()
    department = ma.auto_field()


# db.create_all()
