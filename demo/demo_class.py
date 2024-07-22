class Car:
    def __init__(self, color, engine_type):
        self.color = color
        self.engine_type = engine_type
        self.speed = 0
        self.is_start = False

    def __repr__(self):
        return f'This is'

    def __str__(self):
        return f'This has a {self.color} color and a {self.engine_type} engine type.'

    def start_engine(self):
        self.speed = 0
        self.is_start = True

    def speed_up(self, speed):
        self.speed += speed

    def speed_down(self, speed):
        self.speed -= speed


if __name__ == "__main__":
    car = Car(color="Blue", engine_type="Electric")
    print(car)
    print(__name__)
