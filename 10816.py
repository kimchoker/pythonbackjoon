import sys
from collections import Counter

line = sys.stdin.readline()

count = line
card_list = list(map(int, line.split()))

check_count = line
checklist = list(map(int, line.split()))

# 카운터 메소드를 이용해 숫자: 빈도 를 딕셔너리에 저장
counter = Counter(card_list)
dictionary = dict(counter)

frequencies = []

# 체크리스트에 있는 숫자가 딕셔너리의 key 값에 존재하면 그 key 값의 value (출현 빈도)를 frequencies 에 저장
for i in range(len(checklist)):
    if checklist[i] in dictionary.keys():
        frequencies.append(dictionary.get(checklist[i]))
    else:
        frequencies.append(0)


print(" ".join(map(str, frequencies)))