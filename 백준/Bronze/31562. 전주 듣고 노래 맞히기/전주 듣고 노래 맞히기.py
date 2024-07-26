import sys
from collections import defaultdict

# 입력 받기
known, try_count = map(int, input().split())

# 노래 정보 저장 딕셔너리
song_dict = defaultdict(list)

# 노래 데이터 입력
for _ in range(known):
    parts = sys.stdin.readline().split()
    title = parts[1]
    notes = parts[2:9]
    key = tuple(notes[:3])  # 첫 3개의 음을 키로 사용
    song_dict[key].append(title)

# 시도 데이터 입력 및 처리
for _ in range(try_count):
    query = tuple(sys.stdin.readline().split())
    if query in song_dict:
        titles = song_dict[query]
        if len(titles) == 1:
            print(titles[0])
        elif len(titles) > 1:
            print('?')
        else:
            print('!')
    else:
        print('!')
