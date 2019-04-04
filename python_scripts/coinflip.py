#---Author: Anthony Rodriguez
#---Created Date: 08/12/2018
#---Project Tag:Python3, random, probability
#---Purpose:
#   The purpose of this file is to write a simple coin flip script to
#   generate a distribution of coin flips.
#--->

#!/usr/bin/env python

#---Library imports
import random
minnum = 1
maxnum = 2000

heads = 0

for i in range(minnum, maxnum):
    if random.randint(0, 1) == 1: heads = heads + 1
#    if i == 500:
#        print('Halfway done!')

tails = maxnum - heads

print('COIN FLIP RESULTS' + '\n' + '\tHeads: ' + str(heads) +'\n'+ '\tTails: ' + \
str((maxnum - heads)))
print('\nA coin was flipped ' + str(heads + tails) + ' times. ')
