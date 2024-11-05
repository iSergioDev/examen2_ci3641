import time
# import matplotlib.pyplot as plt

# Pregunta a, Recursión
def fibonacci(n, alpha=7, beta=4):
    if 0 <= n < alpha * beta:
        return n
    else:
        return sum(fibonacci(n - beta * i, alpha, beta) for i in range(1, alpha + 1))


# Pregunta b, Recursión por cola
def fibonacci_tail(n, alpha=7, beta=4):
    def aux(n, acc):
        if 0 <= n < alpha * beta:
            return n + acc
        else:
            total = acc
            for i in range(1, alpha + 1):
                total += aux(n - beta * i, 0)
            return total
    
    return aux(n, 0)


# Pregunta c, Ciclo iterativo
def fibonacci_iterative(n, alpha=7, beta=4):
    limit = alpha * beta
    # Crear un arreglo para almacenar resultados
    results = [0] * (n + 1)

    for i in range(n + 1):
        if 0 <= i < limit:
            results[i] = i  # Caso base
        else:
            # Sumar los resultados de los índices relevantes
            results[i] = sum(results[i - beta * j] for j in range(1, alpha + 1) if (i - beta * j) >= 0)

    return results[n]


n_values = range(28, 140, 2)
recursive_times = []
tail_recursive_times = []
iterative_times = []

for n in n_values:
    start_time = time.time()
    fibonacci(n)
    recursive_times.append(time.time() - start_time)

    start_time = time.time()
    fibonacci_tail(n)
    tail_recursive_times.append(time.time() - start_time)

    start_time = time.time()
    fibonacci_iterative(n)
    iterative_times.append(time.time() - start_time)

# Graficar los resultados
plt.plot(n_values, recursive_times, label='Función Recursiva')
plt.plot(n_values, tail_recursive_times, label='Función Recursiva de Cola')
plt.plot(n_values, iterative_times, label='Functión Iterativa')
plt.xlabel('Valor de n')
plt.ylabel('Tiempo (segundos)')
plt.title('Comparación de Tiempos de Ejecución')
plt.legend()
plt.show()
