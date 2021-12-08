#!/usr/bin/env python3

with open('./input.txt') as fd:
	items = [x.strip() for x in fd]

print(items)

total = 0
for i in items:
	dims = [int(x) for x in i.split('x')]
	print(dims)
	ribbon = sum(dims) - max(dims)
	ribbon *= 2

	bow = dims[0] * dims[1] * dims[2]

	this_box = ribbon + bow
	print(ribbon, bow, this_box)
	total += this_box
print(total)
