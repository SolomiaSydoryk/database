from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from my_project.auth.controller import employee_controller
from my_project.auth.domain import Employee

employee_bp = Blueprint('employee', __name__, url_prefix='/employee')


@employee_bp.get('/all')
def get_all_employees() -> Response:
    return make_response(jsonify(employee_controller.find_all()), HTTPStatus.OK)


@employee_bp.get('/<int:employee_id>')
def get_employee(employee_id: int) -> Response:
    return make_response(jsonify(employee_controller.find_by_id(employee_id)), HTTPStatus.OK)


@employee_bp.get('/<int:employee_id>/supermarket')
def get_supermarket_by_employee(employee_id) -> Response:
    return make_response(
        jsonify(employee_controller.get_supermarket_by_employee(employee_id)), HTTPStatus.OK)


@employee_bp.post('')
def create_employee() -> Response:
    content = request.get_json()
    employee = Employee.create_from_dto(content)
    employee_controller.create(employee)
    return make_response(jsonify(employee.put_into_dto()), HTTPStatus.CREATED)


@employee_bp.put('/<int:owner_id>')
def update_owner(employee_id: int) -> Response:
    content = request.get_json()
    employee = Employee.create_from_dto(content)
    employee_controller.update(employee_id, employee)
    return make_response("Employee updated", HTTPStatus.OK)


@employee_bp.patch('/<int:employee_id>/remove_supermarket')
def remove_supermarket_from_employee(employee_id) -> Response:
    try:
        data = request.get_json()
        supermarket_id = data.get('supermarket_id')

        employee_controller.remove_panel_from_section(employee_id, supermarket_id)

        return make_response(jsonify({"message": "Supermarket removed successfully"}), HTTPStatus.OK)

    except Exception as e:
        return make_response(jsonify({"error": str(e)}), HTTPStatus.INTERNAL_SERVER_ERROR)


@employee_bp.patch('/<int:employee_id>')
def patch_employee(employee_id: int) -> Response:
    content = request.get_json()
    employee_controller.patch(employee_id, content)
    return make_response("Employee updated", HTTPStatus.OK)
