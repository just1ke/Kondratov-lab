r= input("введите целые числа через пробед: ").strip()
if r=="":
    print("нет данных")
else:
    numb=[]
    for part in r.split():
        numb.append(int(part))
    count=len(numb)
    total=sum(numb)
    minim=min(numb)
    maxim=max(numb)
    average=total/count
    print(f"количество: {count}")
    print(f"сумма: {total}")
    print(f"минимум: {minim}")
    print(f"максимум: {maxim}")
    print(f"среднее: {average}")
