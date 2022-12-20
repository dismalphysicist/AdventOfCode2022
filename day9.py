instructions = []

with open("input9.txt","r") as f:
    for line in f.read().splitlines():
        l = line.split(" ")
        for i in range(int(l[1])):
            instructions.append(l[0])

xh = 0
yh = 0
xt = 0
yt = 0
visited = [(0,0)]
for i in instructions:
    # where does the head go?
    if i == 'L':
        xh -= 1
    elif i == 'R':
        xh += 1
    elif i == 'U':
        yh += 1
    elif i == 'D':
        yh -= 1
    
    # where does the tail go?
    if abs(xh-xt) <= 1 and abs(yh-yt) <= 1:
        # tail does not move 
        continue 
    if xh==xt: # same column 
        yt += (yh-yt)/abs(yh-yt)
    elif yh==yt: # same row 
        xt += (xh-xt)/abs(xh-xt)
    else: # tail must move diagonally
        yt += (yh-yt)/abs(yh-yt)
        xt += (xh-xt)/abs(xh-xt)

    # store the position if not stored already 
    if (xt,yt) not in visited:
        visited.append((xt,yt))

print(len(visited))
