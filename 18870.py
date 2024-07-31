import sys
# 좌표의 수
coordinates_count = int(sys.stdin.readline().strip())

# 좌표가 모인 리스트
coordinates = list(map(int, sys.stdin.readline().strip().split(' ')))

# [원래 인덱스, 값] 의 형태를 가지도록 변환
origin = [[index, value] for index, value in enumerate(coordinates)]

# 값을 기준으로 정렬
origin.sort(key=lambda x: x[1])

# 중복값이 있었는지 저장해 줄 딕셔너리
dictionary = {}

# 압축된 좌표의 번호를 지정할 변수 생성
compressed_number = 0


for i in range(len(origin)):
    current = origin[i][1]
    # 현재 값이 딕셔너리에 없으면
    if current not in dictionary:
        # 딕셔너리에 값 : 압축된 값 으로 저장
        dictionary[current] = compressed_number
        # 오리진 배열의 요소를 압축된 값으로 변경
        origin[i][1] = compressed_number
        # 압축된 값이 사용되었으므로 다음 값으로 넘김
        compressed_number += 1
    # 현재 값이 딕셔너리에 있다면
    elif current in dictionary:
        # 딕셔너리의 키(원래 값)로 압축된 값을 불러와 요소 업데이트
        origin[i][1] = dictionary[current]

# 바뀐 값을 원래의 인덱스를 기준으로 재정렬
origin.sort(key=lambda x: x[0])

# key, value 형태에서 value 부분만 불러와서 저장
compressed = [str(value) for index, value in origin]

# 출력
print(' '.join(compressed))