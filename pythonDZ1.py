"""
Найдите сумму цифр трехзначного числа n.
Результат сохраните в перменную res.
Пример:
n = 123 -> res = 6 (1 + 2 + 3)
n = 100 -> res = 1 (1 + 0 + 0)
"""
n = 123
x = int (n%10)
y = int(n%100//10)
z = int(n // 100)
result = z+y+x
print(result)



"""
Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали n журавликов.
Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое количество 
журавликов, а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
Выведите через пробел количество журавликов, сделанных Петей, Катей и Сережей.
Пример:
n = 6 -> 1 4 1  
n = 24 -> 4 16 4    
n = 60 -> 10 40 10 
"""
n = 6
x = n//6
y = n//6*4
print (x,y,x)

"""
Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером.
Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех.
Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6.
Вам требуется написать программу, которая проверяет счастливость билета с номером n и выводит на экран yes или no.
"""
n = '385916'
i=0
leftsum =0
rightsum = 0
while i<6 :    
    if i<3:
        leftsum = leftsum + int(n[i])
        i = i +1
    elif i>2 and i<6:
        rightsum = rightsum + int(n[i])
        i = i +1

if rightsum == leftsum:
    print('yes')
else:
     print('no')
