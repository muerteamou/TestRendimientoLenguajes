import time

def iniciar_cuenta_atras():
    """
    Realiza una cuenta atrás de 3 segundos con pausas de 1 segundo.
    """
    for i in range(3, 0, -1):
        print(i)
        time.sleep(1)  # Pausa de 1 segundo


def main():
    # Constantes para el número de iteraciones y el factor de multiplicación
    ITERATIONS = 1_000_000_000  # 1.000 millones de iteraciones
    factor = 9999  # Factor de multiplicación

    # Variables para almacenar los resultados de las operaciones
    sumResult = 0
    minResult = 0

    print("Test de rendimiento de Python - Manejo de bucles y operaciones matemáticas")

    print("Comienza la suma de enteros")
    iniciar_cuenta_atras()

    # Capturar el tiempo inicial en segundos
    start = time.time()

    # Primera operación: multiplicación de enteros
    for _ in range(ITERATIONS):
        sumResult = factor + 5

    # Capturar el tiempo final en segundos
    end = time.time()
    time_int = end - start

    print("Comienza la resta de enteros")
    iniciar_cuenta_atras()

    # Capturar el tiempo inicial en segundos
    start = time.time()

    # Segunda operación: resta de enteros
    for _ in range(ITERATIONS):
        minResult = factor - 5

    # Capturar el tiempo final en segundos
    end = time.time()
    time_double = end - start

    # Imprimir los resultados
    print(f"El tiempo de ejecución de multiplicar enteros es: {time_int:.2f} segundos. Resultado de la operación: {sumResult}")
    print(f"El tiempo de ejecución de multiplicar decimales es: {time_double:.2f} segundos. Resultado de la operación: {minResult}")
   
if __name__ == "__main__":
    main()