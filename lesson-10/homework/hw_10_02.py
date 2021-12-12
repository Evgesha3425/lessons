from hw_10_01 import Circle, Square, Triangle

# s - square
# c - circle
# t - triangle

if __name__ == "__main__":
    s = Square(1, 5, 2, 5)
    c = Circle(5)
    t = Triangle(1, 2, 3, 3, 1, 2)

    list_figures = [s, c, t]
    summ = 0

    for i in list_figures:
        if i == s:
            summ += i.area_square()
            print(f"Площадь квадрата: {i.area_square()}")

        if i == c:
            summ += i.area_circle()
            print(f"Площадь круга: {i.area_circle()}")

        if i == t:
            summ += i.area_triangle()
            print(f"Площадь треугольника: {i.area_triangle()}")

    print(f"Площадь фигур: {summ}")