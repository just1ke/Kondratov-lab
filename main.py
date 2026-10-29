from functions import sum_digits, average, normalize_text, select_numbers
def main():
    number = int(input("Введите целое число: "))
    print(f"Сумма цифр: {sum_digits(number)}")
    raw = input("Введите числа через пробел: ")
    numbers = [int(x) for x in raw.split()] if raw.strip() else []
    avg = average(numbers)
    if avg is None:
        print("Среднее: Нет данных")
    else:
        print(f"Среднее: {avg}")
    text = input("Введите текст: ")
    print(f"Нормализованный текст: {normalize_text(text)!r}")
    threshold = int(input("Введите порог (целое неотрицательное): "))
    selected = select_numbers(numbers, threshold)
    print(f"Числа с модулем больше {threshold}: {selected}")
if __name__ == "__main__":
    main()