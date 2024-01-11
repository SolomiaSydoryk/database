from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from my_project.auth.controller import address_controller
from my_project.auth.domain import Address

address_bp = Blueprint('address', __name__, url_prefix='/address')


@address_bp.get('/all')
def get_all_address() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    return make_response(jsonify(address_controller.find_all()), HTTPStatus.OK)


@address_bp.get('/<int:address_id>')
def get_address(address_id: int) -> Response:
    """
    Gets address by ID.
    :return: Response object
    """
    return make_response(jsonify(address_controller.find_by_id(address_id)), HTTPStatus.OK)


@address_bp.get('/<int:address_id>/supermarket')
def get_supermarket_by_address(address_id) -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    return make_response(
        jsonify(address_controller.find_supermarket_by_adress(address_id)), HTTPStatus.OK)


@address_bp.post('')
def create_address() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    content = request.get_json()
    address = Address.create_from_dto(content)
    address_controller.create(address)
    return make_response(jsonify(address.put_into_dto()), HTTPStatus.CREATED)


@address_bp.post('/<int:address_id>/add_supermarket')
def add_address_to_supermarket(address_id) -> Response:
    try:
        data = request.get_json()
        supermarket_id = data.get('supermarket_id')

        address_controller.add_supermarket_to_address(address_id, supermarket_id)

        return make_response(jsonify({"message": "Supermarket added successfully"}), HTTPStatus.OK)

    except Exception as e:
        return make_response(jsonify({"error": str(e)}), HTTPStatus.INTERNAL_SERVER_ERROR)


@address_bp.put('/<int:address_id>')
def update_address(address_id: int) -> Response:
    content = request.get_json()
    address = Address.create_from_dto(content)
    address_controller.update(address_id, address)
    return make_response("Address updated", HTTPStatus.OK)


@address_bp.patch('/<int:address_id>/remove_supermarket')
def remove_address_from_supermarket(address_id) -> Response:
    try:
        data = request.get_json()
        supermarket_id = data.get('supermarket_id')

        # Call the controller method to remove the address from the supermarket
        address_controller.remove_supermarket_from_address(address_id, supermarket_id)

        return make_response(jsonify({"message": "Supermarket removed successfully"}), HTTPStatus.OK)

    except Exception as e:
        return make_response(jsonify({"error": str(e)}), HTTPStatus.INTERNAL_SERVER_ERROR)


@address_bp.patch('/<int:address_id>')
def patch_address(address_id: int) -> Response:
    """
    Patches address by ID.
    :return: Response object
    """
    content = request.get_json()
    address_controller.patch(address_id, content)
    return make_response("Address updated", HTTPStatus.OK)


@address_bp.delete('/<int:address_id>')
def delete_address(address_id: int) -> Response:
    """
    Deletes address by ID.
    :return: Response object
    """
    address_controller.delete(address_id)
    return make_response("Address deleted", HTTPStatus.OK)
