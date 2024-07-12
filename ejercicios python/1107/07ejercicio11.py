añoactual=2024
añonacimiento=int

añonacimiento=int(input("ingrese su año de nacimiento sin comas ni puntos:"))

edad=añoactual-añonacimiento
if edad >= 18:
    print("es mayor de edad")
else:
    print("es menor de edad")