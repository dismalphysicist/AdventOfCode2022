def compare(item1,item2):
    # print("Comparing items {} and {}".format(item1,item2))
    # work out types
    list1 = False
    list2 = False
    try:
      int(item1)
    except TypeError:
      list1 = True
    try:
      int(item2)
    except TypeError:
      list2 = True

    # compare according to types
    if not list1 and not list2:
        # both integers 
        if item1 < item2:
            return 1
        elif item1 > item2:
            return 0
        else:
            return -1 # inconclusive

    if list1 and list2:
        for i in range(len(item1)):
            if i < len(item2):
                result = compare(item1[i],item2[i])
                if result == 1:
                    return 1
                elif result == 0:
                    return 0
                else: # inconclusive
                    continue
            else:
                # if right list runs out of items first
                return 0
        # we got to the end of list 1, so compare lengths
        if len(item1) < len(item2):
            return 1
        elif len(item1) == len(item2):
            return -1 # inconclusive

    elif not list1:
        return compare([item1],item2)
    elif not list2:
        return compare(item1,[item2])

with open("input13.txt","r") as f:
    pairs = [pair.split("\n") for pair in f.read().split("\n\n")]

sum_indices = 0
for index_minus_one, pair in enumerate(pairs):
    print("Considering pair {}".format(index_minus_one+1))
    right_order = compare(eval(pair[0]),eval(pair[1]))
    if right_order == 1:
        print("Pair {} is correct".format(index_minus_one+1))
        sum_indices += index_minus_one + 1

print(sum_indices)