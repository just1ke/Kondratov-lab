first_room = input("Первая аудитория: ")
second_room = input("Вторая аудитория: ")
print("До обмена:")
print(f"first_room  = {first_room}")
print(f"second_room = {second_room}")
t_room = first_room
first_room = second_room
second_room = t_room
print("После обмена:")
print(f"first_room  = {first_room}")
print(f"second_room = {second_room}")