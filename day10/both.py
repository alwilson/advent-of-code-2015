#!/usr/bin/env python3

for times in [40, 50]:
    las = '1113122113'
    
    for _ in range(times):
        new_las = ''
        run = 1
        for c_i, c in enumerate(las):
            if c_i < len(las)-1 and las[c_i+1] == c:
                run += 1
                continue

            new_las += str(run) + c
            run = 1

        las =  new_las

    print(len(las))