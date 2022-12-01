import numpy as np


def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False


filename = "../../assets/day_1.txt"

content = open(filename).readlines()

idxs = [i for i, v in enumerate(content, 1) if v == '\n']
result = [content[i:j] for i, j in zip([0] + idxs, idxs)]

allRations = []

for elfRations in result:
    rations = [int(x) for x in filter(lambda ration: ration.strip().isdigit(), elfRations)]
    allRations.append(sum(rations))

print("1. Find the Elf carrying the most Calories. How many total Calories is that Elf carrying?")
print(np.max(allRations))
print()

max1 = np.max(allRations)
allRations.remove(max1)

max2 = np.max(allRations)
allRations.remove(max2)

max3 = np.max(allRations)

print()

print("2. Find the top three Elves carrying the most Calories. How many Calories are those Elves carrying in total?")
print(max1 + max2 + max3)
print()
