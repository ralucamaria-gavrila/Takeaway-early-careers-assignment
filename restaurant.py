class Restaurant:
    def __init__(self, name: str = "", address: str = "", cuisine: list = None, rating: float = 0.0):
        self.name = name
        self.address = address
        self.cuisine = cuisine if cuisine is not None else []
        self.rating = rating

