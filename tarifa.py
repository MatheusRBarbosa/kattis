import sys

max = int(input())
n = int(input())
total = 0

for p in range(n):
    total += int(input())

print((n * max) - total + max)