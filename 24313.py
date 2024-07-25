import itertools

point, length = map(int, input().split())

numbers = list(range(1, point + 1))

sequences = itertools.permutations(numbers, length)

# 중복값을 허용하지 않는 set 생성
distinct_sequences = set()

# 튜플 안의 요소를 사전순으로 정렬한 뒤 set 넣음
# (1, 2) (2, 1) 과 같은 요소를 정렬하여 같은 (1, 2)로 만들고 set 에 넣어 제거하기 위함
for sequence in sequences:
    distinct_sequences.add(tuple(sorted(sequence)))

# 고유값만 남은 set 을 list 로 바꾸어 정렬이 가능하도록 만들고, 오름차순으로 정렬
sorted_distinct_sequences = sorted(list(distinct_sequences))

for sequence in sorted_distinct_sequences:
    print(' '.join(map(str, sequence)))