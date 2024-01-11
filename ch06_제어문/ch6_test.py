# 1
from random import *
cnt = 0 # 총 탑승 승객 수
for i in range(1,51): # 1 ~ 50 이라는 수 (승객)
    time = randrange(5,51) # 5분 ~ 50분 소요 시간
    if 5 <= time <= 15: # 5분 ~ 15분 이내의 손님, 탑승 승객 수 증가 처리
        print("[0] {0}번째 손님 (소요시간 : {1}분)".format(i, time))
        cnt += 1
    else:
        print("[ ] {0}번째 손님 (소요시간 : {1}분)".format(i,time))

print("총 탑승 승객: {0} 분".format(cnt))


# 2
import random

cnt = 0
for i in range(1,51):
    time = random.randrange(5,51)
    if 5 <= time <= 15:
        print(f'[O] {i}번째 손님 (소요시간 : {time}분)')
        cnt += 1
    else:
        print(f'[ ] {i}번째 손님 (소요시간 : {time}분)')
print(f'총 탑승객 : {cnt}명')

# 3
price = 1000
goods = 6
total = 0
for i in range (1, goods + 1):
    print("2+1 상품입니다.")
    if i % 3 == 0:
        continue
    total += price

print("총 가격은 "+ str(total) + "원입니다.")