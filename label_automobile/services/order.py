from ..repositories.order import OrderRepository


class OrderService:
    def __init__(self, session):
        self._repository = OrderRepository(session)

    def find_by_user_id(self, user_id):
        user_orders = self._repository.find_by_user_id(user_id)
        #TODO - Serialize into JSOn
        return user_orders

    def get_all(self):
        orders = self._repository.get_all()
        #TODO - Serialize into JSON

        return orders

    def find_by_order_id(self, order_id):
        order = self._repository.find_by_order_id(order_id)
        #TODO - Serialize into JSON

    def add(self, user_id, date, cart):
        order = self._repository.add(user_id, date, cart)    
        return order

    def delete(self, order_id):
        self._repository.delete(order_id)
        #TODO - return boolean value representing whether order has been deleted successfully