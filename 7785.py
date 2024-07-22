# 처음에 리스트로 구현했다가 시간초과

log_count = int(input())

# 회사에 들어간 인원 집계할 집합 생성
company = set()

# 이미 집합에 이름이 존재하면 존재하는 이름을 삭제
# 존재하지 않는 이름이면 집합에 저장
for _ in range(log_count):
    employee = input().split(' ')[0]

    if employee in company:
        company.remove(employee)
    else:
        company.add(employee)

# 역순으로 출력
print(" ".join(sorted(company, reverse=True)))
