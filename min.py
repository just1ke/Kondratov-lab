a= int (input("Введите первое число: "))
b= int (input("Ведите второе число:"))
c= int (input("Введите третье число: "))
if a<=b and a<=c:
    minim=a
elif b<=a and b<=c:
    minim=b
else:
    minim=c
print("Минимальное число", minim)