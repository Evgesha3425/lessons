"""
Переопределить магические методы сложения, вычитания, умножения на число.
"""

from __future__ import annotations
from cw_10_01 import MyTime


class MyTimeMath(MyTime):
    def __add__(self, other: MyTimeMath) -> MyTimeMath:
        seconds = self.seconds + other.seconds
        minutes_offset = 0
        if seconds > 60:
            minutes_offset = seconds // 60
            seconds %= 60

        minutes = self.minutes + other.minutes + minutes_offset
        hours_offset = 0
        if minutes > 60:
            hours_offset = minutes // 60
            minutes %= 60

        hours = self.hours + other.hours + hours_offset
        return MyTimeMath(hours, minutes, seconds)

    def __sub__(self, other: MyTimeMath) -> MyTimeMath:
        seconds = self.seconds - other.seconds
        minutes_offset = 0
        if seconds < 0:
            minutes_offset = abs(seconds // 60)
            seconds = abs(seconds % 60)

        minutes = self.minutes - other.minutes - minutes_offset
        hours_offset = 0
        if minutes < 0:
            hours_offset = abs(minutes // 60)
            minutes = abs(minutes % 60)

        hours = self.hours - other.hours - hours_offset
        return MyTimeMath(hours, minutes, seconds)

    def __mul__(self, multiplier: int) -> MyTimeMath:
        seconds = self.seconds * multiplier
        minutes_offset = 0
        if seconds > 60:
            minutes_offset = seconds // 60
            seconds %= 60

        minutes = self.minutes * multiplier + minutes_offset
        hours_offset = 0
        if minutes > 60:
            hours_offset = minutes // 60
            minutes %= 60

        hours = self.hours * multiplier + hours_offset
        return MyTimeMath(hours, minutes, seconds)

if __name__ == "__main__":
    my_time_1 = MyTimeMath(2, 50, 40)
    my_time_2 = MyTimeMath(1, 32, 27)

    my_time_3 = my_time_1 - my_time_2 + MyTimeMath(7, 45, 0)
    print(my_time_3)

    # print(my_time_1 + my_time_2)
    # #print(my_time_1 - my_time_2)
    # print(my_time_2 - my_time_1)
    # print(my_time_1 * 2)