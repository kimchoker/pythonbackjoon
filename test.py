import sys

# 표준 입력에서 데이터를 한 번에 받아옵니다.
input_data = sys.stdin.read()

# 받아온 입력을 줄 단위로 나눠 리스트로 만듭니다.
lines = input_data.strip().split('\n')

# 첫 번째 줄에서 column과 row를 추출합니다.
column, row = map(int, lines[0].split())

# 입력된 데이터에서 각 줄을 역순으로 출력합니다.
for line in lines[1:1+column]:
    print(line[::-1])
