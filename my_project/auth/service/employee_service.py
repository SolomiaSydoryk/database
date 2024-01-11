from my_project.auth.service.general_service import GeneralService
from my_project.auth.dao import employee_dao


class EmployeeService(GeneralService):
    _dao = employee_dao
