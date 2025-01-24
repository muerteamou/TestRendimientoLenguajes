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
    minResult = 0.0
    div_result = 0.0

    print("Test de rendimiento de Python - Manejo de bucles y operaciones matemáticas")
    print("--------------------------------------------------------------------------")
    print("Comienza la multiplicación de enteros")
    iniciar_cuenta_atras()
    

    # Capturar el tiempo inicial en segundos
    start = time.time()

    # Primera operación: multiplicación de enteros
    for _ in range(ITERATIONS):
        sumResult = factor * 5

    # Capturar el tiempo final en segundos
    end = time.time()
    time_int = end - start

    print("Comienza la multiplicación de decimales")
    iniciar_cuenta_atras()

    # Capturar el tiempo inicial en segundos
    start = time.time()

    # Segunda operación: multiplicación con decimales
    for _ in range(ITERATIONS):
        minResult = factor * 0.5

    # Capturar el tiempo final en segundos
    end = time.time()
    time_double = end - start

    print("Comienza la división")
    iniciar_cuenta_atras()

    # Capturar el tiempo inicial en segundos
    start = time.time()

    # Tercera operación: división
    for _ in range(ITERATIONS):
        div_result = factor / 2.0

    # Capturar el tiempo final en segundos
    end = time.time()
    time_div = end - start
    time_total = time_int + time_double + time_div # Calcular el tiempo total de ejecución 

    # Imprimir los resultados
    print(f"El tiempo de ejecución de multiplicar enteros es: {time_int:.2f} segundos. Resultado de la operación: {sumResult}")
    print(f"El tiempo de ejecución de multiplicar decimales es: {time_double:.2f} segundos. Resultado de la operación: {minResult}")
    print(f"El tiempo de ejecución de dividir es: {time_div:.2f} segundos. Resultado de la operación: {div_result}")
    print(f"Tiempo total de ejecución: {time_total:.2f} segundos")


if __name__ == "__main__":
    main()