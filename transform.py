r= input("введите целые числа через пробед: ").strip()
numb=[]
if r !="":
    for part in r.split():
        numb.append(int(part))
absl=[]
for num in numb:
    if num<0:
        absl.append(-num)
    else:
        absl.append(num)
print(f"исходный: {numb}")
print(f"новый: {absl}")