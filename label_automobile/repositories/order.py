from label_automobile.models.order import Order, Order

class OrderRepository:
    def __init__(self, session):
        self.session = session
        self.model = Order
        self.schema = Order

    
    def find_by_user_id(self, user_id):
        return self.session.query(Order).filter(
            Order.user_id == user_id).all()

    def get_all(self):
        return self.session.query(Order).all()

    def find_by_order_id(self, order_id):
        return self.session.query(Order).filter(
            Order.id == order_id).first()

    def add(self, user_id, date, cart):
        order = Order()
        order.user_id = user_id
        order.delivery_date = date
        self.session.add(order)

        #TODO - create order_line for each product in cart

        return order

    def delete(self, order_id):
        order = self.find_by_order_id(order_id)
        if not (order is None):
            self.session.delete(order) #TODO - Not sure if it cascades on order_line