import sys

class Monkey:
    def __init__(self,starting_list,oper,divisor):
        self.item_list = starting_list
        self.oper = oper
        self.divisor = divisor
        self.handle_count = 0

    def set_monkeys(self,true_monkey,false_monkey):
        self.true_monkey = true_monkey
        self.false_monkey = false_monkey

    def turn(self):
        # throw each item in turn
        for item in self.item_list:
            # worry level operation while inspecting item
            item = eval(self.oper.replace("old",str(item)))
            # relief factor
            if part == 1:
                item = int(item/3)
            else:
                item = item % divisor_product
            # test to determine item's trajectory
            if item % self.divisor == 0:
                self.true_monkey.item_list.append(item)
            else:
                self.false_monkey.item_list.append(item)
        # this monkey has handled some items
        self.handle_count += len(self.item_list)
        # everything has been thrown
        self.item_list = []

with open("input11.txt","r") as f:
    input = f.read().split("Monkey")[1:]

# create each monkey 
monkeys = []
divisor_product = 1
for m in input:
    starting_list = [int(i) for i in m.splitlines()[1].split(":",1)[1].split(",")]
    operation = m.splitlines()[2].split("=")[1]
    divisor = int(m.splitlines()[3].split("by ")[1])
    monkeys.append(Monkey(starting_list,operation,divisor))
    # we need to stop the worry level from exploding 
    # must not change the result of any of the tests, so find product of divisors
    divisor_product *= divisor

# now all the monkeys are created, set the receiving monkeys 
for i,m in enumerate(input):
    j = int(m.splitlines()[4].split(" ")[-1])
    k = int(m.splitlines()[5].split(" ")[-1])
    monkeys[i].set_monkeys(monkeys[j],monkeys[k])

# run 20 rounds for part 1, 10000 rounds for part 2
part = 2
if part == 2:
    num_rounds = 10000
else:
    num_rounds = 20

for i in range(num_rounds):
    for m in monkeys:
        m.turn()
    sys.stdout.write('\rRound {0}'.format(i))
    sys.stdout.flush()

print("")
handle_counts = [monkey.handle_count for monkey in monkeys]
handle_counts.sort()
print(handle_counts[-2]*handle_counts[-1])