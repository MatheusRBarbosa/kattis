import sys

x = int(input())
qaly = 0

for i in range(x):
    numbers = input().split()
    qaly += float(numbers[0]) * float(numbers[1])

print("%.3f" % qaly)