salariodias=float
diastrabajados=int

diastrabajados=int(input("ingrese la cantidad de dias trabajados:"))
salariodias=float(input("ingrese el valor de su dia trabajado:"))

total=salariodias*diastrabajados
total= total - ((total*0.10) + (total*0.15))

print("usted debe retirar:", total)