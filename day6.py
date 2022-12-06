#!/usr/bin/env python3

inputlist = []

with open("input6.txt","r") as f:
  while True:
    nextchar = f.read(1)
    if nextchar:
      inputlist.append(nextchar)
    else:
      break

processed = 0
foundPacket = False

for i,c in enumerate(inputlist):
  processed += 1

  if i < 3:
    continue 

  if not foundPacket:
    sub_4 = inputlist[i-3:i+1]
    could_be_packet = True
    for c in sub_4:
      if sub_4.count(c) != 1:
        could_be_packet = False
        break
    if could_be_packet:
      print("Found packet, needed to process:",processed)
      foundPacket = True

  if i < 13:
    continue 
  
  sub_14 = inputlist[i-13:i+1]
  could_be_message = True
  for c in sub_14:
    if sub_14.count(c) != 1:
      could_be_message = False
      break
  if could_be_message:
    print("Found message, needed to process:",processed)
    break
  

print("Length of buffer is",len(inputlist))