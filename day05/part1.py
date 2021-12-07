#!/usr/bin/env python3

import re

with open('./input.txt') as fd:
    strings = [s.strip() for s in fd]

nice = 0
for s in strings:
    print(s, '- ', end='')

    count = 0
    for c in s:
        if c in 'aeiou':
            count += 1
    if count < 3:
        print('too few vowels')
        continue

    prev_c = ''
    double = False
    for c in s:
        if c == prev_c:
            double = True
            break
        prev_c = c
    if not double:
        print('no doubles')
        continue

    if 'ab' in s or 'cd' in s or 'pq' in s or 'xy' in s:
        print('bad couples')
        continue

    nice += 1
    print('nice')
print(nice)





