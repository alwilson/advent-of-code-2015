#!/usr/bin/env python3

with open('./input.txt') as fd:
    strings = [l.strip() for l in fd]

total = 0
for s in strings:
    s_decode = bytes(s, "utf-8").decode("unicode_escape")
    print(s, len(s), '-> ', s_decode, len(s_decode)-2)
    total += len(s) - len(s_decode) + 2
print(total)
