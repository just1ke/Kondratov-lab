subject1 = input("Название предмета 1: ")
lessons1 = int(input("Количество занятий по предмету 1 за неделю : "))
prod1 = int(input("Продолжительность занятия 1 в минутах : "))
subject2 = input("Название предмета 2: ")
lessons2 = int(input("Количество занятий по предмету 2 за неделю: "))
prod2 = int(input("Продолжительность занятия 2 в минутах: "))
svhours = float(input("Доступное время на неделю, в часах: "))
minutes1 = lessons1 * prod1
minutes2 = lessons2 * prod2
vsminutes = minutes1 + minutes2
vshours = vsminutes / 60
free_hours = svhours - vshours
four_weeks_hours = vshours * 4
print("УЧЕБНАЯ НАГРУЗКА")
print(f"{subject1}: {minutes1} мин")
print(f"{subject2}: {minutes2} мин")
print(f"Общая нагрузка: {vsminutes} мин = {vshours:.2f} ч")
print(f"Свободное время: {free_hours:.2f} ч")
print(f"Нагрузка за 4 недели: {four_weeks_hours:.2f} ч")
