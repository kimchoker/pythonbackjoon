import itertools

point, length = map(int, input().split())

# 기준점이 되는 숫자와 그 아래의 숫자로 이루어진 리스트를 생성
numbers = list(map(int, input().split()))

sequences = itertools.permutations(numbers, length)

# 중복값을 허용하지 않는 set 생성
distinct_sequences = set()

# 같은 값을 제거하기 위해 set 에 집어넣음
for sequence in sequences:
    distinct_sequences.add(tuple(sequence))

# 고유값만 남은 set 을 list 로 바꾸어 정렬이 가능하도록 만들고, 오름차순으로 정렬
sorted_distinct_sequences = sorted(list(distinct_sequences))

for sequence in sorted_distinct_sequences:
    print(' '.join(map(str, sequence)))