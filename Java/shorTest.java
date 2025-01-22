public class shorTest {

    public static void main(String[] args) {

        // Constantes para el número de iteraciones y el factor de multiplicación
        final int ITERATIONS = 1_000_000_000, factor = 9999; // 1.000 millones de iteraciones y factor de multiplicación

        // Variables para almacenar los resultados de las operaciones
        int minResult = 0, sumResult = 0;
        double start = 0, end = 0, timeSum = 0, timeMin = 0;

        System.out.println("Test de rendimiento de java - Manejo de bucles y operaciones matemáticas");
        System.out.println("Comienza la suma de enteros");

        iniciarCuentaAtras();

        // Capturar el tiempo inicial en milisegundos
        start = System.currentTimeMillis();

        // Primera operación: suma de enteros
        for (int i = 0; i < ITERATIONS; i++) {
            sumResult = factor + 5;
        }
        // Capturar el tiempo final en milisegundos
        end = System.currentTimeMillis();
        timeSum = (end - start) / 1000;

        System.out.println("Comienza la multiplicación de decimales");

        iniciarCuentaAtras();

        // Capturar el tiempo inicial en milisegundos
        start = System.currentTimeMillis();

        // Segunda operación: resta de enteros
        for (int i = 0; i < ITERATIONS; i++) {
            minResult = factor - 5;
        }
        // Capturar el tiempo final en milisegundos
        end = System.currentTimeMillis();
        timeMin = (end - start) / 1000;

        // Imprimir los resultados
        System.out.println("El tiempo de ejecución de sumar enteros es: " + timeSum
                + " segundos. Resultado de la operación: " + sumResult);
        System.out.println("El tiempo de ejecución de restar enteros es: " + timeMin
                + " segundos. Resultado de la operación: " + minResult);
    }

    // Función para realizar una cuenta atrás de 3 segundos
    public static void iniciarCuentaAtras() {
        for (int i = 3; i > 0; i--) {
            System.out.println(i);
            try {
                Thread.sleep(1000); // Esperar 1 segundo entre cada número
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
    }
}