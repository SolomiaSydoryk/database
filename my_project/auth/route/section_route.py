from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from my_project.auth.controller import section_controller
from my_project.auth.domain import Section

section_bp = Blueprint('section', __name__, url_prefix='/section')


@section_bp.get('/all')
def get_all_sections() -> Response:
    return make_response(jsonify(section_controller.find_all()), HTTPStatus.OK)


@section_bp.get('/<int:section_id>')
def get_section(section_id: int) -> Response:
    return make_response(jsonify(section_controller.find_by_id(section_id)), HTTPStatus.OK)


@section_bp.get('/<int:section_id>/panel')
def get_panel_by_section(section_id) -> Response:
    return make_response(
        jsonify(section_controller.get_panel_by_section(section_id)), HTTPStatus.OK)


@section_bp.post('')
def create_section() -> Response:
    content = request.get_json()
    section = Section.create_from_dto(content)
    section_controller.create(section)
    return make_response(jsonify(section.put_into_dto()), HTTPStatus.CREATED)


@section_bp.post('/<int:section_id>/add_panel')
def add_panel_to_section(section_id) -> Response:
    try:
        data = request.get_json()
        panel_id = data.get('interactive_advertising_panel_id')

        section_controller.add_panel_to_section(section_id, panel_id)

        return make_response(jsonify({"message": "Panel added successfully"}), HTTPStatus.OK)

    except Exception as e:
        return make_response(jsonify({"error": str(e)}), HTTPStatus.INTERNAL_SERVER_ERROR)


@section_bp.put('/<int:section_id>')
def update_section(section_id: int) -> Response:
    content = request.get_json()
    section = Section.create_from_dto(content)
    section_controller.update(section_id, section)
    return make_response("Section updated", HTTPStatus.OK)


@section_bp.patch('/<int:section_id>/remove_panel')
def remove_panel_from_section(section_id) -> Response:
    try:
        data = request.get_json()
        panel_id = data.get('interactive_advertising_panel_id')

        section_controller.remove_panel_from_section(section_id, panel_id)

        return make_response(jsonify({"message": "Panel removed successfully"}), HTTPStatus.OK)

    except Exception as e:
        return make_response(jsonify({"error": str(e)}), HTTPStatus.INTERNAL_SERVER_ERROR)


@section_bp.patch('/<int:section_id>')
def patch_section(section_id: int) -> Response:
    content = request.get_json()
    section_controller.patch(section_id, content)
    return make_response("Section updated", HTTPStatus.OK)


@section_bp.delete('/<int:section_id>')
def delete_section(section_id: int) -> Response:
    section_controller.delete(section_id)
    return make_response("Section deleted", HTTPStatus.OK)
