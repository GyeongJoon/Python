# # 활용 예제
# from random import *
# lst = [1,2,3,4,5]
# print(lst)
# shuffle(lst)
# print(lst)
# print(sample(lst,1))

# 1
from random import *
lst = range(1,21)
lst = list(lst)
shuffle(lst)
winners = sample(lst, 4)
print(f"---당첨자 발표---\n치킨 당첨자 : {winners[0]}\n커피 당첨자 : {winners[1:]}\n---축하합니다---")

# 2
import random
id = range(1,21)
id = list(id)
random.shuffle(id)
id = random.sample(id, 4)
print('치킨 당첨자:' + str(id[0]))
print('커피 당첨자:' + str(id[1:]))

# 3 (중복제거)
my_list = ['자료구조','알고리즘','자료구조','운영체제']
my_set = set(my_list)
my_list = list(my_set)
print(my_list)