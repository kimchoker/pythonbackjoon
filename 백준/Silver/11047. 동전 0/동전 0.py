import sys

coin_count, money = map(int, sys.stdin.readline().strip().split())

coins = []
count = 0

for i in range(coin_count):
    cur_coin = int(sys.stdin.readline().strip())
    coins.append(cur_coin)

# 오름차순으로 들어온 동전을 역순으로 처리 (큰 동전부터 사용)
while money > 0:
    for coin in reversed(coins):
        if coin <= money:
            count += money // coin
            money %= coin
            break  # 한번 처리했으면 바로 나가서 다시 큰 동전부터 확인

print(count)
