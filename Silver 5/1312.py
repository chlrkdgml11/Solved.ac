import sys

A, B, N = map(int, sys.stdin.readline().split())

for _ in range(N):
    A = (A % B) * 10
    result = A // B

print(result)
