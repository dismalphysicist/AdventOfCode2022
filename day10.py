with open("input10.txt","r") as f:
    input = ["offbyone"]
    for line in f.read().splitlines():
        if line.split(" ")[0] == "addx":
            input.append("addx 0")
        input.append(line)

sig_strength = 0
X = 1
cursor_posn = 0
screen = ""
for cycle in range(1,len(input)):
    if (cycle-20) % 40 == 0: # readout 
        sig_strength += cycle * X

    # draw pixel 
    if cursor_posn in range(X-1,X+2):
        screen += "#"
    else: 
        screen += "."
    # update cursor position 
    cursor_posn += 1
    if cursor_posn > 39:
        cursor_posn = 0
        screen += "\n"

    # add 
    if input[cycle].split(" ")[0] == "addx": # add
        X += int(input[cycle].split(" ")[1])

print(sig_strength)
print(screen)