public class prueba {
    public static void main(String[] args) {
        // Capturar el tiempo inicial en milisegundos
        long time1 = System.currentTimeMillis();

        // Primera operación: multiplicación
        for (int i = 0; i < 1_000_000_000; i++) {
            int multiplicacion = 2000 * 55555;
        }
        long time2 = System.currentTimeMillis();

        // Segunda operación: multiplicación con decimales
        for (int i = 0; i < 1_000_000_000; i++) {
            double multiplicacion = 9999 * 0.5;
        }
        long time3 = System.currentTimeMillis();

        // Tercera operación: división 
        for (int i = 0; i < 1_000_000_000; i++) {
            double division = 9999 / 2.0;
        }
        long time4 = System.currentTimeMillis();

        // Imprimir los resultados
        System.out.println("El tiempo de ejecución de multiplicar enteros es: " + (time2 - time1) / 1000.0 + " segundos");
        System.out.println("El tiempo de ejecución de multiplicar decimales es: " + (time3 - time2) / 1000.0 + " segundos");
        System.out.println("El tiempo de ejecución de dividir es: " + (time4 - time3) / 1000.0 + " segundos");
    }
}
