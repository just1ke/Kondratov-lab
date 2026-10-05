n=int(input("введите количество чисел : "))
total=0
bol=0
maximum= None
for i in range (n):
    number= int(input(f"введите число #{i+1}: ",))
    total+=number
    if number>0:
        bol+=1
    if maximum == None or number> maximum:
        maximum=number
print("Сумма:",total)
print("Положительные",bol)
print("максимум",maximum)