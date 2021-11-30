my_string = input("Введите строку: ")
new_string = lambda string: [letter for letter in string if letter < "и"]
print("".join(new_string(my_string)))