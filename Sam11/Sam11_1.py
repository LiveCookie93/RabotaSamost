def fib(n):
    fib0 = 1
    yield fib0
    fib1 = 1
    yield fib1
    for i in range(n - 2):
        fib0, fib1 = fib1, fib0 + fib1
        yield fib1


# Тест
for num in fib(20):
    pass
print(num)