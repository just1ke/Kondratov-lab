ord_name = input("Название заказа: ")
customer = input("Имя заказчика: ")
item1_name = input("Позиция 1 — название: ")
item1_q = int(input("Позиция 1 — количество : "))
item1_price = float(input("Позиция 1 — цена за единицу, руб. : "))
item2_name = input("Позиция 2 — название: ")
item2_q = int(input("Позиция 2 — количество : "))
item2_price = float(input("Позиция 2 — цена за единицу, руб.: "))
st = float(input("Стоимость доставки, руб: "))
paid = float(input("Внесённая сумма, руб: "))
item1_cost = item1_q * item1_price
item2_cost = item2_q * item2_price
goods_cost = item1_cost + item2_cost
total = goods_cost + st
total_qty = item1_q + item2_q
if paid < total:
    print("Ошибка: внесённой суммы недостаточно.")
    raise SystemExit
change = paid - total
print(f"ЗАКАЗ: {ord_name}")
print(f"Заказчик: {customer}")
print(f"{item1_name}  {item1_q}  {item1_price:.2f}  {item1_cost:.2f}")
print(f"{item2_name}  {item2_q} {item2_price:.2f}  {item2_cost:.2f}")
print(f"Товары без доставки: {goods_cost:.2f} руб.")
print(f"Доставка: {st:.2f} руб.")
print(f"Итого с доставкой: {total:.2f} руб.")
print(f"Всего единиц: {total_qty}")
print(f"Сдача:  {change:.2f} руб.")
