"""
Напишите программу, которая принимает текст и выводит два слова:
наиболее часто встречающееся и самое длинное.
"""


text = input().split()
max_word = ""
for word in text:
    if len(word) > len(max_word):
        max_word = word
print(max_word)


