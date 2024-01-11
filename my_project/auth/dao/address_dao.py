from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain import Address
from my_project.auth.domain import Supermarket


class AddressDAO(GeneralDAO):
    """
    Realisation of Address data access layer.
    """
    _domain_type = Address

    def find_supermarket_by_adress(self, address_id):
        session = self.get_session()
        supermarket = session.query(Supermarket).filter_by(address_id=address_id).first()
        address = session.query(Address).filter_by(id=address_id).first()
        data = {"Address": address.put_into_dto(),
                "Supermarket": supermarket.put_into_dto()}
        return data
