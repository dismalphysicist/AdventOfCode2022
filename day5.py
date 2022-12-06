#!/usr/bin/env python3
from collections import deque

piles = {}
piles2 = {}
for i in range(1,10):
  piles[i] = deque()
  piles2[i] = deque()

with open("input5.txt","r") as f:
  for line in f.read().splitlines():
    if len(line.strip()) == 0:
      continue

    if line.strip()[0] == '[':
      # crate line 
      pos = -1
      for i in range(1,10):
        # work out where next crate goes 
        pos = line.find('[',pos+1)
        pile = int(pos/4 + 1)
        if pile == 0:
          # no more crates
          break
        # the top of the pile is the right of the deque
        piles[pile].appendleft(line[pos+1])
        piles2[pile].appendleft(line[pos+1])

    elif line.strip()[0] == 'm':
      # move instruction line 
      num = int(line.split(' ')[1])
      start = int(line.split(' ')[3])
      end = int(line.split(' ')[5])
      removed = deque()
      for i in range(num):
        piles[end].append(piles[start].pop())
        removed.appendleft(piles2[start].pop())
      piles2[end].extend(removed)

    else:
      continue

printstr1 = ""
printstr2 = ""

for pile in piles.values():
  printstr1 += pile[-1]

for pile in piles2.values():
  printstr2 += pile[-1]

print("Planned top crates:", printstr1)
print("Actual top crates:", printstr2)