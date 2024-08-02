import sys

book_count, carry_once = map(int, sys.stdin.readline().strip().split(' '))
points = list(map(int, sys.stdin.readline().strip().split(' ')))

points.sort()

print(points)