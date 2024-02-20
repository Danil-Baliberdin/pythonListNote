"""
coins = [0,0,0,0,0,1,1,1,1,1,1,1,1,1,1]
count0 = 0 
count1 = 0

for i in coins:
    if i == 0:
        count0 = count0 +1
    if i == 1:
        count1 = count1 +1

answer  = 0

if count1>count0:
    answer = count0
else:
    answer = count1

print(answer)
"""
#
#
#
"""
n  = 1024 
counter = 1
while n>counter:
    print(counter)
    counter = counter * 2
"""
#
#
#
"""
s = 15
p = 50 

answer = []
counter = 1
answercounter = 0
while counter<=s:
    if  p%counter == 0:
        answer.insert(answercounter, int(p/counter))
        answercounter = answercounter +1
    counter = counter+1
print(answer)

for i in range(len(answer)):
    for j in range(len(answer)):
        if j == i:
            continue
        if answer[i] + answer[j] == s:
            print( answer[i], answer[j])
"""


