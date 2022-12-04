import numpy as np
from itertools import zip_longest


filename = "../../assets/day_4.txt"

with open(filename) as f:
    content = f.read().splitlines()

result = 0

for line in content:
    split = line.split(",")
    elf1split = split[0].split("-")
    elf1 = list(range(int(elf1split[0]), int(elf1split[1])+1))
    elf2split = split[1].split("-")
    elf2 = list(range(int(elf2split[0]), int(elf2split[1])+1))

    includes1 = all(item in elf1 for item in elf2)
    includes2 = all(item in elf2 for item in elf1)
    if includes1 or includes2:
        result += 1

print("1. In how many assignment pairs does one range fully contain the other?")
print(result)
print()

result = 0

for line in content:
    split = line.split(",")
    elf1split = split[0].split("-")
    elf1 = list(range(int(elf1split[0]), int(elf1split[1])+1))
    elf2split = split[1].split("-")
    elf2 = list(range(int(elf2split[0]), int(elf2split[1])+1))

    includes1 = any(item in elf1 for item in elf2)
    includes2 = any(item in elf2 for item in elf1)
    if includes1 or includes2:
        result += 1


print("2. In how many assignment pairs do the ranges overlap?")
print(result)
print()