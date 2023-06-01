#IF statements are for decision making in coding, they execute code when other conditions are true or false
isMale = True
isTall = True

if isMale and isTall:
    print("You are a male or tall or both")
elif isMale and not (isTall):
    print("You are a short male")
elif not(isMale) and isTall:
    print("You are a shor person")
else:
    print("You are neither male or  not tall or both")

#IF STATEMENT AND COMPARISONS
def max_num(num1, num2, num3):   #this function will return the largest of the three
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3
print(max_num(3, 4, 5))






