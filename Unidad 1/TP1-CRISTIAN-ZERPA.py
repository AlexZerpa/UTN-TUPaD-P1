#ejercicio 1 
print("Hola Mundo")

#ejercicio 2
nombre  = input("¿Cómo te llamas? ")
print(f"Hola, {nombre}")

#ejercicio 3
nombre = input("¿Cual es tu nombre? ")
apellido = input("¿Cuál es tu apellido? ")
edad = input("¿Cuántos años tienes? ")
residencia = input("¿Dónde vives? ")
print(f"Soy, {nombre} {apellido}. Tengo {edad} años y vivo en {residencia}.")

#ejercicio 4
radio = float(input("Ingrese el radio del círculo: "))
area = 3.1416 * radio ** 2
perimetro = 2 * 3.1416 * radio
print(f"El área del círculo es: {area}")
print(f"El perímetro del círculo es: {perimetro}")

#ejercicio 5
segundos = float(input("Ingrese el tiempo en segundos: "))
horas = segundos // 3600
print(f"El tiempo en horas es: {horas}")

#ejercicio 6
digitos = int(input("Ingrese un número: "))
print(f" 1 * {digitos} = {1 * digitos}")
print(f" 2 * {digitos} = {2 * digitos}")
print(f" 3 * {digitos} = {3 * digitos}")
print(f" 4 * {digitos} = {4 * digitos}")
print(f" 5 * {digitos} = {5 * digitos}")
print(f" 6 * {digitos} = {6 * digitos}")
print(f" 7 * {digitos} = {7 * digitos}")
print(f" 8 * {digitos} = {8 * digitos}")
print(f" 9 * {digitos} = {9 * digitos}")
print(f"10 * {digitos} = {10 * digitos}")

#ejercicio 7
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
suma = num1 + num2
resta = num1 - num2
producto = num1 * num2
cociente = num1 / num2 if num2 != 0 else "Indefinido (división por cero)"
print(f"Suma: {suma}")
print(f"Resta: {resta}")
print(f"Producto: {producto}")
print(f"Cociente: {cociente}")

#ejercicio 8
altura = float(input("Ingrese su estatura: "))
peso = float(input("Ingrese su peso: "))
imc = peso / (altura ** 2)
print(f"Su índice de masa corporal (IMC) es: {imc}")

#ejercicio 9
grados_celsius = float(input("Ingrese la temperatura en grados Celsius: "))
grados_fahrenheit = (grados_celsius * 9/5) + 32
print(f"La temperatura en grados Fahrenheit es: {grados_fahrenheit}")

#ejercicio 10
num1 = int(input("Ingrese primer número entero: "))
num2 = int(input("Ingrese segundo número entero: "))
num3 = int(input("Ingrese tercer número entero: "))
promedio = (num1 + num2 + num3) / 3
print(f"El promedio de los tres números es: {promedio}")


