#include <iostream>
#include <chrono> // Para medir el tiempo de ejecución
#include <thread> // Para usar sleep_for

// Definir constantes para los factores de multiplicación y el número de iteraciones
const int FACTOR = 9999, ITERATIONS = 1'000'000'000;

// Variables para almacenar los resultados de las operaciones y los tiempos de ejecución
int minResult = 0, sumResult = 0;
double timeSum = 0, timeMin = 0;

// Función para realizar una cuenta atrás de 3 segundos
void cuentaAtras()
{
    for (int i = 3; i > 0; i--)
    {
        std::cout << i << std::endl;
        std::this_thread::sleep_for(std::chrono::seconds(1)); // Esperar 1 segundo
    }
}

int main()
{
    // Iniciar la prueba de suma de enteros
    std::cout << "Comienza suma de enteros" << std::endl;
    cuentaAtras(); // Realizar la cuenta atrás

    // Capturar el tiempo inicial
    auto start = std::chrono::high_resolution_clock::now();
    // Realizar la suma de enteros
    for (int i = 0; i < ITERATIONS; i++)
    {
        sumResult = FACTOR + 5;
    }
    // Capturar el tiempo final
    auto end = std::chrono::high_resolution_clock::now();
    // Calcular el tiempo de ejecución
    timeSum = std::chrono::duration<double>(end - start).count();

    // Iniciar la prueba de resta de enteros
    std::cout << "Comienza la resta de enteros" << std::endl;
    cuentaAtras(); // Realizar la cuenta atrás

    // Capturar el tiempo inicial
    start = std::chrono::high_resolution_clock::now();
    // Realizar la resta de enteros
    for (int i = 0; i < ITERATIONS; i++){
        minResult = FACTOR - 5;
    }
    // Capturar el tiempo final
    end = std::chrono::high_resolution_clock::now();
    // Calcular el tiempo de ejecución
    timeMin = std::chrono::duration<double>(end - start).count();

    // Imprimir los resultados de los tiempos de ejecución
    std::cout << "El tiempo de ejecucion de sumar enteros es: " << timeSum << " segundos. Resultado de la operación: " << sumResult << "\n";
    std::cout << "El tiempo de ejecucion de restar enteros es: " << timeMin << " segundos. Resultado de la operación: " << minResult << "\n";

    return 0;
}