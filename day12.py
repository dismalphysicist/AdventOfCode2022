with open("input12.txt","r") as f:
    lines = f.read().splitlines()
    area = []
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


ymax = len(area)-1
xmax = len(area[0])-1

xpos = start_xpos
ypos = start_ypos
elev = 'a'
nsteps = 0
maxsteps = 3

