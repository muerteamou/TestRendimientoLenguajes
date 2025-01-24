import numpy as np
import time

def countdown():
    """
    Realiza una cuenta atrás de 3 segundos con pausas de 1 segundo.
    """
    for i in range(3, 0, -1):
        print(i)
        time.sleep(1)  # Pausa de 1 segundo
    print("¡Calculando!")

def main():
    # Constantes para el número de iteraciones y el factor de multiplicación
    ITERATIONS = 100_000_000  # 100 millones de iteraciones
    FACTOR = 9999  # Factor de multiplicación
    CHUNK_SIZE = 10_000_000  # Tamaño del chunk para la división
    
    print("Test de rendimiento de Python con Numpy - Manejo de bucles y operaciones matemáticas")
    print("------------------------------------------------------------------------------------")

    # Primera operación: multiplicación de enteros con Numpy
    print("Comienza la multiplicación de enteros con Numpy")
    countdown()
    start = time.time()  # Capturar el tiempo inicial
    
    # Crear un array de enteros con ITERATIONS elementos, todos con el valor FACTOR
    data = np.full(ITERATIONS, FACTOR, dtype=np.int64) 
    sumResult = data * 5 # Realizar la multiplicación de cada elemento por 5
    end = time.time() # Capturar el tiempo final
    time_int_np = end - start # Calcular el tiempo de ejecución

    # Segunda operación: multiplicación con decimales
    print("Comienza la multiplicación de decimales con Numpy")
    countdown()
    start = time.time() # Capturar el tiempo inicial
    
    # Crear un array de decimales con ITERATIONS elementos, todos con el valor FACTOR
    data2 = np.full(ITERATIONS, FACTOR, dtype=np.float64)
    mult_doub_result = data2 * 0.5 # Realizar la multiplicación de cada elemento por 0.5 
    end = time.time()  # Capturar el tiempo final
    time_doub_np = end - start # Calcular el tiempo de ejecución

    # Tercera operación: división
    print("Comienza la división con Numpy")
    countdown()
    start = time.time() # Capturar el tiempo inicial
    
    # Crear un array para almacenar los resultados de la división
    div_result = np.zeros(ITERATIONS, dtype=np.float64)   
    for i in range(0, ITERATIONS, CHUNK_SIZE): # Realizar la división en chunks para evitar usar demasiada memoria
        data_chunk = np.full(CHUNK_SIZE, FACTOR, dtype=np.float64)
        div_result[i:i + CHUNK_SIZE] = data_chunk / 2   
    
    end = time.time() # Capturar el tiempo final
    time_div_np = end - start # Calcular el tiempo de ejecución
    
    time_total = time_int_np + time_doub_np + time_div_np # Calcular el tiempo total de ejecución   

    # Imprimir los resultados
    print(f"El tiempo de ejecución de multiplicar enteros con Numpy es: {time_int_np:.2f} segundos. Resultado de la operación: {sumResult[0]}")
    print(f"El tiempo de ejecución de multiplicar decimales con Numpy es: {time_doub_np:.2f} segundos. Resultado de la operación: {mult_doub_result[0]}")
    print(f"El tiempo de ejecución de dividir con Numpy es: {time_div_np:.2f} segundos. Resultado de la operación: {div_result[0]}")
    print(f"Tiempo total de ejecución: {time_total:.2f} segundos")
    
if __name__ == "__main__":
    main()