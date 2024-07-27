word = input().strip()
parts = set()

for i in range(len(word)):
    for o in range(1, len(word) - i + 1):
        parts.add(word[i:i+o])


print(len(parts))

