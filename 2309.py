import sys

height = [int(sys.stdin.readline().strip()) for _ in range(9)]

# 전체 합에서 100을 뺀 값이 제거해야 할 두 난쟁이의 키의 합임
timid = sum(height) - 100

# 2중 for 문으로 돌면서 두 비겁자들의 키를 찾아준다
found = False
for i in range(9):
    for j in range(i + 1, 9):
        if height[i] + height[j] == timid:
            suspect1, suspect2 = height[i], height[j]
            found = True
            break
    if found:
        break

# 찾은 두 난쟁이의 키를 리스트에서 제거
height.remove(suspect1)
height.remove(suspect2)

# 정렬하여 출력
height.sort()
for dwarf in height:
    print(dwarf)
