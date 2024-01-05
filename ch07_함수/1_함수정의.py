# 함수 
def show_price(): # 함수 정의
	print('커트 가격은 10000원입니다.')

show_price() # 함수 호출

customer1 = '장경준'
print(f'{customer1}고객님')
show_price() # 함수 호출

customer2 = '장경원'
print(f'{customer2}고객님')
show_price() # 함수 호출

# >>커트 가격은 10000원입니다.
# 	장경준 고객님
# 	커트 가격은 10000원입니다.
# 	장경원 고객님
# 	커트 가격은 10000원입니다.


def open_account():
    print("새로운 계좌가 생성되었습니다.")

open_account()

