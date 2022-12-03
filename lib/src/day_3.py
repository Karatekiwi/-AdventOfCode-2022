import numpy as np
from itertools import zip_longest


def splitstring(value):
    string1, string2 = value[:len(value)//2], value[len(value)//2:]
    return string1, string2


def grouper(list, size):
    return [list[n:n+size] for n in range(0, len(list), size)]


def get_priority(letter):
    lower = 96
    upper = 38
    if letter.isupper():
        return ord(letter) - upper
    else:
        return ord(letter) - lower


def calculate_priority(list):
    priority = 0
    for item in list:
        priority += get_priority(item)
    return priority

filename = "../../assets/day_3.txt"

with open(filename) as f:
    content = f.read().splitlines()

duplicates = []

for rucksack in content:
    split = splitstring(rucksack)
    rucksack0 = split[0]
    rucksack1 = split[1]

    duplicate = set(rucksack0).intersection(rucksack1)
    for x in duplicate:
        duplicates.append(x)


print("1. Find the item type that appears in both compartments of each rucksack. What is the sum of the priorities of those item types?")
print(calculate_priority(duplicates))
print()

priority = 0
duplicates = []

for group in grouper(content, 3):
    badge = set(group[0]).intersection(group[1], group[2])
    duplicates.append(list(badge)[0])

print("2. Find the item type that corresponds to the badges of each three-Elf group. What is the sum of the priorities of those item types?")
print(calculate_priority(duplicates))
print()