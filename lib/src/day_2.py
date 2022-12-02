import numpy as np


def get_score(line):
    score = 0
    line = line.strip()
    if line == "A X":
        score += 4
    elif line == "A Y":
        score += 8
    elif line == "A Z":
        score += 3
    elif line == "B X":
        score += 1
    elif line == "B Y":
        score += 5
    elif line == "B Z":
        score += 9
    elif line == "C X":
        score += 7
    elif line == "C Y":
        score += 2
    elif line == "C Z":
        score += 6
    return score


def choose_move(line):
    line = line.strip()

    if line == "A X":
        return "Z"
    elif line == "A Z":
        return "Y"
    elif line == "B X":
        return "X"
    elif line == "B Z":
        return "Z"
    elif line == "C X":
        return "Y"
    elif line == "C Z":
        return "X"
    #draw
    elif line == "A Y":
        return "X"
    elif line == "B Y":
        return "Y"
    elif line == "C Y":
        return "Z"


def replacer(s, newstring, index):
    return s[:index] + newstring + s[index + 1:]


filename = "../../assets/day_2.txt"

content = open(filename).readlines()

total = []

for line in content:
    score = get_score(line)
    total.append(score)

print("1. What would your total score be if everything goes exactly according to your strategy guide?")
print(np.sum(total))
print()

total = []

for line in content:
    move = choose_move(line)
    line = replacer(line, move, 2)
    score = get_score(line)
    total.append(score)

print("1. Following the Elf's instructions for the second column, what would your total score be if everything goes exactly according to your strategy guide?")
print(np.sum(total))
print()