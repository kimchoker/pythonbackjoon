from collections import Counter

file_count = int(input())

# 확장자 파일을 받을 리스트 생성
extension_count = []

# 파일 이름은 중요하지 않으므로 . 앞의 정보는 .split() 으로 버리고 확장자만 리스트에 추가
for _ in range(file_count):
    extension_count.append(input().split('.')[1])

# counter 메소드로 각 확장자가 몇 번 씩 등장했는지 카운트
counter = Counter(extension_count)

# counter 의 .key() 메소드를 이용해 확장자의 이름과 횟수가 같이 있는 counter 에서 이름만 가져온 뒤 sort()로 사전순 정렬
sorted_extension = sorted(counter.keys())

# 출력해주기
for extension in sorted_extension:
    print(f"{extension} {counter[extension]} ")