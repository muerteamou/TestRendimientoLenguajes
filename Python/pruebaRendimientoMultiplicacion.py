import time
import numpy as np
time1 = time.time()

for i in range(100000000):
    multiplicacion = 2000*55555

time2 = time.time()

for i in range(1000000000):
    multiplicacion = 9999 * 0.5

time3 = time.time()

for i in range(1000000000):
    division = 9999 / 2

time4 = time.time()

#print("tiempo1",time1)
#print("tiempo2",time2)

print("El tiempo de ejecución de multiplicar es: ", time3-time2)
print("El tiempo de ejecución de dividir es: ", time4-time3)

