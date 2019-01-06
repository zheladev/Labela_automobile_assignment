from ..repositories.part import PartRepository
from ..schemas.part import PartSchema

class PartService:
    def __init__(self, session):
        self._repository = PartRepository(session)
        self._schema = PartSchema()

    def find_by_vendor_id(self, vendor_id):
        """
        Find part by its vendor_id
        :param vendor_id: int a part's vendor id
        :return: str: json-formatted string containing the information regarding the part with vendor_id
        """
        part = self._repository.find_by_vendor_id(vendor_id)

        return self._schema.dump(part).data

    def get_all(self):
        """
        Returns name, price and vendor_id of every part in the database
        :return: str: json-formatted string containing data regarding every part in the database
        """
        parts = self._repository.get_all()
        return self._schema.dump(parts, many=True) #TODO - Fix up serialization
        

    def add(self, name, price, vendor_id, details):
        """
        Adds a part to the database
        :param name: str name of the part
        :param price: float price of the part
        :param vendor_id: str vendor's part id
        :param details: str parts details
        :return: str: json-formatted string containing data of the part that was just added to the database
        """
        new_part = self._repository.add(name, price, vendor_id, details)
        return self._schema.dump(new_part)

    def delete(self, vendor_id):
        """
        Removes part from the database
        :param name: str name of the part
        :param price: float price of the part
        :param vendor_id: str vendor's part id
        :param details: str parts details
        """
        self._repository.delete(vendor_id)