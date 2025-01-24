#include <iostream>
#include <vector>
#include <cmath>
#include <thread>
#include <chrono>

using namespace std;

/**
 * Verifica si un número es primo.
 * 
 * @param n Número a verificar
 * @return true si el número es primo, false en caso contrario
 */
bool isPrime(int n) {
    if (n <= 1) return false;
    for (int i = 2; i <= sqrt(n); i++) {
        if (n % i == 0) return false;
    }
    return true;
}

/**
 * Realiza una cuenta atrás de 3 segundos con pausas de 1 segundo.
 */
void countdown() {
    for (int i = 3; i > 0; i--) {
        cout << i << endl;
        this_thread::sleep_for(chrono::seconds(1)); // Pausa de 1 segundo
    }
    cout << "¡Calculando!" << endl;
}

/**
 * Calcula los primeros n números primos.
 * 
 * @param n Cantidad de números primos a calcular
 * @return Vector con los números primos calculados
 */
vector<int> getPrimes(int n) {
    vector<int> primes;
    int number = 2;
    while (primes.size() < n) {
        if (isPrime(number)) {
            primes.push_back(number);
        }
        number++;
    }
    return primes;
}

int main() {
    const int PRIMES = 200000; // Número de primos a calcular

    cout << "Test de rendimiento de C++ calculando números primos" << endl;
    cout << "----------------------------------------------------" << endl;
    cout << "Comienza el cálculo de primos" << endl;

    countdown(); // Realiza una cuenta atrás antes de iniciar el cálculo

    auto start = chrono::high_resolution_clock::now(); // Captura el tiempo inicial
    vector<int> primes = getPrimes(PRIMES); // Calcula los primeros 200,000 números primos
    auto end = chrono::high_resolution_clock::now(); // Captura el tiempo final

    chrono::duration<double> elapsed = end - start; // Calcula el tiempo transcurrido

    cout << "Tiempo de ejecución: " << elapsed.count() << " segundos" << endl; // Imprime el tiempo de ejecución
    cout << "Valor del último primo: " << primes.back() << endl; // Imprime el valor del último primo encontrado

    return 0;
}
