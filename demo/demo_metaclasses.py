class Car(object):
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

    def __repr__(self):
        return f"Brand: {self.brand}, Color: {self.color}"


# Create our Metaclass
class Meta(type):
    def __new__(self, name, attrs):
        attrs['shape'] = 'sendan'
        return type(name, (Car, ), attrs)


EVCar = Meta('EVCar', {})

# Create Instance of EVCar class
lucid = EVCar('Lucid', 'Yellow')
print(lucid)
print(lucid.shape)
