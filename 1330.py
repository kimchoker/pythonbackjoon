# 입력을 받기 위한 input()
# 공백을 기준으로 두 수가 입력되기 때문에 .split()으로 두 수로 나누어 준다
# input()으로 들어오는 값은 기본적으로 문자이기 때문에 int로 선언해주어 숫자로 바꿔준다

a, b = map(int, input().split())

if a > b:
    print('>')
elif a < b:
    print('<')
elif a == b:
    print('==')