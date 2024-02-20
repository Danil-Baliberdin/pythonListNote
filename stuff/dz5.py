import random
list = []
for i in range(20):
    num = int(random.randint(-100,100))
    list.append(num)
print(list)
min = -27
print(min)
max = 27
print(max)


list = tuple(list)
for i in range(len(list)):
    if min<list[i] and max >list[i]:
        print(i)

# def prograssion(a1,d,n):
#     list = []
#     for i in range(n):
#         list.append(a1+(i)*d)
#         print (list[i])
#     return list
# prograssion(2,3,4)
    






