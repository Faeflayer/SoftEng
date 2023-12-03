def fib(n):
    a, b = 1, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

if __name__ == '__main__':
    for i in fib(200):
        print(i)
