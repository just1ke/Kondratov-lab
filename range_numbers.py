a= int(input("Введите число а: "))
b= int(input("введите число б: "))
if a<b:
    for number in range (a,b+1):
        print(number)
elif a>b:
    for number in range (a,b-1,-1):
        print(number)
    else:
        print(a)
