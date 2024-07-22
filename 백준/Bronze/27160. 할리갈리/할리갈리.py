count = int(input())

input_data = []

cards = [['STRAWBERRY', 0], ['BANANA', 0], ['LIME', 0], ['PLUM', 0]]


for i in range(count):
    input_data.append(list(input().split(' ')))

def update_card_value(samples, data):
    for fruit, value in data:
        value = int(value)
        for sample in samples:
            if sample[0] == fruit:
                sample[1] += value


update_card_value(cards, input_data)

if any(card[1] == 5 for card in cards):
    print('YES')
else:
    print('NO')