import sys

for line in sys.stdin:
    numbers = line.split()
    result = abs(int(numbers[0]) - int(numbers[1]))
    print(result)