import sys

with open("input12.txt","r") as f:
    lines = f.read().splitlines()
    area = []
    distances = []
    visited = []
    for i,l in enumerate(lines):
        # look for start position
        if l.find('S') != -1:
            start_xpos = l.index('S')
            start_ypos = i
            l = l.replace('S','a')
        # look for end position
        if l.find('E') != -1:
            end_xpos = l.find('E')
            end_ypos = i
            l = l.replace('E','z')

        # create area
        area.append([h for h in l])
        distances.append([sys.maxint for _ in l])
        visited.append([False for _ in l])


ymax = len(area)
xmax = len(area[0])

xpos = start_xpos
ypos = start_ypos
elev = 'a'
distances[start_ypos][start_xpos] = 0
visited[start_ypos][start_xpos] = True
visit_next = []
maxsteps = sys.maxint # debugging
nsteps = 0

# Dijkstra's algorithm for smallest distance between two points
while not visited[end_ypos][end_xpos] and nsteps < maxsteps:
    # look at all neighbours - if possible to get to, assign distance
    for (x,y) in [(xpos-1,ypos),(xpos+1,ypos),(xpos,ypos+1),(xpos,ypos-1)]:
        # if in grid
        if x in range(0,xmax) and y in range(0,ymax):
            # if unvisited
            if not visited[y][x]:
                if ord(area[y][x]) <= ord(elev)+1:
                    distances[y][x] = min(distances[y][x],distances[ypos][xpos]+1)
                    if (x,y) not in visit_next:
                        visit_next.append((x,y))

    # mark current node as visited 
    visited[ypos][xpos] = True
    if not visited[end_ypos][end_xpos]:
        # select unvisited node with the smallest tentative distance 
        visit_next.sort(key = lambda (x,y): distances[y][x], reverse = True)
        xpos,ypos = visit_next.pop()
        nsteps += 1
        # update elevation
        elev = area[ypos][xpos]

print(distances[end_ypos][end_xpos])