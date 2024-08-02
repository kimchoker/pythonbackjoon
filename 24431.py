# 접근방법
# 한 단어는 조합에서 한 번 밖에 사용할 수 없다.
# -> 쌍이 될 수 있는 요소 중에서 어느 것과 짝을 짓고 그 요소를 제거해도 상관 없음
# 어짜피 라임은 같기 때문에 쌍을 짓는 것이 가능하다면, 남은 요소들에서 쌍을 지을 수 있기 때문
# 쌍을 지은 요소는 제거

import sys
from _collections import deque

test_case = int(sys.stdin.readline().strip())

for i in range(test_case):
    # 단어 수, 단어 길이, 라임 길이
    word_count, word_length, rhyme_length = map(int, sys.stdin.readline().strip().split())
    # 성능 저하 예방을 위해서 deque 자료구조 사용(근데 시간차이가 안나네요?)
    words = deque(sys.stdin.readline().strip().split())
    # 쌍의 수를 계산해 줄 count
    count = 0

    for _ in range(len(words)):
        # 덱이 비어있으면 break
        if not words:
            break
        # 덱의 첫 번째 요소를 pop
        first_word = words.popleft()
        # pop 해온 요소의 접미사와 같은 요소(.endswith()) 를 찾아 filtered 에 담음
        filtered = [word for word in words if word and word.endswith(first_word[-rhyme_length:])]
        # filtered 가 비어있지 않으면 = 쌍이 될 수 있는 요소가 있으면
        if filtered:
            # 카운트를 한개 올려줌
            count += 1
            # 쌍이 될 수 있는 요소가 아무리 많다고 해도 한 번 밖에 사용할 수 없으므로 pop
            used = filtered.pop()
            # filtered 에서 사용된 요소를 words 에서도 제거
            words.remove(used)

    print(count)

