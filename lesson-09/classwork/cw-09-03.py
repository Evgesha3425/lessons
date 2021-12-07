"""
Создать новый класс Cat, который имеет все те же атрибуты что и Dog, только заменить метод bark на meow.
"""


class Cat:
    def __init__(self, height, weight, name, age):
        self.height = height
        self.weight = weight
        self.name = name
        self.age = age

    def jump(self):
        print(f"Jump {self.name}")

    def run(self):
        print(f"run {self.name}")

    def meow(self):
        print(f"meow {self.name}")


if __name__ == "__main__":
    cat_pushok = Cat(50, 30, "Pushok", 3)
    cat_pushok.jump()
    cat_pushok.run()
    cat_pushok.meow()

    print(cat_pushok.name)
    print(cat_pushok.height)
    print(cat_pushok.weight)
    print(cat_pushok.age)