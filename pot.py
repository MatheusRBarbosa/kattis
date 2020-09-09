import sys

lines = int(input())
total = 0
for i in range(lines):
    number = str(input())

    pow = number[-1]
    number = number[:-1]

    total += int(number)**int(pow)
print(total)