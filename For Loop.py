#For Loop is used to iterate the elements of a collection in the order that they appear.
#This collection can be a list or string
#syntax-------------- for [variable] in [sequence]:

num = 2

for a in range(1, 6):
    print(num * a)

#sum of 10 numbers

sum1 = 0
for n in range(1, 11):
    sum1 += n
print(sum1)

#nested for loops
for i in range(1, 6):
    for j in range(1, i+1):
        print(i)

#patter program
#for i in range(1, 6):
#    for j in range(5, i-1, -1):
#       print("i")




