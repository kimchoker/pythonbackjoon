number = int(input())

blank = '  '
star = '*'

for i in range(1, number + 1):

    print((star * i) + (blank * (number - i)) + (star * i))

for i in range(1, number):

    print((star * (number - i)) + (blank * i) + (star * (number - i)))