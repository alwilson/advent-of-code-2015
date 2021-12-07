#!/usr/bin/env python3
from typing import Dict, List

import z3

with open('./input.txt') as fd:
    routes = [l.strip() for l in fd]

# s = Solver()
s = z3.Optimize()

syms : Dict[str, z3.ArithRef] = {}
city_idx = 0

xij = {}

def add_sym(a : str) -> z3.Int:
    if a not in syms:
        syms[a] = z3.Int(a)
    return syms[a]

edges: Dict[str, z3.ArithRef] = {}
def add_edge(a : str) -> z3.Bool:
    if a not in edges:
        edges[a] = z3.Bool(a)
    return edges[a]

lengths = []
raw_lengths = []

for r in routes:
    r_s = r.split(' ')

    a_s = r_s[0]
    a = add_sym(a_s)

    b_s = r_s[2]
    b = add_sym(b_s)

    d = int(r_s[4])

    xij[(a,b)] = add_edge(a_s+'->'+b_s)
    xij[(b,a)] = add_edge(b_s+'->'+a_s)

    lengths.append(d * xij[(a,b)])
    lengths.append(d * xij[(b,a)])

    raw_lengths.append(d)

    print(a, b, d)

for a in syms.values():
    city_from = []
    city_to = []
    for b in syms.values():
        if a is not b:
            city_from.append(z3.If(xij[(a,b)], 1, 0))
            city_to.append(z3.If(xij[(b,a)], 1, 0))
    s.add(z3.Sum(city_from) == 1)
    s.add(z3.Sum(city_to) == 1)

length = z3.Int('length')
s.add(length == z3.Sum(lengths))
s.minimize(length)

print('s:', s.sexpr())
print('syms:', syms)
print('max(raw_lengths): ', max(raw_lengths))

# Check if constraints have been satisfied
while s.check() == z3.sat:
    m = s.model()
    solution = []
    for e in edges.values():
        if z3.is_true(m[e]):
            print(e, m[e])
            solution.append(e != m[e])
    s.add(z3.Or(solution))
    # print('s:', s.sexpr())
    length_z: z3.IntNumRef = m[length]
    print(length_z.as_long(), max(raw_lengths))
    print(length_z.as_long() - max(raw_lengths))
else:
    print("Failed to solve")
