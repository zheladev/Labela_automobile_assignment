from pyramid.view import view_defaults, view_config
from pyramid.response import Response
from label_automobile.models.part import Part
from label_automobile.services.part import PartService

@view_defaults(renderer="json")
class PartView:
    def __init__(self, request):
        self.request = request
        self.session = request.dbsession

    @view_config(route_name='part.list')
    def list(self):
        service = PartService(self.session)
        parts = service.get_all()
        return parts

    @view_config(route_name="part.find_by_vendor_id")
    def get_by_vendor_id(self):
        vendor_id = self.request.params.get('vid', None)
        service = PartService(self.session)
        part = service.find_by_vendor_id(vendor_id)

        return part

    @view_config(route_name="part.add_part")
    def add_part(self):
        service = PartService(self.session)
        new_part = service.add("APIpart", 2039.43, "a8234D", "Part added with api")

        return new_part

    @view_config(route_name="part.delete_part")
    def delete_part(self):
        service = PartService(self.session)
        service.delete("a8234D")

        return {"deleted": "rest in peace, car  piece"}