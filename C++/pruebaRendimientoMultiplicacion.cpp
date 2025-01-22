#include <iostream>
#include <chrono> // Para medir el tiempo de ejecución
#include <thread> // Para usar sleep_for

// Definir constantes para los factores de multiplicación

const int FACTOR = 9999, ITERATIONS = 1'000'000'000;

int multIntResult = 0;
double multDoubleResult = 0, divResult = 0, timeInt = 0, timeDou = 0, timeDiv = 0;

void cuentaAtras()
{
    for (int i = 3; i > 0; i--)
    {
        std::cout << i << std::endl;
        std::this_thread::sleep_for(std::chrono::seconds(1));
    }
}

int main()
{
    std::cout << "Comienza multiplicación de enteros" << std::endl;
    cuentaAtras();

    auto start = std::chrono::high_resolution_clock::now();
    for (int i = 0; i < ITERATIONS; i++)
    {
        multIntResult = FACTOR * 5;
    }
    auto end = std::chrono::high_resolution_clock::now();
    timeInt = std::chrono::duration<double>(end - start).count();

    std::cout << "Comienza la multiplicación de decimales" << std::endl;
    cuentaAtras();

    start = std::chrono::high_resolution_clock::now();
    for (int i = 0; i < ITERATIONS; i++)
    {
        multDoubleResult = FACTOR * 0.5;
    }
    end = std::chrono::high_resolution_clock::now();
    timeDou = std::chrono::duration<double>(end - start).count();

    std::cout << "Comienza  división" << std::endl;
    cuentaAtras();
    start = std::chrono::high_resolution_clock::now();
    for (int i = 0; i < ITERATIONS; i++)
    {
        divResult = FACTOR / 2;
    }
    end = std::chrono::high_resolution_clock::now();
    timeDiv = std::chrono::duration<double>(end - start).count();

    std::cout << "El tiempo de ejecucion de multiplicar enteros es: " << timeInt << " segundos. Resultado de la operación: " << multIntResult << "\n";
    std::cout << "El tiempo de ejecucion de multiplicar decimales es: " << timeDou << " segundos. Resultado de la operación: " << multDoubleResult << "\n";
    std::cout << "El tiempo de ejecucion de dividir es: " << timeDiv << " segundos. Resultado de la operación: " << divResult << "\n";

    return 0;
}