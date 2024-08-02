import sys

case_count = int(sys.stdin.readline().strip())

for i in range(case_count):
    country, airplane = sys.stdin.readline().split(' ')
    airplanes = [sys.stdin.readline().strip().split(' ') for _ in range(int(airplane))]
    print(int(country) - 1)