class Variable:

    def __init__(self, name, points, price):
        """
        Variable object that keeps track of price and points
        :param name: Name of driver or team
        :param points: Points that the driver or team scored
        :param price: Price of the driver or team
        """
        self.name = name
        self.points = points
        self.price = price
