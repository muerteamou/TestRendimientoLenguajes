import numpy as np
import time

def iniciar_cuenta_atras():
    """
    Realiza una cuenta atrás de 3 segundos con pausas de 1 segundo.
    """
    for i in range(3, 0, -1):
        print(i)
        time.sleep(1)  # Pausa de 1 segundo
    print("¡Calculando!")

def main():

    # Constantes para el número de iteraciones y el factor de multiplicación
    ITERATIONS = 100_000_000  # 1.000 millones de iteraciones
    factor = 9999  # Factor de multiplicación

    # Variables para almacenar los resultados de las operaciones
    sumResult = 0
    
    print("Test de rendimiento de Python - Manejo de bucles y operaciones matemáticas")

    print("Comienza la multiplicación de enteros")
    iniciar_cuenta_atras()

    # Capturar el tiempo inicial en segundos
    start = time.time()

    # Primera operación: multiplicación de enteros
    for i in range(ITERATIONS):
        sumResult = factor * 5

    # Capturar el tiempo final en segundos
    end = time.time()
    time_int = end - start

    print("Comienza la multiplicación de enteros con Numpy")
    iniciar_cuenta_atras()
    # Usando NumPy
    start = time.time()
    data = np.full(ITERATIONS, factor, dtype=np.float64)
    result = data *5
    end = time.time()
    time_int_np = end - start

    # Imprimir los resultados
    print(f"El tiempo de ejecución de multiplicar enteros es: {time_int:.2f} segundos. Resultado de la operación: {sumResult}")
    print(f"El tiempo de ejecución de multiplicar enteros con Numpy es: {time_int_np:.2f} segundos. Resultado de la operación: {sumResult}")

if __name__ == "__main__":
    main()
