import sys

word_count = int(sys.stdin.readline().strip())

words = set(sys.stdin.readline().strip() for _ in range(word_count))

sorted_words = sorted(words, key=lambda x: (len(x), x))

for word in sorted_words:
    print(word)