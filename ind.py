kol=int(input("количество страниц: "))
stran=int(input("всего страниц в тетради: "))
full=kol//stran
ost=kol%stran
vs=(kol+stran-1)//stran
print(f"полных: {full}")
print(f"остаток: {ost}")
print(f"всего: {vs}")
