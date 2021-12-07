"""
Создать класс Car. Атрибуты: марка, модель, год выпуска, скорость (по умолчанию 0).
Методы: увеличить скорости (скорость +5), уменьшение скорости (скорость -5),
стоп (сброс скорости на 0), отображение скорости, задния ход (изменение знака скорости).
"""


class Car:
    def __init__(self, brand, model, year, speed):
        # атрибуты(свойства)
        self.brand = brand
        self.model = model
        self.year = year
        self.speed = speed

    # методы
    def increase_speed(self):
        self.speed += 5

    def reduce_speed(self):
        self.speed -= 5

    def stop(self):
        self.speed = 0

    def current_speed(self):
        print(f"Your speed: {self.speed} km/h")

    def reverse(self):
        self.speed *= -1


if __name__ == "__main__":
    my_car = Car("Toyota", "Camry", 2017, 0)

    my_car.increase_speed()
    my_car.reduce_speed()
    my_car.stop()
    my_car.current_speed()
    my_car.reverse()



