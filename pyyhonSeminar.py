"""
ZADACHA1
s=750km
n = vvodish s consoli skorost 
nado chtobi bil output = skolko dnei eto zaimet
"""
from math import ceil

"""
s =int( input('Vvedite S(rasstoyanie): '))
n =int( input('Vvedite skorost: '))
answer = 0
if s%n==0:
    answer = s/n
else: answer = s/n+1

print(int(answer)) 
"""

"""
ZA
3 класса , в каждом известно количество учеников , посчитать минимальное количество парт 
"""
"""
a = int(input('Class A: '))
b = int(input('Class B: '))
c = int(input('Class C: '))

partiA = ceil(a/2)
partiB = ceil(b/2)
partiC = ceil(c/2)

sum = partiA + partiB + partiC
print(sum)
"""

"""
вычисление факториала числа 
"""
"""
f  = int(input())
counter = 1
sum = 1
if f == 0:
    print(f'факториал {f} = {sum}')
else:
    while counter<=f:
        sum = sum * counter
        counter = counter + 1 
    print(f'факториал {f} = {sum}')
"""
"""
Ебаная фибабнача
"""

# a = int(input())
# fibonachi = [0,1]
# addnumber = 1
# addcounter = 2
# while addnumber<= a:
#     fibonachi.insert(addcounter,addnumber)
#     addnumber = addnumber + fibonachi[addcounter-1]
#     addcounter = addcounter + 1 
   

# if a == fibonachi[len(fibonachi)-1]:
#     print(len(fibonachi)-1)
# else : print(-1)

# def numToStr(number):
#     srting = int(number) 
#     return srting
# print(type(numToStr('12345')))

# import random  ЦИСЛА В МАССИВЕ КОТОРЫЕ БОЛЬШЕ ЧЕМ СУММА ЧИСЕЛ СПРАВА ОТ НИХ
# array = []
# for i in range (20):
#     array.append(random.randint(1,100))
# array = tuple(array)
# print(array)
# answerList = []
# for i in range(len(array)):
#     sum=0
#     counter = len(array) -1
#     while counter > i:
#         sum = sum +  array[counter]
#         counter = counter -1
#     print(sum)
#     if array[i]>sum:
#         answerList.append(array[i])
# print(*answerList)
 
import random
list = []
for i in range(10):
    num = random.randint(-5,10)
    list.append(num)

answerList = []
def para (a):
    list = [a,a*a]
    list = tuple(list)
    return list

for i in range(len(list)):
    if list[i]%2==0:
        answerList.append(para(list[i]))

print(answerList)


        
        



















































