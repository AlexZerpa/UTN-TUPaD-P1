
# Ejercicio 1
edad = int(input("¿Cuántos años tienes? "))

if edad >= 18:
    print("Eres mayor de edad.")
elif edad < 18:
    print("Eres menor de edad.")

# Ejercicio 2
nota=int(input("Ingrese su nota (0-10): "))
if nota >= 6:
    print("Aprobado")
else:
    print("Desaprobado")

# Ejercicio 3
num = int(input("Ingrese un número entero: "))
if num % 2 == 0:
    print("Ha ingresado un número par.")
else:
    print("Por favor, ingrese número par.")

# Ejercicio 4
edad = int(input("¿Cuántos años tienes? "))

if edad > 0 and edad < 12:
    print("Eres un niño/a.")
elif edad >= 12 and edad < 18:
    print("Eres un adolescente.")
elif edad >= 18 and edad < 30:
    print("Eres un adulto/a joven.")
elif edad >=30:
    print("Eres un adulto/a.")

# Ejercicio 5
print("Bienvenido al sistema de autenticación")
print("condiciones para la contraseña: ")
print("1. Debe tener entre 8 y 14 caracteres")
contraseña = input("Introduce la contraseña: ")
min=len(contraseña)>=8
max=len(contraseña)<=14
if (contraseña and min and max) == True:
    print("Acceso concedido")
else:
    print("Acceso denegado")
    
# Ejercicio 6

from statistics import mean, median, mode
import random
numeros_aleatorios = [random.randint(1, 100) for _ in range(50)]
print("Números aleatorios:", numeros_aleatorios)
print("Moda:", mode(numeros_aleatorios))
print("Mediana:", median(numeros_aleatorios)) 
print("Media:", mean(numeros_aleatorios)) 

# Ejercicio 7
frase=str(input("Ingrese una frase: "))
ultimaLetra=frase[-1]
if ultimaLetra == "a" or ultimaLetra == "e" or ultimaLetra == "i" or ultimaLetra == "o" or ultimaLetra == "u":
    print("La frase es: ",frase + "!")
elif ultimaLetra == "A" or ultimaLetra == "E" or ultimaLetra == "I" or ultimaLetra == "O" or ultimaLetra == "U":
    print("La frase es: ",frase + "!")
else:
    print("La frase es: ",frase)

# Ejercicio 8
nombre=str(input("Ingrese su nombre: "))
print("Seleccione una opción:")
print("1 - Escribir nombre en Mayúsculas")
print("2 - Escribir nombre en Minúsculas")
print("3 - Escribir nombre con la primera letra en Mayúscula")
opc=int(input("Ingrese una opción (1-3): "))

if opc==1:
    print(nombre.upper())
elif opc==2:
    print(nombre.lower())
elif opc==3:
    print(nombre.title())
else:
    print("Opción no válida")

# Ejercicio 9
print("Clasificación de un sismo según su magnitud")
magnitud=int(input("Ingrese la magnitud: "))
if magnitud < 3:
    print("Muy leve")
elif magnitud >= 3 and magnitud < 4:
    print("Leve")
elif magnitud >= 4 and magnitud < 5:
    print("Moderado")
elif magnitud >= 5 and magnitud < 6:
    print("Fuerte")
elif magnitud >= 6 and magnitud < 7:
    print("Muy fuerte")
elif magnitud >= 7:
    print("Extremo")

# Ejercicio 10
print("ESTACIONES DEL AÑO")
hemisferio = input("Ingrese el hemisferio (N/S): ").strip().lower()
print("hemisferio:", hemisferio)
print("sabiendo que Enero es el 1 mes y Diciembre es el 12 mes")
mes = int(input("Ingrese el mes (1-12): "))
print("mes:", mes)
dia = int(input("Ingrese el día (1-31): "))
print("dia:", dia)

if hemisferio == "n":
    if (mes == 12 and dia >= 21) or (mes <= 3 and dia <= 20) or (mes < 3):
        print("Es invierno")
    elif (mes == 3 and dia >= 21) or (mes <= 6 and dia <= 20) or (mes < 6):
        print("Es primavera")
    elif (mes == 6 and dia >= 21) or (mes <= 9 and dia <= 20) or (mes < 9):
        print("Es verano")
    elif (mes == 9 and dia >= 21) or (mes <= 12 and dia <= 20) or (mes < 12):
        print("Es otoño")
    else:
        print("Fecha no válida")
if hemisferio == "s":
    if (mes == 12 and dia >=21) or (mes <=3 and dia <=20) or (mes<3):
        print("Es verano")
    elif (mes == 3 and dia >=21) or (mes <=6 and dia <=20) or (mes<6):
        print("Es otoño")
    elif (mes == 6 and dia >=21) or (mes <=9 and dia <=20) or (mes<9):
        print("Es invierno")
    elif (mes == 9 and dia >=21) or (mes <=12 and dia <=20) or (mes<12):
        print("Es primavera")
    else:
        print("Fecha no válida")
