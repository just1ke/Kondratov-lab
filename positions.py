r= input("введите целые числа через пробед: ").strip()
numb=[]
if r !="":
    for part in r.split():
        numb.append(int(part))
if len(numb)==0:
    print("нет данных")
else:
    maxim=max(numb)
    pos=[]
    for index,value in enumerate(numb):
        if value==maxim:
            pos.append(index)
    print(pos)