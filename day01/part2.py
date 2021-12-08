#!/usr/bin/env python3

with open('./part1.txt') as fd:
	items = [x.strip() for x in fd]

print(items)

for i in items:
	print(i)
	lvl = 0
	for c_i, c in enumerate(i):
		print(lvl, c_i)
		if c == '(':
			lvl += 1
		if c == ')':
			lvl -= 1
		if lvl == -1:
			print('basement: ', 1+c_i)
			break
	print('done')
