"""
Пользователь делает вклад в размере 2130 рублей сроком на 5 лет под 10% годовых
(каждый год размер его вклада увеличивается на 10%. Эти деньги прибавляются к сумме вклада,
и на них в следующем году тоже будут проценты). Рассчитать сумму на счету пользователя по
окончании вклада и вывести на печать, если в конце каждого года ему начисляется бонус
в размере 120 рублей.
"""

sum = 2130
years = 5
percent = 0.1
bonus = 120
while years != 0:
    sum = sum + sum * percent + bonus
    years -= 1
print(sum)