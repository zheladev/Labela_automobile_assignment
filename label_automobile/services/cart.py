from ..models import Order, Order_line
from .order import OrderService


class CartService:
    def __init__(self, dbsession, session):
        self._dbsession = dbsession #request.dbsession
        self._session = session #request.session
    def add_product_to_cart(self, vendor_id, num = 1):
        """
        Creates cart in current session if no cart is found, and adds any number of vendor_id parts to it
        :param vendor_id: str a part's vendor id.
        :param num: int number of items to add to cart, by default adds one.
        """
        #TODO - cart dictionary saves keys as  '"key"' instead of 'key' for some reason ej. {'cart': {'"key"': 2}}
        _s = self._session
        if 'cart' in _s:
            #cart exists
            if vendor_id in _s['cart']: 
                #product already in cart
                _s['cart'][vendor_id] += num
            else:
                #product not in cart
                _s['cart'][vendor_id] = num
        else:
            #cart doesn't exist
            _s['cart'] = {vendor_id : num}
            

    def remove_product_from_cart(self, vendor_id, num = 1):
        """
        Removes any number of vendor_id parts from cart
        :param vendor_id: str a part's vendor id.
        :param num: int number of items to remove from cart, by default adds one.
        """
        _s = self._session
        if 'cart' in _s and vendor_id in _s['cart']:
            if _s['cart'][vendor_id] > num:
                _s['cart'][vendor_id] -= num
            else:
                _s['cart'].pop(vendor_id)

    def empty_cart(self):
        _s = self._session
        if 'cart' in _s:
            del _s['cart']

    def order_cart(self, user_id, date):
        service = OrderService(self._dbsession)
        #TODO - doesn't work just yet
        service.add(user_id, date, self._session)

    def get_cart(self):
        return self._session['cart'] if 'cart' in self._session else None