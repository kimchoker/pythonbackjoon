import sys
from collections import deque

test_case = int(sys.stdin.readline().strip())

for i in range(test_case):
    word_count, word_length, rhyme_length = map(int, sys.stdin.readline().strip().split())
    words = deque(sys.stdin.readline().strip().split())
    count = 0

    while words:
        # 덱의 첫 번째 요소를 pop
        first_word = words.popleft()
        # pop 해온 요소의 접미사와 같은 요소(.endswith())를 찾아 filtered에 담음
        filtered = [word for word in words if word and word.endswith(first_word[-rhyme_length:])]
        # filtered가 비어있지 않으면 = 쌍이 될 수 있는 요소가 있으면
        if filtered:
            # 카운트를 한 개 올려줌
            count += 1
            # 쌍이 될 수 있는 요소가 아무리 많다고 해도 한 번밖에 사용할 수 없으므로 pop
            used = filtered.pop()
            # filtered에서 사용된 요소를 words에서 제거
            words.remove(used)

    print(count)
