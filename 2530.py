h, m, s = map(int, input().split())

remain = int(input())

rH = remain // 3600  # 시간
rM = (remain % 3600) // 60  # 분
rS = (remain % 3600) % 60  # 초


h = h + rH
m = m + rM
s = s + rS

# 초가 60을 넘으면 분으로 넘겨줌
if s >= 60:
    s = s - 60
    m = m + 1
# 분이 60을 넘으면 시간으로 넘겨줌
if m >= 60:
    m = m - 60
    h = h + 1
# 시간이 24시를 넘으면 0시부터 다시 시작
if h >= 24:
    h % 24

print(h, m, s)
