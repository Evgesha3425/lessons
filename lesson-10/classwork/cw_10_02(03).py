"""
Переопределить магические методы сложения, вычитания, умножения на число.
"""

from __future__ import annotations
from cw_10_01 import MyTime


class MyTimeMath(MyTime):
    def __add__(self, other: MyTimeMath) -> MyTimeMath:
        self.seconds += other.seconds
        minutes_offset = 0
        if self.seconds > 60:
            minutes_offset = self.seconds // 60
            self.seconds %= 60

        self.minutes += other.minutes + minutes_offset
        hours_offset = 0
        if self.minutes > 60:
            hours_offset = self.minutes // 60
            self.minutes %= 60

        self.hours += other.hours + hours_offset
        return self


if __name__ == "__main__":
    my_time_1 = MyTimeMath(2, 50, 40)
    my_time_2 = MyTimeMath(1, 32, 27)

    print(my_time_1 + my_time_2)