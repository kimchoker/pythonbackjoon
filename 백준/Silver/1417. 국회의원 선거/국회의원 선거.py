import sys

candidate_count = int(input())
dasom = int(input())
expected_votes = [int(sys.stdin.readline().strip()) for _ in range(candidate_count - 1)]
corruptionFund = 0

if candidate_count > 1:
    while dasom <= max(expected_votes):
        index, value = max(enumerate(expected_votes), key=lambda x: x[1])
        dasom += 1
        expected_votes[index] = value - 1
        corruptionFund += 1

print(corruptionFund)
