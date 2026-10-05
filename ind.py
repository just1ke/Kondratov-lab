#индивидуальное задание номер 4
score=int(input("Введите целое число от 0 до 100: "))
if score<0 or score>100:
    print("Ошибка диапазона")
elif score<=49:
    print("Нужна доработка")
elif score<=84:
    print("Зачет")
else:
    print("отличный результат")