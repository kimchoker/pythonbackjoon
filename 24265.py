
def MenOfPassion(A, n):
    sum_value = 0
    count = 0
    for i in range(1, n):
        for j in range(i + 1, n + 1):
            sum_value += A[i] * A[j]
            count += 1
    return sum_value, count


number = int(input())


