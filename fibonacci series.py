def fibonacci(n):
    fib_series = []
    a, b = 0, 1
    for _ in range(n):
        fib_series.append(a)
        a, b = b, a + b
    return fib_series


n_terms = 20
print("Fibonacci series with", n_terms, "terms:")
print(fibonacci(n_terms))
