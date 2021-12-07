#!/usr/bin/env python3

import re

with open('./input.txt') as fd:
    instr = [i.strip() for i in fd]

grid = [[0 for x in range(1000)] for x in range(1000)]

for i in instr:
    print(i)
    i_s = i.split(' ')
    if 'toggle' in i:
        top_left = i_s[1]
        bot_right = i_s[-1]
    else:
        top_left = i_s[2]
        bot_right = i_s[-1]

    tl = [int(x) for x in top_left.split(',')]
    br = [int(x) for x in bot_right.split(',')]
    print(tl, br)
    for x in range(tl[0], br[0]+1):
        for y in range(tl[1], br[1]+1):
            if 'toggle' in i:
                grid[x][y] ^= 1
            if 'turn on' in i:
                grid[x][y] = 1
            if 'turn off' in i:
                grid[x][y] = 0
    count = sum([sum(x) for x in grid])
    print(count)



# grid[500][500] = 1


count = sum([sum(x) for x in grid])
print(count)




