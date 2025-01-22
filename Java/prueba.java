public class prueba {

    public static void main(String[] args) {

        // Constantes para el número de iteraciones y el factor de multiplicación
        final int ITERATIONS = 1_000_000_000, factor = 9999; // 1.000 millones de iteraciones y factor de multiplicación

        // Variables para almacenar los resultados de las operaciones
        int multIntResult = 0;
        double multDoubleResult = 0, divResult = 0, start = 0, end = 0, timeInt = 0, timeDou = 0, timeDiv = 0;

        System.out.println("Test de rendimiento de java - Manejo de bucles y operaciones matemáticas");

        System.out.println("Comienza la multiplicación de enteros");

        iniciarCuentaAtras();

        // Capturar el tiempo inicial en milisegundos
        start = System.currentTimeMillis();

        // Primera operación: multiplicación de enteros
        for (int i = 0; i < ITERATIONS; i++) {
            multIntResult = factor * 5;
        }
        // Capturar el tiempo final en milisegundos
        end = System.currentTimeMillis();
        timeInt = (end - start) / 1000;

        System.out.println("Comienza la multiplicación de decimales");

        iniciarCuentaAtras();

        // Capturar el tiempo inicial en milisegundos
        start = System.currentTimeMillis();

        // Segunda operación: multiplicación con decimales
        for (int i = 0; i < ITERATIONS; i++) {
            multDoubleResult = factor * 0.5;
        }
        // Capturar el tiempo final en milisegundos
        end = System.currentTimeMillis();
        timeDou = (end - start) / 1000;

        System.out.println("Comienza la división");

        iniciarCuentaAtras();

        // Capturar el tiempo inicial en milisegundos
        start = System.currentTimeMillis();

        // Tercera operación: división
        for (int i = 0; i < ITERATIONS; i++) {
            divResult = factor / 2.0;
        }
        // Capturar el tiempo final en milisegundos
        end = System.currentTimeMillis();
        timeDiv = (end - start) / 1000;

        // Imprimir los resultados
        System.out.println("El tiempo de ejecución de multiplicar enteros es: " + timeInt + " segundos. Resultado de la operación: " + multIntResult);
        System.out.println("El tiempo de ejecución de multiplicar decimales es: " + timeDou + " segundos. Resultado de la operación: " + multDoubleResult);
        System.out.println("El tiempo de ejecución de dividir es: " + timeDiv + " segundos. Resultado de la operación: " + divResult);
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