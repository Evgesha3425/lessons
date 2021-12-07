"""
Создать программу, которая импортирует класс из предыдущей задачи, создает объект и при
инициализации устанавливает марку Mercedes, модель E500, год выпуска 2000. Далее “разгоняет”
машину до 100 км/ч и выводит скорость на экран.
"""

from hw_09_01 import Car


if __name__ == "__main__":
    alexandrs_car = Car("Mercedes", "E500", 2000, 0)

    while alexandrs_car.speed < 100:
        alexandrs_car.increase_speed()
        alexandrs_car.current_speed()

