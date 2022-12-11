#!/usr/bin/env python3

import numpy as np

with open("input8.txt") as f:
  lines = f.read().splitlines()
  ilen = len(lines)
  jlen = len(lines[0])
  trees = np.empty((ilen, jlen),dtype=int)
  for i,l in enumerate(lines):
    trees[i] = [c for c in l]

visibles = 0
scenic_scores = np.empty((ilen, jlen),dtype=int)

for (i,j), tree in np.ndenumerate(trees):
  if i % (ilen-1) == 0 or j % (jlen-1) == 0:
    # on edge 
    visibles += 1
    scenic_scores[i,j] = 0

  else:
    # need to check if visible 
    if trees[0:i,j].max() < tree or trees[i+1:ilen,j].max() < tree or trees[i,0:j].max() < tree or trees[i,j+1:jlen].max() < tree:
      visibles += 1

    # calculate scenic score for each direction: how many trees can be seen until one with height >= current tree blocks the view
    trees_left = trees[i,0:j] >= tree
    try:
      scenic_left = list(np.flip(trees_left)).index(True) + 1
    except ValueError:
      scenic_left = j
    
    trees_right = trees[i,j+1:jlen] >= tree
    try:
      scenic_right = list(trees_right).index(True) + 1
    except ValueError:
      scenic_right = (jlen-1) - j

    trees_up = trees[0:i,j] >= tree
    try:
      scenic_up = list(np.flip(trees_up)).index(True) + 1
    except ValueError:
      scenic_up = i
    
    trees_down = trees[i+1:ilen,j] >= tree
    try:
      scenic_down = list(trees_down).index(True) + 1
    except ValueError:
      scenic_down = (ilen-1) - i

    # multiply scenic scores 
    scenic_scores[i,j] = scenic_left * scenic_right * scenic_up * scenic_down

print(visibles)
print(scenic_scores.max())