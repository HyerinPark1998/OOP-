
# --------------------------------
# Animal

class Animal():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        pass


class Dog(Animal):
    def speak(self):
        self.speak = '멍멍'
        return self.speak


class Cat(Animal):
    def speak(self):
        self.speak = '야옹'
        return self.speak


mycat = Cat('나비', 10)
print(mycat.speak())


# --------------------------------
# Shape

class Shape():
    def __init__(self):
        pass

    def get_area(self):
        return self.area


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        return self.radius ** 2 * 3.14


class Rectangle(Shape):
    def __init__(self, length, widht):
        self.length = length
        self.widht = widht

    def get_area(self):
        return self.length * self.widht


a = Rectangle(5, 10)
print(a.get_area())


# --------------------------------
# Car
class Car():
    def __init__(self, model, color, speed):
        self.model = model
        self.color = color
        self.speed = speed

    def accelerate(self, plus):
        self.speed += plus

    def brake(self, minus):
        self.speed -= minus

    def get_speed(self):
        return self.speed


mycar = Car('sonata', 'black', 50)
mycar.brake(20)
print(mycar.get_speed())
