# Словарь по умолчанию
from multiprocessing.sharedctypes import Value
import re
from secrets import choice


dict = {
    "router" : "маршрутизатор",
    "switch" : "коммутатор",
    "firewall" : "файрвол",
    "repeater" : "повторитель",
    "splitter" : "разветвитель",
}

print("*" * 15, "Dict v 0.1", "*" * 15)

# Справка выводится при нажатии кнопки "h"
help_message = """
s - Поиск
a - Добавить новое слово
r - Удалить слово 
k - Показать все слова
d - Показать весь словарь
h - Справка
q - Выход
"""
choice = ""
while choice != "q":
    choice = input("(h - help)>> " )
    if choice == "s":
        word = input("Введите слово: ")
        res = dict.get(word, "Не найдено! ")
        print(res)
    elif choice == "a":
        word = input("Введите слово: ")
        value = input("Введите перевод: ")
        dict[word] = value
        print("Слово добавлено! ")
    elif choice == "r":
        word = input("Введите слово: ")
        del dict[word]
        print("Слово удалено! ")
    elif choice == "k":
        print(dict.keys())
    elif choice == "d":
        for word in dict:
            print(word, ": ", dict[word])
    elif choice == "h":
        print(help_message)
    elif choice == "q":
        continue;
    else: 
        print("Нераспознанная команда. введите h для справки. ")