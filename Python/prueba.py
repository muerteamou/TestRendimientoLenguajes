import numpy as np
import time

# Parámetros
num_iteraciones = 1_000_000_000

# Usando NumPy
start_np = time.time()
data = np.full(num_iteraciones, 9999, dtype=np.float64)
result = data / 2
end_np = time.time()
print(f"Tiempo con NumPy: {end_np - start_np:.2f} segundos")

# Usando un bucle nativo
start_native = time.time()
for _ in range(num_iteraciones):
    division = 9999 / 2
end_native = time.time()
print(f"Tiempo con bucle nativo: {end_native - start_native:.2f} segundos")
