from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain import Employee


class EmployeeDAO(GeneralDAO):
    """
    Realisation of Employee data access layer.
    """
    _domain_type = Employee
