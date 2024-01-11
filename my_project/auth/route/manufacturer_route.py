from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from my_project.auth.controller import manufacturer_controller

manufacturer_bp = Blueprint('manufacturer', __name__, url_prefix='/manufacturer')


@manufacturer_bp.get('/all')
def get_all_manufacturers() -> Response:
    return make_response(jsonify(manufacturer_controller.find_all()), HTTPStatus.OK)


@manufacturer_bp.get('/<int:manufacturer_id>')
def get_manufacturer(manufacturer_id: int) -> Response:
    return make_response(jsonify(manufacturer_controller.find_by_id(manufacturer_id)), HTTPStatus.OK)


@manufacturer_bp.get('/<int:manufacturer_id>/supermarkets')
def get_supermarket_by_manufacturer(manufacturer_id: int):
    return make_response(jsonify(manufacturer_controller.get_supermarkets_for_manufacturer(manufacturer_id)),
                         HTTPStatus.OK)


@manufacturer_bp.post('/<int:manufacturer_id>/add_supermarket')
def connect_manufacturer_and_supermarket_from_manufacturer(manufacturer_id: int):
    try:
        data = request.get_json()
        supermarket_id = data.get('supermarket_id')
        manufacturer_controller.connect_manufacturer_and_supermarket_from_manufacturer(manufacturer_id, supermarket_id)
        return make_response(jsonify({"message": "supermarket added successfully"}), HTTPStatus.OK)
    except Exception as e:
        return make_response(jsonify({"error": str(e)}), HTTPStatus.INTERNAL_SERVER_ERROR)


@manufacturer_bp.post('/add_manufacture_supermarket')
def insert_in_supermarket_has_manufacturer_by_values() -> Response:
    content = request.get_json()
    manufacturer_name = content.get('manufacturer_name')
    supermarket_name = content.get('supermarket_name')
    if any(arg is None for arg in [manufacturer_name, supermarket_name]):
        return make_response(jsonify({"error": "Missing required fields"}), HTTPStatus.BAD_REQUEST)
    try:
        manufacturer_controller.insert_in_supermarket_has_manufacturer_by_values(manufacturer_name, supermarket_name)
        return make_response(jsonify({"message": "successful connecting"}), HTTPStatus.CREATED)
    except Exception as e:
        return make_response(jsonify({"error": str(e)}), HTTPStatus.INTERNAL_SERVER_ERROR)


@manufacturer_bp.patch('/<int:manufacturer_id>/remove_supermarket')
def remove_supermarket_from_manufacturer(manufacturer_id) -> Response:
    try:
        data = request.get_json()
        supermarket_id = data.get('supermarket_id')
        manufacturer_controller.remove_supermarket_from_manufacturer(manufacturer_id, supermarket_id)
        return make_response(jsonify({"message": "Supermarket removed successfully"}), HTTPStatus.OK)
    except Exception as e:
        return make_response(jsonify({"error": str(e)}), HTTPStatus.INTERNAL_SERVER_ERROR)
