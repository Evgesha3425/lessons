years_earth = int(input("Введите количество земных лет: "))
years_mars = lambda years_earth: years_earth * 365 // 687
print(years_mars(years_earth))

