import sys

case_count = int(input())
schools = {}
for i in range(case_count):
    school_count = int(input())
    for s in range(school_count):
        key, value = sys.stdin.readline().split(' ')
        schools[key] = int(value)

    tuples = [(key, value) for key, value in schools.items()]

    sorted_tuples = sorted(tuples, key=lambda x: x[1], reverse=True)

    print(sorted_tuples[0][0])
    schools.clear()