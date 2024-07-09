menu= '''
menu
1 imc (indice de masa corporal)
2 porcentaje de grasa corporal
3 tasa metabólica basal
'''
print (menu)
op = int(input("elige tu opcion:"))
if op is 1:
    peso=float(input("ingrese su peso:"))
    estatura=float(input("ingrese su estatura:"))
    imc=peso/(estatura*estatura)
    print("su IMC es:", imc)

if op is 2:
    peso=float(input("ingrese su peso:"))
    estatura=float(input("ingrese su estatura:"))
    imc=peso/(estatura*estatura)
    edad=int(input("ingrese su edad:"))
    valor_genero=input("ingrese si su genero es femenino oprima 1 o masculino oprima 2")
    if valor_genero== "1":
        valor_genero=0
    else:
        valor_genero=10.8
    porcentaje_grasa = 1.2 * imc + 0.23 * edad - 5.4 - valor_genero
    print("su porcentaje de grasa corporal es:", porcentaje_grasa)
if op is 3:
    peso=float(input("ingrese su peso:"))
    estatura=float(input("ingrese su estatura:"))
    edad=int(input("ingrese su edad:"))
    valor_genero=input("ingrese si su genero es femenino oprima 1 o masculino oprima 2")
    if valor_genero== "1":
        valor_genero=-161
    else:
        valor_genero=5
    tasa_metabolica=(10*peso)+(6.25*estatura) - (5*edad) + valor_genero
    print("su tasa metabolica basal es:", tasa_metabolica)
    
    
    
    
    
    