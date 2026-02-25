#1 Escriba un código que

x = 5

# Clasificación positivo / negativo / cero
if x > 0:
    print("Positivo")
elif x < 0:
    print("Negativo")
else:
    print("Cero")
  
# Clasificación par / impar
if x % 2 == 0:
    print("es Par")
else:
    print("es Impar")
  
#2 Explique la diferencia entre
#if → Primera condición.
#elif → Condición alternativa si la anterior no se cumple.
#else → Se ejecuta cuando ninguna condición anterior fue verdadera.

#3 Escriba un código que calcule la suma de los números del 1 al 20
#3 Imprima únicamente los números múltiplos de 3. use operadores abreviados (+=).

suma = 0

for i in range(1, 21):
    suma += i
    
    if i % 3 == 0:
        print(i)

print("La suma total es:", suma)

#4  Cree una función llamada clasificar_numero(x) que:
# Determine si el número es positivo, negativo o cero
# Determine si es par o impar
# Devuelva un mensaje combinando ambas clasificaciones

def clasificar_numero(x):

    if x > 0:
        tipo = "positivo"
    elif x < 0:
        tipo = "negativo"
    else:
        tipo = "cero"

    if x % 2 == 0:
        paridad = "par"
    else:
        paridad = "impar"

    return "El número es " + tipo + " y " + paridad
  
resultado = clasificar_numero(5)
print(resultado)
  
