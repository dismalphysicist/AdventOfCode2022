#!/usr/bin/env python3

input = []
totals = []
highestSingle = 0
highest3 = 0

with open("input1.txt","r") as f:
  input = [l.split("\n") for l in f.read().split("\n\n")]

for i,elf in enumerate(input): 
  elf = [int(c) for c in elf]
  totals.append(sum(elf))

totals.sort()
highestSingle = totals[-1]
highest3 = sum(totals[-3:])

print("Highest calorie count of a single elf: ", highestSingle)
print("Top 3 total calories is: ",highest3)