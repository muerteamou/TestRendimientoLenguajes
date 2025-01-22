#include <iostream>
#include <chrono> // Para medir el tiempo

int main() {
    // Capturar el tiempo inicial en milisegundos
    auto start1 = std::chrono::high_resolution_clock::now();

    // Primera operación: multiplicación
    for (int i = 0; i < 1'000'000'000; i++) {
        int multiplicacion = 2000 * 55555;
    }
    auto end1 = std::chrono::high_resolution_clock::now();

    // Segunda operación: multiplicación con decimales
    for (int i = 0; i < 1'000'000'000; i++) {
        double multiplicacion = 9999 * 0.5;
    }
    auto end2 = std::chrono::high_resolution_clock::now();

    // Tercera operación: división
    for (int i = 0; i < 1'000'000'000; i++) {
        double division = 9999 / 2.0;
    }
    auto end3 = std::chrono::high_resolution_clock::now();

    // Calcular los tiempos en segundos
    double time1 = std::chrono::duration<double>(end1 - start1).count();
    double time2 = std::chrono::duration<double>(end2 - end1).count();
    double time3 = std::chrono::duration<double>(end3 - end2).count();

    // Imprimir los resultados
    std::cout << "El tiempo de ejecucion de multiplicar enteros es: " << time1 << " segundos\n";
    std::cout << "El tiempo de ejecucion de multiplicar decimales es: " << time2 << " segundos\n";
    std::cout << "El tiempo de ejecucion de dividir es: " << time3 << " segundos\n";

    return 0;
}