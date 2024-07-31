import sys

# 실행 횟수를 받고 학교 딕셔너리 만듬
case_count = int(input())
schools = {}

# 실행 횟수만큼
for i in range(case_count):

    # 실행 횟수마다 들어오는 학교의 수
    school_count = int(input())

    # 들어오는 학교의 수만큼
    for s in range(school_count):
        # 딕셔너리에 넣기 위해 키, 밸류 형태로
        key, value = sys.stdin.readline().split(' ')
        # 들어오는 값은 문자열이므로 밸류를 숫자로 바꿈
        schools[key] = int(value)
    # 딕셔너리에 있는 값을 키, 밸류 형태의 튜플로 바꾸고 정렬을 위해 리스트 안에 넣어줌
    tuples = [(key, value) for key, value in schools.items()]
    # 튜플로 바꾼 값을 sorted() 를 통해 정렬(내림차순 reversed = True)
    sorted_tuples = sorted(tuples, key=lambda x: x[1], reverse=True)

    # 정렬된 값 중 가장 앞에 있는 값을 출력(내림차순이므로)
    print(sorted_tuples[0][0])
    # 실행횟수가 끝났으므로 딕셔너리를 비움
    schools.clear()