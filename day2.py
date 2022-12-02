#!/usr/bin/env python3

you_ref = {'X':1,'Y':2,'Z':3}
lose_ref = {'A':'Z','B':'X','C':'Y'}
draw_ref = {'A':'X','B':'Y','C':'Z'}
win_ref = {'A':'Y','B':'Z','C':'X'}

def score(you,opp):
    if win_ref[opp] == you:
        return you_ref[you] + 6
    elif draw_ref[opp] == you:
        return you_ref[you] + 3
    else:
        return you_ref[you]

def score2(outcome,opp):
    if outcome == 'X':
        return you_ref[lose_ref[opp]]
    elif outcome == 'Y':
        return you_ref[draw_ref[opp]] + 3
    else:
        return you_ref[win_ref[opp]] + 6

with open("input2.txt","r") as f:
    scoreTot = 0
    score2Tot = 0
    for line in f:
        opp, p2 = line.strip().split(' ')
        scoreTot += score(p2,opp)
        score2Tot += score2(p2,opp)

    print("Part 1 answer: ",scoreTot)
    print("Part 2 answer: ",score2Tot)
