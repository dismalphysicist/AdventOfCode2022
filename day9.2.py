instructions = []

with open("input9.txt","r") as f:
    for line in f.read().splitlines():
        l = line.split(" ")
        for i in range(int(l[1])):
            instructions.append(l[0])

ropeLen = 10

xs = [0 for _ in range(ropeLen)]
ys = [0 for _ in range(ropeLen)]
visited = [(0,0)]
for i in instructions:
    # where does the head go?
    if i == 'L':
        xs[0] -= 1
    elif i == 'R':
        xs[0] += 1
    elif i == 'U':
        ys[0] += 1
    elif i == 'D':
        ys[0] -= 1
    
    # now loop over the rest of the rope in order
    for k in range(1,ropeLen):
        # where does the next knot go?
        if abs(xs[k-1]-xs[k]) <= 1 and abs(ys[k-1]-ys[k]) <= 1:
            # next knot does not move 
            continue 
        if xs[k-1]==xs[k]: # same column 
            ys[k] += (ys[k-1]-ys[k])/abs(ys[k-1]-ys[k])
        elif ys[k-1]==ys[k]: # same row 
            xs[k] += (xs[k-1]-xs[k])/abs(xs[k-1]-xs[k])
        else: # next knot must move diagonally
            ys[k] += (ys[k-1]-ys[k])/abs(ys[k-1]-ys[k])
            xs[k] += (xs[k-1]-xs[k])/abs(xs[k-1]-xs[k])

    # store the position if not stored already 
    if (xs[ropeLen-1],ys[ropeLen-1]) not in visited:
        visited.append((xs[ropeLen-1],ys[ropeLen-1]))

print(len(visited))
