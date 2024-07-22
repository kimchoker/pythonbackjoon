a, b, c = map(int, input().split())

if a == b == c:
    print(10000 + a * 1000)

elif a == b or b == c or a == c:
    if a == b:
        same = a
    elif b == c:
        same = b
    elif a == c:
        same = c
    print(1000 + (same * 100))
else:
    print(max(a, b, c) * 100)
