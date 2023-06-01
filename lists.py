luckyNumbers = [4, 8, 6, 3, 19, 25, 33, 42]
friends = ["kevin", "david", "huey", "bohlale", "lalani", "minenhle", "bohlale"]
friends[1] = "sipho"
print(friends)
print(friends[-1]) #we can access elements of lists based on indexe
print(friends[1:])
print(friends[1:3])
print(luckyNumbers)
print(luckyNumbers[-1])
list3 = luckyNumbers+friends
print(list3)
#A LIST USES BOX PARENTHESES or square brackets and elements or values are separated by commas
#LIST FUNCTIONS
#friends.extend(luckyNumbers)
print(friends)
friends.append("Nomsa") #when you want to add individual element
print(friends)
friends.insert(1, "mbulelo")
print(friends)
friends.remove("mbulelo")
print(friends)
#friends.clear()
#print(friends)
friends.pop()
print(friends)
print(friends.index("huey"))
print(friends.count("bohlale"))
friends.sort()
print(friends)
luckyNumbers.sort()
print(luckyNumbers)
luckyNumbers.reverse()
print(luckyNumbers)
friends2 = friends.copy()
print(friends2)


