import time
import numpy as np
time1 = time.time()

for i in range(100000000):
    multiplicacion = 2000*55555

# Crear un array de tamaño 1,000,000,000 y multiplicar
#data1 = np.full(1_000_000_000, 2000, dtype=np.int64)
#result1 = data1 * 55555
#data = np.full(100_000_000, 2000, dtype=np.int64)
#result = data * 55555

time2 = time.time()

for i in range(1000000000):
   multiplicacion1 = 9999 * 0.5


# Crear un array de tamaño 1,000,000,000 y multiplicar
data2 = np.full(1_000_000_000, 9999, dtype=np.float64)
result2 = data2 * 0.5
result2.size

time3 = time.time()

#for i in range(1000000000):
 #   division = 9999 / 2

# Número de iteraciones
num_iteraciones = 1_000_000_000


#data = np.full(num_iteraciones, 9999, dtype=np.float64)
#result = data / 2

time4 = time.time()

#print("tiempo1",time1)
#print("tiempo2",time2)

print("El tiempo de ejecución de multiplicar es: ", time3-time2, multiplicacion, result2.size)
print("El tiempo de ejecución de dividir es: ", time4-time3)