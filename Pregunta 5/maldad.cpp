#include <iostream>
#include <vector>
#include <cmath>
#include <chrono>
#include <iomanip>

using namespace std;

// Creamos una función propia de Coeficiente Binomial, usando programación dinámica
long long binomialCoefficient(const long long n, const long long k) {
    vector<long long> aSolutions(k);
    aSolutions[0] = n - k + 1;

    for (int i = 1; i < k; ++i) {
        aSolutions[i] = aSolutions[i - 1] * (n - k + 1 + i) / (i + 1);
    }

    return aSolutions[k - 1];
}

long long narayana(long long n, long long k) {
    return (1.0 / n) * binomialCoefficient(n, k) * binomialCoefficient(n, k - 1);
}

// Optimizamos transformando la recursión en un ciclo iterativo
long long tribonacciIterative(long long n) {
    if (n == 0) return 0;
    if (n == 1) return 1;
    if (n == 2) return 2;

    long long a = 0, b = 1, c = 2, next_value;
    for (int i = 3; i <= n; ++i) {
        next_value = a + b + c;
        a = b;
        b = c;
        c = next_value;
    }

    return c;
}

long long maldad(int n) {
    long long k = floor(log2(n));
    long long N_n_k = narayana(n, k);
    long long log_value = floor(log2(N_n_k));

    return tribonacciIterative(log_value + 1);
}

int main(int argc, char* argv[]) {
    int n;

    if (argc > 1) {
        n = stoi(argv[1]);
    } else {
        cin >> n; // Solicitar al usuario o judge el valor de n
    }

    auto start_time = chrono::high_resolution_clock::now();
    long long result = maldad(n);
    auto end_time = chrono::high_resolution_clock::now();
    chrono::duration<double> execution_time = end_time - start_time;

    cout << "maldad(" << n << ") = " << result << endl;
    cout << fixed << setprecision(10);
    cout << "Tiempo de ejecución = " << execution_time.count() << " segundos" << endl;

    return 0;
}
