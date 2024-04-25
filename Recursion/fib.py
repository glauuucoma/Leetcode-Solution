def fib(number):
    if number <= 1:
        return number
    else:
        return fib(number - 1) + fib(number - 2)
    
print(fib(5))