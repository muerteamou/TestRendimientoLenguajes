public class pruebaRendimientoMultiplicacion {
    public static void main(String[] args) {
        

        // Capturar el tiempo inicial
        double time1 = System.currentTimeMillis();

        // Primera operación: multiplicación
        for (int i = 0; i < 1000000000; i++) {
            int multiplicacion = 2000 * 55555;
        }
        double time2 = System.currentTimeMillis();

        // Segunda operación: multiplicación con decimales
        for (int i = 0; i < 1000000000; i++) {
            double multiplicacion = 9999 * 0.5;
        }
        double time3 = System.currentTimeMillis();

        // Tercera operación: división
        for (int i = 0; i < 1000000000; i++) {
            double division = 9999 / 2.0;
        }
        double time4 = System.currentTimeMillis();

        // Imprimir los resultados
        System.out.println("El tiempo de ejecución de multiplicar es: " + (time3 - time2) /1000 + " segundos");
        System.out.println("El tiempo de ejecución de dividir es: " + (time4 - time3) /1000 + " segundos");
    }
}