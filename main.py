from datetime import datetime

from demo.demo_class import Car

tesla = Car(color="green", engine_type="electric")

tesla.start_engine()

for i in range(1, 5):
    tesla.speed_up(1)
    print(tesla.speed)


def higher_order_example(func):
    def inside():
        print("start ...")
        func()
        print("end ...")

    return inside


@higher_order_example
def sample_example():
    print("I am inside")


sample_example()

now = datetime.now()
print(f"{now.year}, {now.month}, {now.day}")
strptime = datetime.strptime("2022-01-01 10:10:10", "%Y-%m-%d %H:%M:%S")
print(f"{strptime}. type:{type(strptime)}")
