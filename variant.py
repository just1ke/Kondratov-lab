def main():
    text = input("Введите строку: ")
    words = text.split()
    matched = []
    for raw in words:
        cleaned = raw.strip(".,!?;:").lower()
        if not cleaned:
            continue
        if "ра" in cleaned:
            matched.append(cleaned)
    if not matched:
        print("Нет совпадений")
        print("Количество: 0")
    else:
        for w in matched:
            print(w)
        print(f"Количество: {len(matched)}")
if __name__ == "__main__":
    main()
    #12 задание
