#!/usr/bin/env python3

with open("input7.txt","r") as f:
  lines = [line.strip().split(" ") for line in f.readlines()]

directories = {}
pwd = ""
total_size = 0

for l in lines:
  if l[0] == '$':
    # command - either ls (ignore and read next lines), or cd (update pwd)
    if l[1] == 'cd':
      # command is cd 
      if l[2] == "/":
        # home directory 
        pwd += "~"
      elif l[2] == "..":
        # remove last thing from pwd 
        pwd = pwd.rsplit("/",1)[0]
      else:
        # add new directory
        pwd += "/" + l[2]

  else:
    # result of ls in pwd 
    try:
      size = int(l[0])
    except ValueError:
      # this is a directory, let cd handle it 
      continue

    if pwd not in directories.keys():
      directories[pwd] = 0
    directories[pwd] += size 

# now separate out the directories and their sizes
individual_dirs = {}
for dir in directories.keys():
  len_path = len(dir.split("/"))
  dir_names = [dir.rsplit("/",n)[0] for n in range(0,len_path)]
  for dir_name in dir_names:
    if dir_name not in individual_dirs.keys():
      individual_dirs[dir_name] = 0
    individual_dirs[dir_name] += directories[dir]

# now count up the directories with size <= 100000
total_part1 = 0
for dir in individual_dirs:
  if individual_dirs[dir] <= 100000:
    total_part1 += individual_dirs[dir]

print("Total for all dirs with size <= 100,000: ",total_part1)

space_needed = 30000000 - (70000000 - individual_dirs["~"])
print("Need to free up ",space_needed)
space_freed = 30000000
for dir in individual_dirs:
  if (individual_dirs[dir] >= space_needed) and (individual_dirs[dir] < space_freed):
    space_freed = individual_dirs[dir]

print("Freed up ", space_freed)