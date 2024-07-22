from collections import Counter


word = input().upper()

counter = Counter(word).most_common(2)


if len(counter) > 1 and counter[0][1] == counter[1][1]:
    print('?')

else:
    print(counter[0][0])