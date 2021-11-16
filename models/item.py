class Item:

    def __init__(self, name, brand, description, stock_quantity, buying_cost, selling_price, id = None):
        self.name = name
        self.brand = brand
        self.description = description
        self.stock_quantity = stock_quantity
        self.buying_cost = buying_cost
        self.selling_price = selling_price
        self.id = id

    def markup(item):
        markup = ((item.selling_price - item.buying_cost) / item.buying_cost) * 100
        return round(markup, 1)