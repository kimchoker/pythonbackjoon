import itertools

point, length = map(int, input().split())
numbers = list(range(1, point + 1))
sequences = itertools.permutations(numbers, length)

for sequence in sequences:
    print(' '.join(map(str, sequence)))