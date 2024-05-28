def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

n = int(input("Enter the number of Fibonacci numbers to generate: "))
gen = fibonacci_generator()
fib_sequence = [next(gen) for _ in range(n)]
print(fib_sequence)
