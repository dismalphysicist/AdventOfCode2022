import sys

with open("input12.txt","r") as f:
    lines = f.read().splitlines()
    area = []
    distances = []
    visited = []
    for i,l in enumerate(lines):
        # look for start position for reversed search
        if l.find('E') != -1:
            start_xpos = l.index('E')
            start_ypos = i
            l = l.replace('E','z')
        # look for end position for reversed search
        if l.find('S') != -1:
            l = l.replace('S','a')

        # create area
        area.append([h for h in l])
        distances.append([sys.maxint for _ in l])
        visited.append([False for _ in l])


ymax = len(area)
xmax = len(area[0])

xpos = start_xpos
ypos = start_ypos
elev = 'z'
distances[start_ypos][start_xpos] = 0
visited[start_ypos][start_xpos] = True
visit_next = []
maxsteps = xmax*ymax # total number of points for full traversal
nsteps = 0

# Dijkstra's algorithm for smallest distance between two points
while nsteps < maxsteps:
    # look at all neighbours - if possible to get to, assign distance
    for (x,y) in [(xpos-1,ypos),(xpos+1,ypos),(xpos,ypos+1),(xpos,ypos-1)]:
        # if in grid
        if x in range(0,xmax) and y in range(0,ymax):
            # if unvisited
            if not visited[y][x]:
                if ord(area[y][x]) >= ord(elev)-1: # reverse of part 1 
                    distances[y][x] = min(distances[y][x],distances[ypos][xpos]+1)
                    if (x,y) not in visit_next:
                        visit_next.append((x,y))

    # mark current node as visited 
    visited[ypos][xpos] = True
    # select unvisited node with the smallest tentative distance 
    visit_next.sort(key = lambda (x,y): distances[y][x], reverse = True)
    if len(visit_next) > 0:
        xpos,ypos = visit_next.pop()
    nsteps += 1
    # update elevation
    elev = area[ypos][xpos]

# now identify position with elevation 'a' with smallest distance 
min_a = sys.maxint
for x in range(0,xmax):
    for y in range(0,ymax):
        if area[y][x] == 'a':
            if distances[y][x] < min_a:
                min_a = distances[y][x]

print(min_a)