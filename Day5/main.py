import re
from copy import deepcopy

crates = []
with open('input.txt') as file:
    line = file.readline()
    while "1" not in line:
        crates += line.split("\n")
        line = file.readline()
    instr = file.read().split("\n")[1:-1]

n = (len(crates[0])+1)//4
crates = [[crate[i:i+3] for crate in crates[::2]] for i in range(0, n*4-1, 4)]
instr = [[int(i)-1 for i in re.findall(r'\b\d+\b', el)] for el in instr]
crates = [[i for i in el if i != "   "] for el in crates]
crates1 = deepcopy(crates)
for el in instr:
    for i in crates[el[1]][:el[0]+1]:
        crates[el[2]].insert(0, i)
    crates[el[1]] = crates[el[1]][el[0]+1:]

for el in instr:
    for i in crates1[el[1]][:el[0]+1][::-1]:
        crates1[el[2]].insert(0, i)
    crates1[el[1]] = crates1[el[1]][el[0] + 1:]


print("1. ", end="")
for el in crates:
    print(el[0][1], end="")
print("\n2. ", end="")
for el in crates1:
    print(el[0][1], end="")
    
