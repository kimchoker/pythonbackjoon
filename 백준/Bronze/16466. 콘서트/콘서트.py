import sys

# 1차 티켓팅에서 팔린 티켓들의 수를 입력받습니다.
num_count = int(input().strip())

# 1차 티켓팅에서 팔린 티켓들의 번호를 입력받아 집합으로 만듭니다.
sold = set(map(int, sys.stdin.readline().strip().split()))

# 1번부터 차례대로 확인하여 가장 작은 사용 가능한 티켓 번호를 찾습니다.
ticket_number = 1
while ticket_number in sold:
    ticket_number += 1

# 결과 출력
print(ticket_number)
