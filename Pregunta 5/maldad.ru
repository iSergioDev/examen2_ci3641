# Importamos el módulo Math para acceder a funciones matemáticas
require 'bigdecimal'

# Función para calcular el Coeficiente Binomial
def binomial_coefficient(n, k)
  a_solutions = Array.new(k)
  a_solutions[0] = n - k + 1

  (1...k).each do |i|
    a_solutions[i] = a_solutions[i - 1] * (n - k + 1 + i) / (i + 1)
  end

  a_solutions[k - 1]
end

# Función para calcular el número de Narayana
def narayana(n, k)
  (1.0 / n) * binomial_coefficient(n, k) * binomial_coefficient(n, k - 1)
end

# Función iterativa para calcular el número de Tribonacci
def tribonacci_iterative(n)
  return 0 if n == 0
  return 1 if n == 1
  return 2 if n == 2

  a, b, c = 0, 1, 2
  (3..n).each do
    next_value = a + b + c
    a = b
    b = c
    c = next_value
  end

  c
end

# Función que calcula la "maldad"
def maldad(n)
  k = Math.log(n, 2).floor
  n_n_k = narayana(n, k)
  log_value = Math.log(n_n_k, 2).floor

  tribonacci_iterative(log_value + 1)
end

# Entrada del usuario o judge
n = gets.to_i

# Medición del tiempo de ejecución
start_time = Time.now
result = maldad(n)
end_time = Time.now

# Cálculo del tiempo de ejecución
execution_time = end_time - start_time

# Salida
puts "maldad(#{n}) = #{result}"
puts "Tiempo de ejecución = #{'%.10f' % execution_time} segundos"
