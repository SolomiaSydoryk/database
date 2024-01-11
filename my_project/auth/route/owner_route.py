from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from my_project.auth.controller import owner_controller
from my_project.auth.domain import Owner

owner_bp = Blueprint('owner', __name__, url_prefix='/owner')


@owner_bp.get('/all')
def get_all_owners() -> Response:
    return make_response(jsonify(owner_controller.find_all()), HTTPStatus.OK)


@owner_bp.get('/<int:owner_id>')
def get_owner(owner_id: int) -> Response:
    return make_response(jsonify(owner_controller.find_by_id(owner_id)), HTTPStatus.OK)


@owner_bp.get('/<int:owner_id>/supermarket')
def get_supermarket_by_owner(owner_id) -> Response:
    return make_response(
        jsonify(owner_controller.get_supermarket_by_owner(owner_id)), HTTPStatus.OK)


@owner_bp.post('')
def create_owner() -> Response:
    content = request.get_json()
    owner = Owner.create_from_dto(content)
    owner_controller.create(owner)
    return make_response(jsonify(owner.put_into_dto()), HTTPStatus.CREATED)


@owner_bp.post('/<int:owner_id>/add_panel')
def add_supermarket_to_owner(owner_id) -> Response:
    try:
        data = request.get_json()
        supermarket_id = data.get('supermarket_id')

        owner_controller.add_supermarket_to_owner(owner_id, supermarket_id)

        return make_response(jsonify({"message": "Supermarket added successfully"}), HTTPStatus.OK)

    except Exception as e:
        return make_response(jsonify({"error": str(e)}), HTTPStatus.INTERNAL_SERVER_ERROR)


@owner_bp.put('/<int:owner_id>')
def update_owner(owner_id: int) -> Response:
    content = request.get_json()
    owner = Owner.create_from_dto(content)
    owner_controller.update(owner_id, owner)
    return make_response("Owner updated", HTTPStatus.OK)


@owner_bp.patch('/<int:owner_id>/remove_supermarket')
def remove_supermarket_from_owner(owner_id) -> Response:
    try:
        data = request.get_json()
        supermarket_id = data.get('supermarket_id')

        owner_controller.remove_panel_from_section(owner_id, supermarket_id)

        return make_response(jsonify({"message": "Supermarket removed successfully"}), HTTPStatus.OK)

    except Exception as e:
        return make_response(jsonify({"error": str(e)}), HTTPStatus.INTERNAL_SERVER_ERROR)


@owner_bp.patch('/<int:owner_id>')
def patch_section(owner_id: int) -> Response:
    content = request.get_json()
    owner_controller.patch(owner_id, content)
    return make_response("Owner updated", HTTPStatus.OK)


@owner_bp.delete('/<int:owner_id>')
def delete_section(owner_id: int) -> Response:
    owner_controller.delete(owner_id)
    return make_response("Owner deleted", HTTPStatus.OK)
