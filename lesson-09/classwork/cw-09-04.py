"""
Создать общий класс Animal, содержащий все общие методы классов Dog и Cat.
Унаследовать Dog и Cat от класса Animal и Удалить в дочерних классах те методы,
которые имеются у родительского класса. Создать объект каждого класса и вызвать все его методы.
"""


class Animal:
    def __init__(self, height, weight, name, age):
        self.height = height
        self.weight = weight
        self.name = name
        self.age = age

    def jump(self):
        print(f"Jump {self.name}")

    def run(self):
        print(f"run {self.name}")


class Dog(Animal):
    def bark(self):
        print(f"bark {self.name}")


class Cat(Animal):
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

    dog_bob = Dog(100, 100, "Bob", 10)
    dog_bob.jump()
    dog_bob.run()
    dog_bob.bark()

    print(dog_bob.name)
    print(dog_bob.height)
    print(dog_bob.weight)
    print(dog_bob.age)