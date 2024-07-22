import sys
from collections import Counter

count = sys.stdin.readline()
card_list = list(map(int, sys.stdin.readline().split()))

check_count = sys.stdin.readline()
check_list = list(map(int, sys.stdin.readline().split()))

counter = Counter(card_list)
counter_dictionary = dict(counter)

answer = []

for i in range(len(check_list)):
    if check_list[i] in counter_dictionary.keys():
        answer.append(counter_dictionary.get(check_list[i]))
    else:
        answer.append(0)


print(" ".join(map(str, answer)))