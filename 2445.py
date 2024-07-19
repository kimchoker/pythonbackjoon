# 별은 정순에서 역순으로 공백은 역순에서 정순으로 출력되는 형태
# 변수의 갯수 계산을 서로 반대로 해주면 해결할 수 있다
# i 만큼 출력하느냐 number - i만큼 출력하느냐의 규칙

number = int(input())

# 공백과 별을 변수로 만듬
blank = '  '
star = '*'

# 늘어나는 별
for i in range(1, number + 1):

    # i 만큼의 별을 출력하고 number - i 만큼의 공백 출력
    print((star * i) + (blank * (number - i)) + (star * i))

# 줄어드는 별
for i in range(1, number):

    # 역순으로 줄어들어야 하기 때문에 number - i 만큼의 별을 출력 후 i 만큼의 공백 출력
    print((star * (number - i)) + (blank * i) + (star * (number - i)))