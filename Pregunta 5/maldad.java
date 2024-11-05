import static java.lang.Math.floor;
import static java.lang.Math.log;
import java.util.Scanner;

class Maldad {

    // Función para calcular el Coeficiente Binomial
    public static long binomialCoefficient(long n, long k) {
        long[] aSolutions = new long[(int) k];
        aSolutions[0] = n - k + 1;

        for (int i = 1; i < k; i++) {
            aSolutions[i] = aSolutions[i - 1] * (n - k + 1 + i) / (i + 1);
        }

        return aSolutions[(int) (k - 1)];
    }

    // Función para calcular el número de Narayana
    public static double narayana(long n, long k) {
        return (1.0 / n) * binomialCoefficient(n, k) * binomialCoefficient(n, k - 1);
    }

    // Función iterativa para calcular el número de Tribonacci
    public static long tribonacciIterative(long n) {
        if (n == 0) return 0;
        if (n == 1) return 1;
        if (n == 2) return 2;

        long a = 0, b = 1, c = 2;
        for (int i = 3; i <= n; i++) {
            long nextValue = a + b + c;
            a = b;
            b = c;
            c = nextValue;
        }

        return c;
    }

    // Función principal que calcula la "maldad"
    public static long maldad(int n) {
        long k = (long) floor(log(n) / log(2)); // Calcular log2(n)
        long N_n_k = (long) narayana(n, k);
        long logValue = (long) floor(log(N_n_k) / log(2)); // Calcular log2(N_n_k)

        return tribonacciIterative(logValue + 1);
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();

        long startTime = System.nanoTime();
        long result = maldad(n);
        long endTime = System.nanoTime();

        double executionTime = (endTime - startTime) / 1_000_000_000.0; // Convertir nanosegundos a segundos

        System.out.printf("maldad(%d) = %d%n", n, result);
        System.out.printf("Tiempo de ejecución = %.10f segundos%n", executionTime);
    }
}
