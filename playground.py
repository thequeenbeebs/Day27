def add(*args):
    total = 0
    for n in args:
        total += n
    return total


print(add(1, 5, 8, 9, 10))

# kwargs are a dictionary


def calculate(n, **kwargs):
    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)
    n += kwargs["add"]
    n *= kwargs['multiply']
    print(n)


calculate(2, add=3, multiply=5)


class Car:

    def __init__(self, **kwargs):
        # get - if key doesn't exist it will just = None
        self.make = kwargs.get('make')
        self.model = kwargs.get('model')
        self.color = kwargs.get('color')
        self.seats = kwargs.get('seats')


my_car = Car(make="Nissan", model="GT-R")
print(my_car.make)






