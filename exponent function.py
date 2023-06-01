#it allows use to take a certain number and raise it to a soecific power

print(2**3)
def raiseTOPOW(base_num, pow_num): #inside the function we created 2variables the base and power number
    result = 1   #defined a variable called result, and its where we are going to store the actial result of doing the math
    for i in range(pow_num):
        result = result * base_num
    return result

print(raiseTOPOW(3, 4))



