#!/usr/bin/python3
import sys

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def factorize(n):
    for i in range(2, n + 1):
        if n % i == 0 and is_prime(i):
            j = n // i
            if is_prime(j):
                return i, j
    return None

if len(sys.argv) != 2:
    print("Usage: rsa <file>")
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
            else:
                print(f"Unable to factorize {n} into two prime numbers.")

except FileNotFoundError:
    print(f"Error: File '{input_file}' not found.")
except ValueError:
    print("Error: Invalid input in the file. The file should contain a single integer.")
