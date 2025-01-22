import time
import numpy as np

# Primera operación: multiplicación
data1 = np.full(100_000_000, 2000, dtype=np.int64)
start1 = time.time()
result1 = data1 * 55555
end1 = time.time()

# Segunda operación: multiplicación con decimales
data2 = np.full(100_000_000, 9999, dtype=np.float64)
start2 = time.time()
result2 = data2 * 0.5
end2 = time.time()

# Tercera operación: división
chunk_size = 10_000_000
num_iteraciones = 100_000_000
result3 = np.zeros(num_iteraciones, dtype=np.float64)
start3 = time.time()
for i in range(0, num_iteraciones, chunk_size):
    data_chunk = np.full(chunk_size, 9999, dtype=np.float64)
    result3[i:i + chunk_size] = data_chunk / 2
end3 = time.time()

# Imprimir resultados
print("Tiempo de multiplicación enteros: ", end1 - start1, result1[0])
print("Tiempo de multiplicación decimales: ", end2 - start2, result2[0])
print("Tiempo de división: ", end3 - start3)
