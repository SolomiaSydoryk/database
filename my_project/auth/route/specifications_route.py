from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from my_project.auth.controller import specifications_controller
from my_project.auth.domain import Specifications

specifications_bp = Blueprint('specifications', __name__, url_prefix='/specifications')


@specifications_bp.get('/all')
def get_all_specifications() -> Response:
    return make_response(jsonify(specifications_controller.find_all()), HTTPStatus.OK)


@specifications_bp.get('/<int:specifications_id>')
def get_specifications(specifications_id: int) -> Response:
    return make_response(jsonify(specifications_controller.find_by_id(specifications_id)), HTTPStatus.OK)


@specifications_bp.get('/<int:specifications_id>/panel')
def get_panel_by_specifications(specifications_id) -> Response:
    return make_response(
        jsonify(specifications_controller.find_panel_by_specifications(specifications_id)), HTTPStatus.OK)


@specifications_bp.post('')
def create_specifications() -> Response:
    content = request.get_json()
    specifications = Specifications.create_from_dto(content)
    specifications_controller.create(specifications)
    return make_response(jsonify(specifications.put_into_dto()), HTTPStatus.CREATED)


@specifications_bp.post('/<int:specifications_id>/add_panel')
def add_panel_to_specifications(specifications_id) -> Response:
    try:
        data = request.get_json()
        panel_id = data.get('interactive_advertising_panel_id')

        specifications_controller.add_panel_to_specifications(specifications_id, panel_id)

        return make_response(jsonify({"message": "Panel added successfully"}), HTTPStatus.OK)

    except Exception as e:
        return make_response(jsonify({"error": str(e)}), HTTPStatus.INTERNAL_SERVER_ERROR)


@specifications_bp.put('/<int:specifications_id>')
def update_specifications(specifications_id: int) -> Response:
    content = request.get_json()
    specifications = Specifications.create_from_dto(content)
    specifications_controller.update(specifications_id, specifications)
    return make_response("Specifications updated", HTTPStatus.OK)


@specifications_bp.patch('/<int:specifications_id>/remove_panel')
def remove_panel_from_specifications(specifications_id) -> Response:
    try:
        data = request.get_json()
        panel_id = data.get('interactive_advertising_panel_id')

        specifications_controller.remove_panel_from_specifications(specifications_id, panel_id)

        return make_response(jsonify({"message": "Panel removed successfully"}), HTTPStatus.OK)

    except Exception as e:
        return make_response(jsonify({"error": str(e)}), HTTPStatus.INTERNAL_SERVER_ERROR)


@specifications_bp.patch('/<int:specifications_id>')
def patch_specifications(specifications_id: int) -> Response:
    content = request.get_json()
    specifications_controller.patch(specifications_id, content)
    return make_response("Specifications updated", HTTPStatus.OK)


@specifications_bp.delete('/<int:specifications_id>')
def delete_specifications(specifications_id: int) -> Response:
    specifications_controller.delete(specifications_id)
    return make_response("Specifications deleted", HTTPStatus.OK)
