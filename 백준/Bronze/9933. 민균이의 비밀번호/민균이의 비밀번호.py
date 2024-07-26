import sys

word_count = int(input())

words = [list(sys.stdin.readline().strip()) for _ in range(word_count)]

reversed_words = list(map(lambda x: list(reversed(x)), words))

for i in range(word_count):
    if words.__contains__(reversed_words[i]):
        print(f'{len(reversed_words[i])} {reversed_words[i][len(reversed_words[i]) // 2]}')
        break
