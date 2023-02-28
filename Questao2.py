def sequenciaFibonacci(n):
    a, b = 0, 1
    while a < n:
        a, b = b, a + b
    if a==n:
        print("Esse número pertence a sequência de Fibonacci")
    else:
        print("Esse número não pertence a sequência de Fibonacci")


numero = 7
sequenciaFibonacci(numero)





