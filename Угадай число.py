import random

print("*" * 10, "Угадай число", "*" * 10)
print("Компьютер выберет случайным образом число от 1 до 10. Попробуй угадать это число. Для выхода введите 0")

answer = 1; #ответ
score = 0;  #счёт
i = 0       #попытки

while answer:

    rand = random.randint(1, 10)
    answer = int(input("Введите число: "))

    if answer == 0:
        break
    if answer == rand:
        score = score +1
        print("Правильно! Ваш счёт: ", score, " из ", i)
    else:
        print("Попробуй ещё раз!")
    i = i + 1

print("Общий счёт ", score, " из ", i)
print("До встречи!")