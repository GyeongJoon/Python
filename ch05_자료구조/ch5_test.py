# # 활용 예제
# from random import *
# lst = [1,2,3,4,5]
# print(lst)
# shuffle(lst)
# print(lst)
# print(sample(lst,1))

from random import *
lst = range(1,21)
lst = list(lst)
shuffle(lst)
winners = sample(lst, 4)
print(f"---당첨자 발표---\n치킨 당첨자 : {winners[0]}\n커피 당첨자 : {winners[1:]}\n---축하합니다---")