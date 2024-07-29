import sys
# 후보자 수
candidate_count = int(input())

# 다솜의 예상 득표수
dasom = int(input())

# 나머지 후보들의 예상 득표수
expected_votes = [int(sys.stdin.readline().strip()) for _ in range(candidate_count - 1)]

# 비겁한 매수 횟수
bribery = 0

if candidate_count > 1:
    while dasom <= max(expected_votes):
        # max 값을 구해서 가장 큰 수를 우선으로 1씩 빼주는 형태로 구현
        # max 값을 구할 때 max 값의 인덱스도 함께 구해야하기 때문에 enumerate 를 이용
        # index, value 형태의 튜플로 값을 구한다
        index, value = max(enumerate(expected_votes), key=lambda x: x[1])
        dasom += 1
        # 구한 index 값을 이용 list 의 요소 업데이트
        expected_votes[index] = value - 1
        bribery += 1

print(bribery)
