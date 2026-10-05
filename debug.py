first = "2"
second = "3"
print(f"Типы до преобразования: {type(first).__name__}, {type(second).__name__}")
first_num = int(first)
second_num = int(second)
print(f"Типы после преобразования: {type(first_num).__name__}, {type(second_num).__name__}")
print(f"Сумма чисел: {first_num + second_num}")
print("--- Фрагмент Б ---")
age = int(input("Возраст: "))
print(f"Тип age после int(): {type(age).__name__}")
print(f"Возраст через год: {age + 1}")
print("--- Фрагмент В ---")
first = 4
second = 7
third = 10
average = (first + second + third) / 3
print(f"Среднее: {average}")