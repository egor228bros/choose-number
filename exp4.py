from random import *
print("привет ты в игре угадай число")
print("твоя задача угадать число от 1 до 100")
r = randint(1, 100)
attempts = 5

while attempts > 0:
    user = int(input("введи число: "))
    attempts = attempts - 1
    if r == user:
        print("угадал")
        break
else:
    print("неверно")
    if r > user:
        print("больше")
    else:
        print("меньше")

    print("осталось попыток", attempts)
print("игра окончена")
print("заданное число", r)