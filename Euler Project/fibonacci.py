#!/usr/bin/python

def fibonacci(n):
    fib = [0] * (n+1);
    fib[0] = 0;
    fib[0] = 1;
    sum = 0;
    for i in range(2, n+1):
        fib[i] = fib[i-1] + fib[i-2]
        if fib[i] <4000000 and fib[i] % 2 == 0:
            sum = sum + fib[i] 
    return sum
n = 100
answer = fibonacci(n)
print(answer);

previous =0;
current =1;
total = 0
while True:
    previous, current = current, previous + current
    if current >= 4000000:
        break
    if current % 2 == 0:
        total += current
print(total)


