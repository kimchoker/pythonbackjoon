# # 수열의 길이와 만들어야하는 숫자를 받음
# length, number = map(int, input().split())
#
# # 입력된 수열을 배열로 변환
# sequence = list(map(int, input().split()))
#
# # 같은 수가 몇 번 나올지 확인할 변수를 생성
# count = 0
#
# # i부터 j 까지의 합을 확인해줄 변수 생성
# for i in range(length):
#     sum = 0
#
#     # 배열 안에서의 합 계산
#     for o in range(i, length):
#         sum = sum + sequence[o]
#         if sum == number:
#             count += 1
#             break
#
#
# print(count)


# 수열의 길이와 목표 숫자를 입력받음
length, number = map(int, input().split())

# 수열을 입력받아 리스트로 변환
sequence = list(map(int, input().split()))

# 투 포인터 초기화
start = 0
end = 0
sum = 0
count = 0

while end < length:
    # sum에 수열의 end번째 요소를 더함
    sum += sequence[end]

    # sum이 목표 숫자보다 크면 start를 이동하여 sum을 줄임
    while sum > number and start <= end:
        sum -= sequence[start]
        start += 1

    # current_sum이 목표 숫자와 같으면 count를 증가시킴
    if sum == number:
        count += 1

    # end를 이동하여 다음 요소를 확인
    end += 1

print(count)
