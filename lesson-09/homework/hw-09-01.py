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
        self.speed_increase = self.speed + 5
        print(f"increase speed {self.speed_increase}")

    def reduce_speed(self):
        self.speed_reduce = self.speed - 5
        print(f"reduce speed {self.speed_reduce}")

    def stop(self):
        self.speed_stop = 0
        print(f"stop {self.speed_stop}")

    def current_speed(self):
        self.speed_current = self.speed
        print(f"current speed {self.speed_current}")

    def reverse(self):
        print(f"reverse -{self.speed}")


if __name__ == "__main__":
    my_car = Car("Toyota", "Camry", 2017, 30)

    my_car.increase_speed()
    my_car.reduce_speed()
    my_car.stop()
    my_car.current_speed()
    my_car.reverse()



