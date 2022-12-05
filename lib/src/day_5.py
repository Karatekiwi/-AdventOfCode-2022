import numpy as np
from itertools import zip_longest
import re

def calculate_result(stacks):
    result = ""
    for stack in stacks:
        result += stack[len(stack)-1].replace("[", "").replace("]", "")
    return result

def fill_stacks(puzzle_input):
    stacks = [[]]

    for line in puzzle_input:
        index = 0
        if line.strip() == "":
            break

        while index <= len(line):
            value = line[index:index+3].strip()
            if value != "":
                stack_num = int(index / 4)

                while len(stacks) <= stack_num:
                    stacks.append([])

                stacks[stack_num].append(value)

            index += 4

    for stack in stacks:
        stack.reverse()

    return stacks


filename = "../../assets/day_5.txt"

with open(filename) as f:
    content = f.read().splitlines()

num_stacks = 9

# fill the stacks
stacks = fill_stacks(content)

# execute the moves - part 1
for line in content:
    index = 0
    if line.startswith("move") == False:
        continue

    split = line.split(" ")
    num_items = int(split[1])
    stack_num_from = int(split[3])-1
    stack_num_to = int(split[5])-1

    for x in range(num_items):
        to_move = stacks[stack_num_from].pop()
        stacks[stack_num_to].append(to_move)

print("1. After the rearrangement procedure completes, what crate ends up on top of each stack?")
print(calculate_result(stacks))
print()

# re-fill the stacks
stacks = fill_stacks(content)

# execute the moves - part 2
for line in content:
    index = 0
    if line.startswith("move") == False:
        continue

    split = line.split(" ")
    num_items = int(split[1])
    stack_num_from = int(split[3])-1
    stack_num_to = int(split[5])-1

    move_array = []
    for x in range(num_items):
        move_array.append(stacks[stack_num_from].pop())

    move_array.reverse()
    for x in move_array:
        stacks[stack_num_to].append(x)

print("2. After the modified rearrangement procedure completes, what crate ends up on top of each stack?")
print(calculate_result(stacks))
print()