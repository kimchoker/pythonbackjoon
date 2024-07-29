import sys
# 입력받기
word_count = int(input())
# 단어를 글자로 나눠서 리스트 안의 리스트로 나누기
words = [list(sys.stdin.readline().strip()) for _ in range(word_count)]
# 비교를 위해 리스트의 요소를 전부 뒤집은 리스트 만들기
reversed_words = list(map(lambda x: list(reversed(x)), words))

# 뒤집었을 때 같은 요소가 무조건 있어야 함(정방향 역방향이 하나씩 들어있으므로)
# 있으면 출력 후 break
for i in range(word_count):
    if words.__contains__(reversed_words[i]):
        print(f'{len(reversed_words[i])} {reversed_words[i][len(reversed_words[i]) // 2]}')
        break
