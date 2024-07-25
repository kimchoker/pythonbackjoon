import itertools

point, length = map(int, input().split())

# 기준점이 되는 숫자와 그 아래의 숫자로 이루어진 리스트를 생성
numbers = list(range(1, point + 1))

# itertools 의 .permutations() 를 이용
# 요소와 길이를 알려주면 겹치지 않는 수열을 만들어준다
sequences = itertools.permutations(numbers, length)

for sequence in sequences:
    print(' '.join(map(str, sequence)))