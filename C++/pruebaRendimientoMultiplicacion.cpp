#include <iostream>
#include <chrono> // Para medir el tiempo de ejecución
#include <thread> // Para usar sleep_for

// Definir constantes para los factores de multiplicación y el número de iteraciones
const int FACTOR = 9999, ITERATIONS = 1'000'000'000;

// Variables para almacenar los resultados de las operaciones y los tiempos de ejecución
int multIntResult = 0;
double multDoubleResult = 0, divResult = 0, timeInt = 0, timeDou = 0, timeDiv = 0;

// Función para realizar una cuenta atrás de 3 segundos
void cuentaAtras() {
    for (int i = 3; i > 0; i--) {
        std::cout << i << std::endl;
        std::this_thread::sleep_for(std::chrono::seconds(1)); // Esperar 1 segundo
    }
}

int main() {
    // Iniciar la prueba de multiplicación de enteros
    std::cout << "Comienza multiplicación de enteros" << std::endl;
    cuentaAtras(); // Realizar la cuenta atrás

    // Capturar el tiempo inicial
    auto start = std::chrono::high_resolution_clock::now();
    // Realizar la multiplicación de enteros
    for (int i = 0; i < ITERATIONS; i++) {
        multIntResult = FACTOR * 5;
    }
    // Capturar el tiempo final
    auto end = std::chrono::high_resolution_clock::now();
    // Calcular el tiempo de ejecución
    timeInt = std::chrono::duration<double>(end - start).count();

    // Iniciar la prueba de multiplicación de decimales
    std::cout << "Comienza la multiplicación de decimales" << std::endl;
    cuentaAtras(); // Realizar la cuenta atrás

    // Capturar el tiempo inicial
    start = std::chrono::high_resolution_clock::now();
    // Realizar la multiplicación de decimales
    for (int i = 0; i < ITERATIONS; i++) {
        multDoubleResult = FACTOR * 0.5;
    }
    // Capturar el tiempo final
    end = std::chrono::high_resolution_clock::now();
    // Calcular el tiempo de ejecución
    timeDou = std::chrono::duration<double>(end - start).count();

    // Iniciar la prueba de división
    std::cout << "Comienza la división" << std::endl;
    cuentaAtras(); // Realizar la cuenta atrás

    // Capturar el tiempo inicial
    start = std::chrono::high_resolution_clock::now();
    // Realizar la división
    for (int i = 0; i < ITERATIONS; i++) {
        divResult = FACTOR / 2.0;
    }
    // Capturar el tiempo final
    end = std::chrono::high_resolution_clock::now();
    // Calcular el tiempo de ejecución
    timeDiv = std::chrono::duration<double>(end - start).count();

    // Imprimir los resultados de los tiempos de ejecución
    std::cout << "Tiempo de ejecución de la multiplicación de enteros: " << timeInt << " segundos" << std::endl;
    std::cout << "Tiempo de ejecución de la multiplicación de decimales: " << timeDou << " segundos" << std::endl;
    std::cout << "Tiempo de ejecución de la división: " << timeDiv << " segundos" << std::endl;

    return 0;
}