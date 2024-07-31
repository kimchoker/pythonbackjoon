import sys
# 단어 갯수 입력받기
word_count = int(sys.stdin.readline().strip())
# 중복된 단어가 있으면 안되기 때문에 set 으로 입력받아 중복 단어를 제거
words = set(sys.stdin.readline().strip() for _ in range(word_count))
# 람다 함수를 이용해 길이순으로 정렬, 길이가 같은 경우 사전순으로 정렬을 구현
sorted_words = sorted(words, key=lambda x: (len(x), x))

for word in sorted_words:
    print(word)