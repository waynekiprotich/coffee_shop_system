class Order:

    def __init__(self, order_id, phone, coffee, size, price):
        self.order_id = order_id
        self.phone = phone
        self.coffee = coffee
        self.size = size
        self.price = price


    def to_dict(self):
        return {
            "order_id": self.order_id,
            "phone": self.phone,
            "coffee": self.coffee,
            "size": self.size,
            "price": self.price
        }