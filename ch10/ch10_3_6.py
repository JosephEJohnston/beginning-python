from time import *
from random import randrange

date1 = (2016, 1, 1, 0, 0, 0, -1, -1, -1)
time1 = mktime(date1)
date2 = (2017, 1, 1, 0, 0, 0, -1, -1, -1)
time2 = mktime(date2)

num = int(input('How many dice?'))
sides = int(input('How many sides per die?'))
sum_value = 0
for i in range(num):
    sum_value += randrange(sides) + 1
print('The result is ', sum_value)
