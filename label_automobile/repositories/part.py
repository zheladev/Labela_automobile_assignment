from label_automobile.models.part import Part

class PartRepository:
    def __init__(self, session):
        self.session = session
        self.model = Part

    
    def find_by_vendor_id(self, vendor_id):
        return self.session.query(Part).filter(
            Part.vendor_id == vendor_id).first()

    def get_all(self):
        return self.session.query(Part).all()

    def add(self, name, price, vendor_id, details):
        part = Part()
        part.name = name
        part.price = price
        part.vendor_id = vendor_id
        part.details = details
        self.session.add(part)
        return part

    def delete(self, vendor_id):
        part = self.find_by_vendor_id(vendor_id)
        if not (part is None):
            self.session.delete(part)

