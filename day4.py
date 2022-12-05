#!/usr/bin/env python3

total_overlap = 0
partial_overlap = 0

with open("input4.txt","r") as f:
  firsts, seconds = zip(*[i.split(",") for i in f.read().splitlines()])
  
  for i,r in enumerate(firsts):
    lower1 = int(r.split("-")[0])
    upper1 = int(r.split("-")[1])
    lower2 = int(seconds[i].split("-")[0])
    upper2 = int(seconds[i].split("-")[1])

    # part 1 
    if lower1 < lower2:
      if upper1 >= upper2:
        total_overlap += 1

    if lower2 < lower1:
      if upper2 >= upper1:
        total_overlap += 1

    if lower2 == lower1:
      total_overlap += 1

    # part 2 
    if (lower2 in range(lower1,upper1+1)) or (lower1 in range(lower2,upper2+1)):
      partial_overlap += 1

print("Total overlapping ranges = ",total_overlap)
print("Partially overlapping ranges = ",partial_overlap)