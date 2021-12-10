#!/usr/bin/env python3

lines = [l.strip() for l in open('input.txt')]
time_elapsed = 2503

deer = []
for l in lines:
    l_split = l.split()
    speed = int(l_split[3])
    duration = int(l_split[6])
    rest = int(l_split[-2])

    dist_l = []
    dist = 0
    running = True
    timer = duration
    for _ in range(time_elapsed):
        timer -= 1
        if running:
            dist += speed
            dist_l.append(dist)
            if timer == 0:
                running = False
                timer = rest
        else:
            dist_l.append(dist)
            if timer == 0:
                running = True
                timer = duration

    dist_l.append(0) # The score
    deer.append(dist_l)

for s in range(time_elapsed):
    deer_dists_now = [d[s] for d in deer]
    max_dist = max(deer_dists_now)
    for d in deer:
        if d[s] == max_dist:
            d[-1] += 1 # increment last 'distance' which is the store

deer_scores = [d[-1] for d in deer]
print('Part 2: ', max(deer_scores))