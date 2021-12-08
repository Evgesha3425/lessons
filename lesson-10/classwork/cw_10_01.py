"""
Создать класс MyTime. Атрибуты: hours, minutes, seconds. Методы: переопределить магические
методы сравнения (==, !=, >=, <=, <, >).
"""


class MyTime:
    def __init__(self, hours: int, minutes: int, seconds: int):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def __eq__(self, other) -> bool:
        return (
                self.hours == other.hours and
                self.minutes == other.minutes and
                self.seconds == other.seconds
                )

    def __ne__(self, other) -> bool:
        return not self.__eq__(other)

    def __ge__(self, other) -> bool:
        return (
                self.hours >= other.hours or
                self.minutes >= other.minutes or
                self.seconds >= other.seconds
                )

    def __le__(self, other) -> bool:
        return not self.__ge__()

    def __gt__(self, other) -> bool:
        return (
                self.hours > other.hours or
                self.minutes > other.minutes or
                self.seconds > other.seconds
        )

    def __lt__(self, other) -> bool:
        return not self.__gt__()


if __name__ == "__main__":
    my_time_1 = MyTime(1, 2, 3)
    my_time_2 = MyTime(1, 2, 3)
    my_time_3 = MyTime(2, 3, 4)


    print(my_time_1 == my_time_2)
    #Следующие две записи абсолютно равнозначны
    print(my_time_1 == my_time_3)
    print(my_time_1.__eq__(my_time_3))

