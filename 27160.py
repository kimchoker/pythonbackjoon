# 카드의 갯수 입력받기
count = int(input())

# 입력받은 카드를 저장할 리스트
input_data = []

# 입력받은 카드의 값의 총합을 계산해줄 cards
cards = [['STRAWBERRY', 0], ['BANANA', 0], ['LIME', 0], ['PLUM', 0]]


for i in range(count):
    input_data.append(list(input().split(' ')))


# 두 리스트의 값을 비교해서 각 카드의 값을 합해줌
def update_card_value(samples, data):
    for fruit, value in data:
        value = int(value)
        for sample in samples:
            if sample[0] == fruit:
                sample[1] += value


update_card_value(cards, input_data)

# cards 안에 5가 있는지 확인 후 있으면 yes, 없으면 no 출력
if any(card[1] == 5 for card in cards):
    print('YES')
else:
    print('NO')