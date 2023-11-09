# word = input('Please enter a word: ')
# first = word[0]. lower()
# length = len(word)
# rest= word[1:length]
# if first not in list('aeiou'):
#     newword = rest + first + 'ay'
# else :
#     newword = word + 'way'
#     print(newword. lower())

# total = 0
# for i in range(0, 5):
#     num = int(input('Enter a number: '))
#     ans = input('Do you want this number included? (y/n)')
#     if ans == 'y' or ans == 'Y':
#         total += num
# print(total)

# def f3(x):
#     tmp= x[::- 1]
#     tmp. remove(min(tmp))
#     return tmp
# lst= [[7,6,8,2,9,3]]
# for _ in range(3):
#     lst. append(f3(lst[-1]))
# print(lst)

# import random
# s= '0123456789'
# passlen = 4
# p = ''. join(random. sample(s, passlen))
# print(p)

# mydict = {
# 'emp1': {'name':'Park', 'salary': 9500},
# 'emp2': {'name':'Lee', 'salary': 8300},
# 'emp3': {'name':'Kim', 'salary': 5500}
# ,}
# mydict['emp3']['salary'] = 8500
# print(mydict)

# i m p o r t random
# d e f isPrime(n):
# i f n < 2:
# r e t u r n F a l s e
# f o r i i n range(2, int(n* * 0.5)+ 1):
# i f n % i = = 0:
# r e t u r n F a l s e
# r e t u r n T r u e
# # 소수 리스트 생성
# prime_list = [i f o r i i n range(1,46) i f isPrime(i) a n d i ! = 13]
# d e f generate_lotto():
# w h i l e T r u e :
# lotto = sorted(random. sample(range(1,46), 6))
# i f 13 i n lotto:
# c o n t i n u e
# i f len([i f o r i i n lotto i f isPrime(i)]) < 2:
# c o n t i n u e
# i f max(lotto) - min(lotto) > 30:
# c o n t i n u e
# i f sum(lotto)/ 6 < 15 o r sum(lotto)/ 6 > 20:
# c o n t i n u e
# r e t u r n lotto
# f o r _ i n range(3):
# print(generate_lotto())

# money = 10000
# price = [2100,3200,2100,800]
# def solution(price, money):
#     answer = 0
#     for i in price:
#         money -= i
#     answer = money
#     if answer < 0:
#         return - 1
#     return answer
# print(solution(price,money))

# scores = [1,2,3,4,5]
# def func_a(s): # 최대, 최소값 구하는 함수
#     s.sort()
#     return s[- 1],s[0]
# def func_b(s): # 총합 구하는 함수
#     ret = 0
#     for i in s:
#         ret += i
#     return ret
# def solution(scores):
#     tot = func_b(scores)
#     mx,mn = func_a(scores)
#     return tot - mx - mn
# print(solution(scores))

# scores = [233,345,123,256]
# def solution1(scores):
#     cnt = 0
#     for s in range(len(scores)):
#         if (scores[s] <= 200):
#             cnt += 1
#     return cnt
# print(solution1(scores))

# grade = 'S'
# price = 2000
# def solution(price, grade):
#     ans = 0
#     if grade == 'S':
#         ans = price * 1.05
#     if grade == 'G':
#         ans = price * 1.10
#     if grade == 'V':
#         ans = price * 1.15
#     return int(ans)
# print(solution(price, grade))

# name = "Bob"
# age = 25

# result = f"안녕하세요, 제 이름은 {name}이고 나이는 {age}살입니다.".upper()
# print(result)

# my_list = [1, 2, 3, 4, 5]
# my_list1 = my_list.append(6).extend([7, 8, 9]).reverse()

# print(my_list1)

# number = 99
# def solution(number):
#     cnt = 0
#     for i in range(1, number + 1):
#         current = i
#         while current != 0:
#             unit = current % 10
#             if unit in [3, 6, 9]:
#                 cnt += 1
#             current //= 10
#     return cnt
# print(solution(number))

# characters = 'aaaddddsssffff'
# def solution(characters):
#     result = [characters[0]]
#     for i in range(1, len(characters)):
#         if characters[i - 1] != characters[i]:
#             result.append(characters[i])
#     return ''.join(result)
# print(solution(characters))

# my_string = "Hello, World!"

# # 문자열을 대문자로 만들고 공백을 제거한 뒤, 'W'의 인덱스를 반환
# result = my_string.upper().replace(" ", "").index("W")

# print(result)  # 결과: 6

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def introduce(self):
#         return f"My name is {self.name} and I am {self.age} years old."

# # Person 클래스를 사용하여 객체 생성
# person1 = Person("John Doe", 30)

# # 객체의 introduce 메서드 호출 및 출력
# print(person1.introduce())

# subway =["유재석","조세호","박명수","허수진"]
# subway.append("장경준")
# subway.extend(["양세찬", "장경원"])
# subway.reverse()

# print(subway)

# my_string = "hello, world!"

# # 문자열을 대문자로 만들고 공백을 제거한 뒤, 'W'의 인덱스를 반환
# result = my_string.upper().replace(" ", "").index("W")

# print(result)  # 결과: 6

# setence = "I love you"
# def solution(sentence):
#     return sentence == sentence[::-1]
# print(solution("I"))

def average(grades):
    return sum(grades) / len(grades)
grades = [90, 85, 74]
print(average(grades)) 


