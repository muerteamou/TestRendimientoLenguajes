import math
import time

def is_prime(n):
    """
    Verifica si un número es primo.
    """
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def countdown():
    """
    Realiza una cuenta atrás de 3 segundos con pausas de 1 segundo.
    """
    for i in range(3, 0, -1):
        print(i)
        time.sleep(1)  # Pausa de 1 segundo
    print("¡Calculando!")

def get_primes(n):
    """
    Calcula los primeros n números primos.
    """
    primes = []
    number = 2
    while len(primes) < n:
        if is_prime(number):
            primes.append(number)
        number += 1
    return primes

PRIMES = 200_000  # Número de primos a calcular
print("Test de rendimiento de Python calculando números primos")
print("-------------------------------------------------------")
print("Comienza el calculo de primos")
countdown()  # Realiza una cuenta atrás antes de iniciar el cálculo

start = time.time()  # Captura el tiempo inicial
primes = get_primes(PRIMES)  # Calcula los primeros 200,000 números primos
end = time.time()  # Captura el tiempo final

print("Tiempo de ejecución: ", end - start , "segundos")  # Imprime el tiempo de ejecución
print("Valor del último primo:", primes[199999])  # Imprime el valor del último primo encontrado