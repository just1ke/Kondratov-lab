ob_seconds = int(input("Введите общее количество секунд : "))
hours = ob_seconds // 3600
minutes = (ob_seconds % 3600) // 60
seconds = ob_seconds % 60
print(f"{hours} ч {minutes} мин {seconds} с")