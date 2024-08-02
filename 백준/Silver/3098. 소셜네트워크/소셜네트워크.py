import sys
from collections import defaultdict

def add_friend(fr, to, friends):
    if to not in friends[fr]:
        friends[fr].append(to)
    if fr not in friends[to]:
        friends[to].append(fr)

def make_friends(friends, N):
    days = 0
    daily_new_friends = []

    while True:
        new_relations = defaultdict(set)

        # 새로 추가될 친구 관계를 찾아낸다
        for person in range(1, N + 1):
            for friend in friends[person]:
                for potential_friend in friends[friend]:
                    if potential_friend != person and potential_friend not in friends[person]:
                        new_relations[person].add(potential_friend)

        if not any(new_relations.values()):
            break

        daily_count = 0
        for person, new_friends in new_relations.items():
            for new_friend in new_friends:
                add_friend(person, new_friend, friends)
                daily_count += 1
        
        daily_new_friends.append(daily_count // 2)  # Since each relation is counted twice
        days += 1
    
    return days, daily_new_friends

def main():
    input = sys.stdin.read
    data = input().split()
    
    N = int(data[0])
    M = int(data[1])
    
    friends = defaultdict(list)
    
    index = 2
    for _ in range(M):
        A = int(data[index])
        B = int(data[index + 1])
        index += 2
        add_friend(A, B, friends)
    
    days, daily_new_friends = make_friends(friends, N)
    
    print(days)
    for count in daily_new_friends:
        print(count)

if __name__ == "__main__":
    main()
