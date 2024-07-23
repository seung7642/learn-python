import inspect
from dataclasses import dataclass, astuple, asdict, replace, field
from pprint import pprint
from typing import List


@dataclass(frozen=True)
class Car:
    id: int
    color: str = ""
    brand: str = ""
    tire_wear: List[float] = field(default_factory=lambda: [1.0, 1.0, 1.0, 1.0])


pprint(inspect.getmembers(Car, inspect.isfunction))

car = Car(1, 'WHITE', 'TESLA')
print(car)
print(f"Copy immutable car object : {replace(car, id=2)}")
print(f"Convert car object to tuple : {astuple(car)}")
print(f"Convert car object to dictionary : {asdict(car)}")
