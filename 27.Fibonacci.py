# f(n) = f(n-1) + f(n-2)
def fibonacci(n):
    if n ==1:
        return 1
    if n == 2:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)

if __name__ == '__main__':
    print fibonacci(9)
    