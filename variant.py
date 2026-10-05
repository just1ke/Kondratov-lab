n= int(input("введите число (больше либо равно 0): "))
k=0
summa=0
for i in range(n):
    number=int(input(f"введите число#{i+1}: "))
    if number%2==0:
        k+=1
        summa+=number
print("количество",k)
print("сумма",summa)