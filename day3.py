#!/usr/bin/env python3

def priority(c):
    if c.upper() == c:
        return 26 + ord(c)-ord('A') + 1
    else:
        return ord(c)-ord('a') + 1

total_wrong = 0
total_badges = 0
prevline = ""
letters_in_common = []
with open("input3.txt","r") as f:
    for i,line in enumerate(f):
        # part 1
        first_half = line[:len(line)/2]
        second_half = line[len(line)/2:]
        
        for c in first_half:
            if c in second_half:
                total_wrong += priority(c)
                break 

        # part 2 
        if (i % 3 == 0):
            # start of a new group 
            prevline = line

        if (i % 3 == 1):
            # second in group
            for l in prevline:
                if l in line:
                    letters_in_common.append(l)

        if (i % 3 == 2):
            # last in group
            for l in letters_in_common:
                if l in line:
                    total_badges += priority(l)
                    break
            letters_in_common = []
        
print("Sum of priorities of incorrect objects: ",total_wrong)
print("Sum of priorities of badges: ",total_badges)