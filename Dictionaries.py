#A dictionary is aspecial structrure in python which allows to store in what are called key value pairs
monthConversions = {
    1: "January",
    2: "February",
    3: "March",
    "Apr": "April",
    "My": "May",
    "Jun": "June",
    "Jly": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct":  "October",
    "Nov": "November",
    "Dec": "December",
}

print(monthConversions["Nov"])
print(monthConversions.get("luv", "Not a default value"))
print(monthConversions.get(3))






