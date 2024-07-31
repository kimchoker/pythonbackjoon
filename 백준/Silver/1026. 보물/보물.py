import sys

count = int(sys.stdin.readline().strip())
A = list(map(int, sys.stdin.readline().strip().split(' ')))
B = list(map(int, sys.stdin.readline().strip().split(' ')))

A.sort(reverse=True)
B.sort()
sumAB = 0

for i in range(count):
    sumAB += min(A) * max(B)
    A.pop()
    B.pop()

print(sumAB)