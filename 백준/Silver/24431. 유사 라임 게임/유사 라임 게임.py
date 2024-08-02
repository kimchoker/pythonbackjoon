import sys

test_case = int(sys.stdin.readline().strip())

for i in range(test_case):
    word_count, word_length, rhyme_length = map(int, sys.stdin.readline().strip().split())
    words = sys.stdin.readline().strip().split()
    count = 0

    for _ in range(len(words)):
        if not words:
            break
        first_word = words.pop(0)
        # print(first_word)
        filtered = [item for item in words if item and item.endswith(first_word[-rhyme_length:])]
        if filtered:
            count += 1
            popped = filtered.pop()
            words.remove(popped)

    print(count)
