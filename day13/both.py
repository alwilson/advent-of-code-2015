#!/usr/bin/env python3

from z3 import *
import pprint as pp

lines = [l.strip() for l in open('input.txt')]

happy = {}
for l in lines:
    splits = l.split()
    person_a = splits[0]
    person_b = splits[10][:-1]
    happiness = (1 if splits[2] == 'gain' else -1) * int(splits[3])

    if person_a not in happy:
        happy[person_a] = {}
    happy[person_a][person_b] = happiness

pp.pprint(happy)

s = Optimize()
persons = {}
num_ppl = len(happy.keys())
for person_a in happy.keys():
    person = Int(person_a)
    persons[person_a] = person
    s.add(person >= 0)
    s.add(person < num_ppl)
s.add(Distinct(list(persons.values())))

pp.pprint(persons)

def abs(x):
    return If(x >= 0,x,-x)

total_happy = []
for person_a, people in happy.items():
    for person_b, happiness in people.items():
        p_b = persons[person_b]
        p_a = persons[person_a]
        dist = abs(p_b - p_a)
        total_happy.append(If(Or(dist == 1, And(p_b == 0, p_a == num_ppl-1), And(p_b == num_ppl-1, p_a == 0)), happiness, 0))

pp.pprint(total_happy)
total = Int('total')
s.add(total == Sum(total_happy))
s.maximize(total)

print(s)

ret = s.check()

if ret == sat:
    print(s.model())
else:
    print(ret)