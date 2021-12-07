#!/usr/bin/env python3

import re

with open('./input.txt') as fd:
    strings = [s.strip() for s in fd]

nice = 0
for s in strings:
    print(s, '- ', end='')

    has_double = False
    for c_i, c in enumerate(s[:-1]):
        couple = s[c_i:c_i+2]
        new_s = list(s)
        new_s[c_i:c_i+2] = '..'
        new_s = ''.join(new_s)
        # print(couple, new_s)
        if couple in new_s:
            has_double = True
            print('has double', couple, '- ', end='')
            break
    if not has_double:
        print('has no double')
        continue


    has_sandwich = False
    for c_i, c in enumerate(s[:-2]):
        if s[c_i] == s[c_i+2]:
            has_sandwich = True
            print('has sandwich of', s[c_i], '- ', end='')
            break
    if not has_sandwich:
        print('has no sandwich')
        continue

    nice += 1
    print('nice')
print(nice)





