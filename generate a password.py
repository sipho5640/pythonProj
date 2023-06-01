#a program to create a password, declare a string of numbers + uppercase + lowercase + special characters
import random

passlen = int(input("enter the length of password: "))
s="abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
p = "".join(random.sample(s, passlen))
#random sampling by joining the length of the password and the variable to generate a random password
print(p)


