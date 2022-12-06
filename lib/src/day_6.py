import numpy as np
from itertools import zip_longest
import re

filename = "../../assets/day_6.txt"

def has_duplicates(str):
    return len(set(str)) != len(str)

with open(filename) as f:
    content = f.read()

index = 0
range = 4

end = len(content)

endIndex = 0

while index < end - range:
    toCheck = content[index: index+range]
    if has_duplicates(toCheck) == False:
        endIndex = index + range
        break
    index += 1

print("1. How many characters need to be processed before the first start-of-packet marker is detected?")
print(endIndex)
print()

index = 0
range = 14

end = len(content)

endIndex = 0

while index < end - range:
    toCheck = content[index: index+range]
    if has_duplicates(toCheck) == False:
        endIndex = index + range
        break
    index += 1

print("2. How many characters need to be processed before the first start-of-message marker is detected?")
print(endIndex)
print()
