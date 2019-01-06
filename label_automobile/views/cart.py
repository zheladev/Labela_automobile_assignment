from pyramid.view import view_defaults, view_config
from pyramid.response import Response
from label_automobile.services.cart import CartService

@view_defaults(renderer="json")
class CartView:
    def __init__(self, request):
        self.request = request
        self.session = request.dbsession
        self.service = CartService(self.session, self.request.session)

    @view_config(route_name="cart.add_to_cart")
    def add_to_cart(self):
        vendor_id = self.request.params.get('vid', None)
        self.service.add_product_to_cart(vendor_id, 1)
        cart = self.service.get_cart()
        return cart

    @view_config(route_name="cart.remove_from_cart")
    def remove_from_cart(self):
        vendor_id = self.request.params.get('vid', None)
        self.service.remove_product_from_cart(vendor_id, 1)
        cart = self.service.get_cart()
        return cart

    @view_config(route_name="cart.empty_cart")
    def empty_cart(self):
        self.service.empty_cart()  
        cart = self.service.get_cart()
        return cart
