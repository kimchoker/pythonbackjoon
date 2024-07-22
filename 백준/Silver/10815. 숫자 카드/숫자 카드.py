sCount = int(input())
sCard_input = input().split()

sCard_set = set(int(num) for num in sCard_input)

fCount = int(input())
fCard_input = input().split()

fCard_list = [int(num) for num in fCard_input]

isExist = []

for i in range(0, len(fCard_list)):
    if fCard_list[i] in sCard_set:
        isExist.append(1)
    else:
        isExist.append(0)

print(" ".join(map(str, isExist)))