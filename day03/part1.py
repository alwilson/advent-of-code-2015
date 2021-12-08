#!/usr/bin/env python3

with open('./input.txt') as fd:
	items = [x.strip() for x in fd]

for i in items:
	houses = {}
	x = 0
	y = 0
	houses[(x, y)] = 1

	print(i)

	for c in i:
		if c == '>':
			x += 1
		if c == '<':
			x -= 1
		if c == '^':
			y += 1
		if c == 'v':
			y -= 1

		if (x, y) in houses:
			houses[(x, y)] += 1
		else:
			houses[(x, y)] = 1


	print(houses, len(houses.keys()))

