import time
from math import log2, floor

def binomial_coefficient(n: int, k: int) -> int:
    a_solutions = [0] * k
    a_solutions[0] = n - k + 1

    for i in range(1, k):
        a_solutions[i] = a_solutions[i - 1] * (n - k + 1 + i) // (i + 1)

    return a_solutions[k - 1]


def narayana(n: int, k: int) -> float:
    return (1 / n) * binomial_coefficient(n, k) * binomial_coefficient(n, k - 1)


def tribonacci_iterative(n: int) -> int:
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 2

    a, b, c = 0, 1, 2
    for _ in range(3, n + 1):
        next_value = a + b + c
        a, b, c = b, c, next_value

    return c

def maldad(n: int) -> int:
    k = floor(log2(n))
    N_n_k = narayana(n, k)
    log_value = floor(log2(N_n_k))

    return tribonacci_iterative(log_value + 1)

def main():
    n = int(input(""))

    start_time = time.time()
    result = maldad(n)
    end_time = time.time()
    
    execution_time = end_time - start_time

    print(f"maldad({n}) = {result}")
    print(f"Tiempo de ejecución = {execution_time:.10f} segundos")

if __name__ == "__main__":
    main()
