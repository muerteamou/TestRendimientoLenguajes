import java.util.ArrayList;
import java.util.List;

public class PrimeNumbers {

    /**
     * Verifica si un número es primo.
     * 
     * @param n Número a verificar
     * @return true si el número es primo, false en caso contrario
     */
    public static boolean isPrime(int n) {
        if (n <= 1) return false;
        for (int i = 2; i <= Math.sqrt(n); i++) {
            if (n % i == 0) return false;
        }
        return true;
    }

    /**
     * Realiza una cuenta atrás de 3 segundos con pausas de 1 segundo.
     */
    public static void countdown() {
        try {
            for (int i = 3; i > 0; i--) {
                System.out.println(i);
                Thread.sleep(1000); // Pausa de 1 segundo
            }
            System.out.println("¡Calculando!");
        } catch (InterruptedException e) {
            System.err.println("Se interrumpió la cuenta atrás.");
        }
    }

    /**
     * Calcula los primeros n números primos.
     * 
     * @param n Cantidad de números primos a calcular
     * @return Lista con los números primos calculados
     */
    public static List<Integer> getPrimes(int n) {
        List<Integer> primes = new ArrayList<>();
        int number = 2;
        while (primes.size() < n) {
            if (isPrime(number)) {
                primes.add(number);
            }
            number++;
        }
        return primes;
    }

    public static void main(String[] args) {
        final int PRIMES = 200_000; // Número de primos a calcular

        System.out.println("Test de rendimiento de Java calculando números primos");
        System.out.println("-------------------------------------------------------");
        System.out.println("Comienza el cálculo de primos");

        countdown(); // Realiza una cuenta atrás antes de iniciar el cálculo

        long start = System.currentTimeMillis(); // Captura el tiempo inicial
        List<Integer> primes = getPrimes(PRIMES); // Calcula los primeros 200,000 números primos
        long end = System.currentTimeMillis(); // Captura el tiempo final

        System.out.println("Tiempo de ejecución: " + (end - start) / 1000.0 + " segundos"); // Imprime el tiempo de ejecución
        System.out.println("Valor del último primo: " + primes.get(PRIMES - 1)); // Imprime el valor del último primo encontrado
    }
}
