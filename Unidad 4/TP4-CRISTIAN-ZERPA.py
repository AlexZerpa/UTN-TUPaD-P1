# Ejercicio 1
print("Bienvenido al programa")
for i in range(0,101,1):
    print(i)

# Ejercicio 2
num = int(input("Ingrese un número entero: "))
cont = 0
while num > 0:
    num2 = num/10
    entera=int(num2)
    num=entera
    cont = cont + 1
    
print(f"El número tiene {cont} dígitos.")

# Ejercicio 3
num = int(input("Ingrese el 1er numero entero: "))
num2 = int(input("Ingrese el 2do  numero entero: "))
suma=0
for i in range(num+1,num2):
    print(i)
    suma=suma+i
print(f"La suma de los números entre {num} y {num2} es: {suma}")

# Ejercicio 4
suma = 0
num = int(input("Ingrese un número entero o ingrese 0 para finalizar: "))
while num !=0:
    suma += num
    num = int(input("Ingrese un número entero o ingrese 0 para finalizar: "))

print(f"La suma de los números ingresados es: {suma}")

# Ejercicio 5
import random
numAleatorio = random.randint(0, 9)
print("Número aleatorio generado (entre 0 y 9):", numAleatorio)
print("adivina un numero entre 0 y 9")
num = int(input("Ingrese un número entero: "))
cont = 0
while numAleatorio != num:
    print("No adivinaste, intenta de nuevo.")
    num = int(input("Ingrese un número entero: "))
    cont = cont + 1

print(f"Felicidades, adivinaste el número {numAleatorio} en {cont} intentos.")

# Ejercicio 6
for i in range(100,0,-2):
    print(i)

# Ejercicio 7
num = int(input("Ingrese un número entero positivo: "))
cont= num
suma = 0
if num > 0:
    while num > 0:
        suma = suma + num
        num = num - 1
else:
    print("Por favor, ingrese un número entero positivo.")

print(f"La suma de los números desde 0 hasta {cont} es: {suma}")

# Ejercicio 8
num = int(input("Ingrese un número entero: "))
fin = 100
contPositivo = 0
contNegativo = 0
contPar = 0
contImpar = 0
for i in range(1, fin+1):
    print(i)
    if num >0:
        contPositivo = contPositivo + 1
    if num <0:
        contNegativo = contNegativo + 1
    if num % 2 == 0:
        contPar = contPar + 1
    else:
        contImpar = contImpar + 1
    num = int(input("Ingrese un número entero: "))
    
print(f"Cantidad de números positivos: {contPositivo}")
print(f"Cantidad de números negativos: {contNegativo}")
print(f"Cantidad de números pares: {contPar}")
print(f"Cantidad de números impares: {contImpar}")

# Ejercicio 9
cantidad = 100 
suma = 0
contador = 0

print(f"Ingresá {cantidad} números enteros:")

while contador < cantidad:
    numero = int(input(f"Número {contador + 1}: "))
    suma += numero
    contador += 1

media = suma / cantidad
print("La media es:", media)

# Ejercicio 10
numero = int(input("Ingresá un número entero: "))
invertido = 0

while numero > 0:
    digito = numero % 10             
    invertido = invertido * 10 + digito  
    print("Dígito extraído:", digito)
    print("Número invertido hasta ahora:", invertido)
    numero = numero // 10             

print("Número invertido:", invertido)