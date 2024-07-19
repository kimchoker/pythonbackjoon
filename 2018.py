number = int(input())
half = number // 2 + 5
end = 1
sum = 0
count = 1

for start in range(0, half):
    while sum < number and end < half:
        sum += end
        end += 1
    if sum == number:
        print(end)
        count += 1
    sum -= (end - start)

print(count)

