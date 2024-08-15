def minimize_expression(expression):
    # '-'로 구분하여 각 구간을 나눔
    parts = expression.split('-')
    
    # 첫 번째 구간의 값을 계산
    initial_sum = sum(map(int, parts[0].split('+')))
    
    # 나머지 구간의 값을 계산하고 빼기
    result = initial_sum
    for part in parts[1:]:
        sum_in_part = sum(map(int, part.split('+')))
        result -= sum_in_part
    
    return result

# 입력을 받아 처리
import sys
input = sys.stdin.read
expression = input().strip()
print(minimize_expression(expression))
