# Tarea 2 de Criptografía y Seguridad 2023-1
# Camila Alexandra Cruz Miranda
# Ejercicio 2
# Algoritmo rho de Pollard para encontrar un factor primo
import random
import math

# Calculamos una función (base^exp) % modulo 
# que será f(x) := x² + c mod p  
# c es un número aleatorio entre 1 ... p-1
# p es un número primo
def modulo_potencia(base, exp, mod):
 
    resultado = 1
 
    while (exp > 0):
     
        # si y es impar entonces base * resultado
        if (exp & 1):
            resultado = (resultado * base) % mod
 
        # exponente = exponente/2
        exp = exp >> 1
 
        # base = base * base
        base = (base * base) % mod
     
    return resultado
 
# Función que regresa el divisor primo para n 
def rho_de_Pollard( n):
    """
    2) Mediante el algoritmo de Rho de Pollard para enteros descomponga n = 7784099

    a) De la función semialeatoria empleada
        f(x) := x² + c mod p  
        c es un número aleatorio entre 1 ... p-1
        p es un número primo

    b) Número de iteración en el cual fue exitoso el algoritmo y factor encontrado.
    """

    pasos = 0

    # Caso Base: divisor primo de 1
    if (n == 1):
        return n
 
    # Caso Base: el divisor primo de números pares = 2
    if (n % 2 == 0):
        return 2
 
    # Aplicamos un rango de [2, N)
    x = (random.randint(0, 2) % (n - 2))
    y = x
 
    # Elegimos una constante para g(x) que podremos cambiar si el algoritmo no nos da la suficiente información
    c = (random.randint(0, 1) % (n - 1))
 
    # Variable del divisor
    divisor = 1

    # Iniciamos a dar pasos
    y = (modulo_potencia(y, 2, n) + c + n)%n
    y = (modulo_potencia(y, 2, n) + c + n)%n
    x = (modulo_potencia(x, 2, n) + c + n)%n

    #print(str(x), " ", str(y))
 
    # 2.b)
    while(x != y):
        pasos += 1
        y = (modulo_potencia(y, 2, n) + c + n)%n
        y = (modulo_potencia(y, 2, n) + c + n)%n
        x = (modulo_potencia(x, 2, n) + c + n)%n
        
    print("Se encontró una colisión después de " + str(pasos) + " intentos.")

    # Ciclo para obtener el factor primo:
    while (divisor == 1):
        
        # Paso chico: x(i+1) = g(x(i))
        x = (modulo_potencia(x, 2, n) + c + n)%n
 
        # Paso grande: y(i+1) = g(g(y(i)))
        y = 2*(modulo_potencia(y, 2, n) + c + n)%n
 
        # Revisamos el máximo común divisor de |x-y| y n
        divisor = math.gcd(abs(x - y), n)
            
        # Paso recursivo
        if (divisor == n):
            return rho_de_Pollard(n)

    return divisor
 
# Función main
if __name__ == "__main__":
 
    n = 7784099
    print("Encontramos que uno de los divisores de ", n , "es ", rho_de_Pollard(n))