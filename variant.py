#задание номер 1
r= input("введите целые числа через пробед: ").strip()
numb=[]
if r !="":
    for part in r.split():
        numb.append(int(part))
sel=[]
for num in numb:
    if num%2==0:
        sel.append(num)

count=len(sel)
total=sum(sel)
sor=sorted(sel)
print(f"выборка:  {sel}")
print(f"количество:  {count}")
print(f"сумма:    {total}")
print(f"сортировка:   {sor}")