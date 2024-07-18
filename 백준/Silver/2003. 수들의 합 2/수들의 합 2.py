length, number = map(int, input().split())

sequence = list(map(int, input().split()))

start = 0
end = 0
sum = 0
count = 0

while end < length:
    
    sum += sequence[end]
    
    while sum > number and start <= end:
        sum -= sequence[start]
        start += 1
   
    if sum == number:
        count += 1

    end += 1

print(count)