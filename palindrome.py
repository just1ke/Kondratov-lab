text= input("введите текст: ")
clear= text.replace(" " , "")
if clear=="":
    print("текст отсутствует")
elif clear==clear[::-1]:
    print("палиндром")
else:
    print("не палиндрои")