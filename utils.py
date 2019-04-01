import random


def genrate_number(size):
    data=[random.randint(1,i) for i in range(2,size)]
    return data