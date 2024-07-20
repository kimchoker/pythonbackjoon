from collections import Counter

file_count = int(input())
extension_count = []

for _ in range(file_count):
    extension_count.append(input().split('.')[1])

counter = Counter(extension_count)
sorted_extension = sorted(counter.keys())

for extension in sorted_extension:
    print(f"{extension} {counter[extension]} ")