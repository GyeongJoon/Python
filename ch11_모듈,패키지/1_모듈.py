import theater_module
theater_module.price(3) # 3명이서 영화 보러 갔을 때 가격
theater_module.price_morning(4) # 4명이서 조조 영화 보러 갔을 때 가격
theater_module.price_soldier(5) # 군인 5명이서 영화 보러 갔을 때 가격

import theater_module as mv
mv.price(3) # 3명이서 영화 보러 갔을 때 가격
mv.price_morning(4) # 4명이서 조조 영화 보러 갔을 때 가격
mv.price_soldier(5) # 군인 5명이서 영화 보러 갔을 때 가격

from theater_module import *
#from random import *
price(3)
price_morning(4)
price_soldier(5)

from theater_module import price,price_morning
price(3)
price_morning(4)

from theater_module import price_soldier as price
price(5)
