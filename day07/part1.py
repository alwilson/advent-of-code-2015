#!/usr/bin/env python3

from z3 import *

with open('./input.txt') as fd:
    wires = [w.strip() for w in fd]

s = Solver()

syms = {}

for w in wires:
    parts = w.split(' ')
    print(parts)
    if parts[-1] not in syms:
        syms[parts[-1]] = BitVec(parts[-1],16)
    rh = syms[parts[-1]]

    if parts[1] == '->':
        if parts[0].isnumeric():
            val = BitVecVal(int(parts[0]),16)
            s.add(val == rh)
        else:
            if parts[0] not in syms:
                syms[parts[0]] = BitVec(parts[0],16)
            a = syms[parts[0]]
            s.add(a == rh)

    if 'AND' in w:
        if parts[0] not in syms:
            syms[parts[0]] = BitVec(parts[0],16)
        a = syms[parts[0]]

        if parts[2] not in syms:
            syms[parts[2]] = BitVec(parts[2],16)
        b = syms[parts[2]]

        s.add(a & b == rh)

    if 'OR' in w:
        if parts[0] not in syms:
            syms[parts[0]] = BitVec(parts[0],16)
        a = syms[parts[0]]

        if parts[2] not in syms:
            syms[parts[2]] = BitVec(parts[2],16)
        b = syms[parts[2]]

        s.add(a | b == rh)

    if 'NOT' in w:
        if parts[1] not in syms:
            syms[parts[1]] = BitVec(parts[1],16)
        a = syms[parts[1]]

        s.add(~a == rh)

    if 'LSHIFT' in w:
        if parts[0] not in syms:
            syms[parts[0]] = BitVec(parts[0],16)
        a = syms[parts[0]]

        val = int(parts[2])

        s.add(a << val == rh)

    if 'RSHIFT' in w:
        if parts[0] not in syms:
            syms[parts[0]] = BitVec(parts[0],16)
        a = syms[parts[0]]

        val = int(parts[2])

        s.add(a >> val == rh)

print('s:', s)

# Check if constraints have been satisfied
if s.check() == sat:
    print(s.model())
else:
    print("Failed to solve")
