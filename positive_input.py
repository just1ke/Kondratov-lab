otkl = 0
number = int(input("Введите целое число: "))
while number <= 0:
    otkl += 1
    number = int(input("Необходимо положительное число!: "))

print("Квадрат:", number * number)
print("Отклонено попыток:", otkl)
