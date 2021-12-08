#!/usr/bin/env python3

with open('./input.txt') as fd:
	items = [x.strip() for x in fd]

for i in items:
	houses = {}
	x = [0, 0]
	y = [0, 0]
	j = 0

	houses[(x[j], y[j])] = 2

	print(i)

	for c in i:
		if c == '>':
			x[j] += 1
		if c == '<':
			x[j] -= 1
		if c == '^':
			y[j] += 1
		if c == 'v':
			y[j] -= 1


		if (x[j], y[j]) in houses:
			houses[(x[j], y[j])] += 1
		else:
			houses[(x[j], y[j])] = 1

		# print(j, x, y, houses)
		j ^= 1

	print(houses, len(houses.keys()))

