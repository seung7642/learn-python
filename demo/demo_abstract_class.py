from typing import List, Protocol


class Item(Protocol):
    quantity: float
    price: float


class Product:
    def __init__(self, name: str, quantity: float, price: float):
        self.name = name
        self.quantity = quantity
        self.price = price


class Stock:
    def __init__(self, product_name, quantity, price):
        self.product_name = product_name
        self.quantity = quantity
        self.price = price


def calculate_total(items: List[Item]) -> float:
    return sum([item.quantity * item.price for item in items])


total = calculate_total([
    Product('A', 10, 150),
    Stock('B', 5, 250)
])

print(total)
