"""
Ввести с клавиатуры целое число n. Получить сумму кубов всех целых чисел от 1 до n (включая n) используя цикл while.
"""

n = int(input("Enter number: "))

index = 0
result = 0

while index <= n:
    result = result + index ** 3
    index += 1

print(result)