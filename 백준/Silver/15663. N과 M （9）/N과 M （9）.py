import itertools

point, length = map(int, input().split())
numbers = list(map(int, input().split()))
sequences = itertools.permutations(numbers, length)
distinct_sequences = set()

for sequence in sequences:
    distinct_sequences.add(tuple(sequence))

sorted_distinct_sequences = sorted(list(distinct_sequences))

for sequence in sorted_distinct_sequences:
    print(' '.join(map(str, sequence)))