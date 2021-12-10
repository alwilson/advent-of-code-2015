#!/usr/bin/env python3

lines = [l.strip() for l in open('input.txt')]
time_elapsed = 2503

distances = []
for l in lines:
    l_split = l.split()
    speed = int(l_split[3])
    duration = int(l_split[6])
    rest = int(l_split[-2])

    period = duration + rest
    full_cycles = time_elapsed // period
    last_cycle_rem = time_elapsed % period

    distance = full_cycles * speed * duration
    if last_cycle_rem < duration:
        distance += last_cycle_rem * speed
    else:
        distance += duration * speed
    distances.append(distance)
print('Part 1: ', max(distances))
