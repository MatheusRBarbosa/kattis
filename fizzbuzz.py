import sys

numbers = list(map(int, input().split()))
n  = 1
while n <= numbers[2]: 
    r = ''
    f = 0
    if n % numbers[0] == 0: r += 'Fizz'
    else: f += 1

    if n % numbers[1] == 0: r += 'Buzz'
    else: f += 1

    if(f == 2): print(n)
    else: print(r)

    n += 1