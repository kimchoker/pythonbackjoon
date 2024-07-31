import sys

num_count = int(input())

sold = set(map(int, sys.stdin.readline().strip().split(' ')))

min_range = set(range(1, max(sold) + 1))
remain = min_range - sold

if not remain:
    print(max(min_range) + 1)
else:
    print(min(remain))
