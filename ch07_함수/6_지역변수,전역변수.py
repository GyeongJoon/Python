gun = 10

def checkpoint(soldiers): # 경계근무
    global gun # 전역 공간에 있는 gun 사용
    gun = gun - soldiers
    print("[함수 내] 남은 총 : {0}".format(gun))
# 지역변수
def secret():
	message = '이건 나만의 비밀' # secret 함수 내에서 정의
	print(message) # 값 출력 가능
	message = '함수 내에서는 자유롭게 수정이 가능해요'

def please():
	message = '이렇게 하면 되지?'
print(message)

# 각 함수에 있는 message는 다름

# 전역변수
def secret():
	message = '이건 나만의 비밀' # secret 함수 내에서 정의
	print(message) # 값 출력 가능
	message = '함수 내에서는 자유롭게 수정이 가능해요'

def please():
	message = '이렇게 하면 되지?'
print(message)

# 각 함수에 있는 message는 다름


def checkpoint_ret(gun, soldiers):
    gun = gun - soldiers
    print("[함수 내] 남은 총 : {0}".format(gun))
    return gun

print("전체 총 : {0}".format(gun))
# checkpoint(2) # 2명이 경계근무 나감
gun = checkpoint_ret(gun,2)
print("남은 총 : {0}".format(gun))

gun = 10
def checkpoint(gun, soldieres):
    gun = gun - soldieres
    print("[함수 내] 남은 총 :{0}".format(gun))
    return gun

print("전체총: {0}".format(gun))
gun = checkpoint(gun, 2)
print("남은 총: {0}".format(gun))