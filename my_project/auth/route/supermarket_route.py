from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from my_project.auth.controller import supermarket_controller

supermarket_bp = Blueprint('supermarket', __name__, url_prefix='/supermarket')


@supermarket_bp.get('/all')
def get_all_supermarkets() -> Response:
    return make_response(jsonify(supermarket_controller.find_all()), HTTPStatus.OK)


@supermarket_bp.get('/<int:supermarket_id>')
def get_supermarket(supermarket_id: int) -> Response:
    return make_response(jsonify(supermarket_controller.find_by_id(supermarket_id)), HTTPStatus.OK)


@supermarket_bp.get('/<int:supermarket_id>/address')
def get_address_for_supermarket(supermarket_id: int) -> Response:
    return make_response(jsonify(supermarket_controller.get_address_for_supermarket(supermarket_id)), HTTPStatus.OK)


@supermarket_bp.get('/<int:supermarket_id>/manufacturers')
def get_manufacturers_for_supermarket(supermarket_id: int):
    return make_response(jsonify(supermarket_controller.get_manufacturers_for_supermarket(supermarket_id)),
                         HTTPStatus.OK)


@supermarket_bp.post('/<int:supermarket_id>/add_manufacturer')
def connect_manufacturer_and_supermarket_from_supermarket(supermarket_id: int):
    try:
        data = request.get_json()
        manufacturer_id = data.get('manufacturer_id')
        supermarket_controller.connect_manufacturer_and_supermarket_from_supermarket(manufacturer_id, supermarket_id)
        return make_response(jsonify({"message": "Manufacturer added successfully"}), HTTPStatus.OK)
    except Exception as e:
        return make_response(jsonify({"error": str(e)}), HTTPStatus.INTERNAL_SERVER_ERROR)


@supermarket_bp.post('/add_manufacture_supermarket')
def insert_in_supermarket_has_manufacturer_by_values() -> Response:
    content = request.get_json()
    manufacturer_name = content.get('manufacturer_name')
    supermarket_name = content.get('supermarket_name')
    if any(arg is None for arg in [manufacturer_name, supermarket_name]):
        return make_response(jsonify({"error": "Missing required fields"}), HTTPStatus.BAD_REQUEST)
    try:
        supermarket_controller.insert_in_supermarket_has_manufacturer_by_values(manufacturer_name, supermarket_name)
        return make_response(jsonify({"message": "successful connecting"}), HTTPStatus.CREATED)
    except Exception as e:
        return make_response(jsonify({"error": str(e)}), HTTPStatus.INTERNAL_SERVER_ERROR)


@supermarket_bp.patch('/<int:supermarket_id>/remove_manufacturer')
def remove_manufacturer_from_supermarket(supermarket_id) -> Response:
    try:
        data = request.get_json()
        manufacturer_id = data.get('manufacturer_id')
        supermarket_controller.remove_manufacturer_from_supermarket(manufacturer_id, supermarket_id)
        return make_response(jsonify({"message": "Manufacturer removed successfully"}), HTTPStatus.OK)
    except Exception as e:
        return make_response(jsonify({"error": str(e)}), HTTPStatus.INTERNAL_SERVER_ERROR)
