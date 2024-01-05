# 전달값
def show_price(customer): # 함수 정의
	print(f'{customer}고객님')
	print('커트 가격은 10000원입니다.')

customer1 = '장경준'
show_price(customer1) # 함수 호출

customer2 = '장경원'
show_price(customer2) # 함수 호출

# >>장경준 고객님
# 	커트 가격은 10000원입니다.
# 	장경원 고객님
# 	커트 가격은 10000원입니다.

# 반환값
def get_price(is_vip): # True: 단골 손님, False: 일반 손님
	if is_vip == True:
		return 10000 # 단골 손님
	else:
		return 15000 # 일반 손님

price = get_price(True)
print(f'커트 가격은 {price}원입니다.') # 10000

price = get_price(False)
print(f'커트 가격은 {price}원입니다.') # 15000


def open_account():
    print("새로운 계좌가 생성되었습니다.")

def deposit(balance, money): # 입금
    print("입금이 완료되었습니다. 잔액은 {0} 원입니다.".format(balance + money))
    return balance + money

def withdraw(balance, money): # 출금
    if balance >= money: #잔액이 출금보다 많으면
        print("출금이 완료되었습니다. 잔액은 {0} 원입니다.".format(balance - money))
        return balance - money
    else: # 잔액이 출금보다 적으면
        print("출금이 완료되지 않았습니다. 잔액은 {0} 원입니다.".format(balance))

def withdraw_night(balance, money): # 저녁에 출금
    commission = 100 # 수수료 100원
    return commission, balance - money - commission

balance = 0 # 잔액
balance = deposit(balance, 1000)
# balance = withdraw(balance,2000)
commission ,balance = withdraw_night(balance,500)
print("수수료 {0} 원이며, 잔액은 {1} 원입니다.".format(commission, balance))



