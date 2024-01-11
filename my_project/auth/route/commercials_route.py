from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response

from my_project.auth.controller import commercials_controller
from my_project.auth.domain import Commercials

commercials_bp = Blueprint('commercials', __name__, url_prefix='/commercials')


@commercials_bp.get('')
def get_all_commercials() -> Response:
    return make_response(jsonify(commercials_controller.find_all()), HTTPStatus.OK)


@commercials_bp.get('/<int:interactive_advertising_panel_id>')
def get_commercials(commercials_id: int) -> Response:
    return make_response(jsonify(commercials_controller.find_by_id(commercials_id)),
                         HTTPStatus.OK)


@commercials_bp.get('/<int:commercials_id>/panel')
def get_panel_by_commercials(commercials_id: int):
    return make_response(jsonify(commercials_controller.get_panel_by_commercials(commercials_id)),
                         HTTPStatus.OK)


@commercials_bp.post('')
def create_commercials() -> Response:
    content = request.get_json()
    obj = Commercials.create_from_dto(content)
    commercials_controller.create(obj)
    return make_response(jsonify(obj.put_into_dto()), HTTPStatus.CREATED)


@commercials_bp.put('/<int:commercials_id>')
def update_commercials(commercials_id: int) -> Response:
    content = request.get_json()
    obj = Commercials.create_from_dto(content)
    commercials_controller.update(commercials_id, obj)
    return make_response("Commercials updated", HTTPStatus.OK)


@commercials_bp.patch('/<int:commercials_id>')
def patch_commercials(commercials_id: int) -> Response:
    content = request.get_json()
    commercials_controller.patch(commercials_id, content)
    return make_response("Commercials updated", HTTPStatus.OK)


@commercials_bp.delete('/<int:commercials_id>')
def delete_commercials(commercials_id: int) -> Response:
    commercials_controller.delete(commercials_id)
    return make_response("Commercials deleted", HTTPStatus.OK)
