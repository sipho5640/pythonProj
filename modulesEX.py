import random

feetInMiles = 5300
meterInKilometers = 1000
beetles = ['mac beth', 'paul matavire', 'ringo stlye']

def get_file_ext(filename):
    return filename[filename.index('.') + 1:]


def roll_dice(num):
    return random.randint(1, num)

import random

passlen = int(input("enter the length of password"))
s="abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
p = "".join(random.sample(s,passlen ))
print(p)