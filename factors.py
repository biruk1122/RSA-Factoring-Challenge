#!/usr/bin/python3
import sys

def factorize(n):
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            return i, n // i
    return None

if len(sys.argv) != 2:
    print("Usage: factors <file>")
    sys.exit(1)

input_file = sys.argv[1]

try:
    with open(input_file, 'r') as file:
        for line in file:
            n = int(line.strip())
            factors = factorize(n)
            if factors:
                p, q = factors
                print(f"{n}={p}*{q}")

except FileNotFoundError:
    print(f"Error: File '{input_file}' not found.")
except ValueError:
    print("Error: Invalid input in the file. All lines should be valid natural numbers greater than 1.")
