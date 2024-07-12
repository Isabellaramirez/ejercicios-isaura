compras=int
costo=float

compras=int(input("ingrese la cantidad de productos comprados"))
costo=int(input("ingrese el valor del producto comprado"))

total=compras*costo
total=total+(total*0.15)

print("el total de sus compras fue de:", total)