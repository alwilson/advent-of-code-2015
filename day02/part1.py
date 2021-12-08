#!/usr/bin/env python3

with open('./input.txt') as fd:
	items = [x.strip() for x in fd]

print(items)

total = 0
for i in items:
	dims = [int(x) for x in i.split('x')]
	# print(dims)
	ab = dims[0] * dims[1]
	bc = dims[1] * dims[2]
	ac = dims[0] * dims[2]
	# print(ab, bc, ac)
	# print(min(ab, bc, ac))
	this_box = 2 * ab + 2 * bc + 2 * ac + min(ab, bc, ac)
	total += this_box
print(total)
