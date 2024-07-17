# 두 번 나온 애들 중에서 긴 것에서 짧은 것을 빼주면 됨
# 입력되지 않은 부분이 더 길어도 어짜피 입력 된 것 안에서만 빼주면 되기 때문에 헷갈일 일이 없다.


melon = int(input())

length = []
c1 = 0
c2 = 0
c3 = 0
c4 = 0

for i in range(6):
    length.append(list(map(int, input().split())))


for i in range(6):
    if length[i][0] == 1:
        c1 += 1
    elif length[i][0] == 2:
        c2 += 1
    elif length[i][0] == 3:
        c3 += 1
    elif length[i][0] == 4:
        c4 += 1
