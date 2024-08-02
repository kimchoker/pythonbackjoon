import sys
from collections import defaultdict


# 친구 관계를 추가하는 함수
def add_friend(fr, to, friends):
    # 'fr'이 'to'를 친구로 추가
    if to not in friends[fr]:
        friends[fr].append(to)
    # 'to'가 'fr'을 친구로 추가 (양방향 친구 관계)
    if fr not in friends[to]:
        friends[to].append(fr)


# 친구 관계를 업데이트하고, 총 일수와 매일 새로 생긴 친구 수를 계산하는 함수
def make_friends(friends, user):
    days = 0  # 전체 일수 초기화
    daily_new_friends = []  # 매일 새로 생긴 친구 수를 저장할 리스트

    while True:
        new_relations = defaultdict(set)  # 새로 생길 친구 관계를 저장할 딕셔너리

        # 현재 모든 사람에 대해 친구 관계를 업데이트
        for i in range(1, user + 1):
            for friend in friends[i]:
                # 각 친구의 친구를 확인하여 새 친구를 찾음
                for potential_friend in friends[friend]:
                    # 현재 사람과 다른 사람이어야 하고, 이미 친구가 아니어야 함
                    if potential_friend != i and potential_friend not in friends[i]:
                        new_relations[i].add(potential_friend)

        # 더 이상 새 친구 관계가 없으면 종료
        if not any(new_relations.values()):
            break

        daily_count = 0  # 하루에 새로 생긴 친구 수 초기화
        for person, new_friends in new_relations.items():
            # 새 친구를 추가
            for new_friend in new_friends:
                add_friend(person, new_friend, friends)
                daily_count += 1

        # 하루에 새로 생긴 친구 수를 리스트에 추가
        daily_new_friends.append(daily_count // 2)  # 양방향 관계로 인해 한 쪽에서 두 번 카운트됨
        days += 1  # 일수 증가

    return days, daily_new_friends  # 총 일수와 매일 새로 생긴 친구 수 반환


def main():
    input = sys.stdin.read
    data = input().split()

    user = int(data[0])  # 사람 수
    relations = int(data[1])  # 초기 친구 관계 수

    friends = defaultdict(list)  # 사람과 친구 관계를 저장할 딕셔너리

    index = 2
    for _ in range(relations):
        A = int(data[index])
        B = int(data[index + 1])
        index += 2
        add_friend(A, B, friends)  # 친구 관계 추가

    days, daily_new_friends = make_friends(friends, user)  # 친구 관계 업데이트 및 결과 계산

    print(days)  # 총 일수 출력
    for count in daily_new_friends:
        print(count)  # 매일 새로 생긴 친구 수 출력


if __name__ == "__main__":
    main()
