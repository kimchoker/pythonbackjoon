import sys

case_count = int(sys.stdin.readline().strip())

data = []

for i in range(case_count):
    each_case = int(sys.stdin.readline().strip())
    for o in range(each_case):
        [document, interview] = list(map(int, sys.stdin.readline().strip().split(' ')))
        data.append([document, interview])
        sorted_by_docs = sorted(document, key=lambda x: x[0])
        sorted_by_interview = sorted(document, key=lambda x: x[1])

