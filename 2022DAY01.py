lines = []
with open('2022DAY01INPUT.txt') as input:
    for line in input:
        lines.append(line.rstrip())

lines.append("")
totalcalories = []
counter = 0

for line in lines:
    if line.isnumeric():
        counter += int(line)
    else:
        totalcalories.append(counter)
        counter = 0

print("part1: ", max(totalcalories))
totalcalories.sort()
print("part2: ", totalcalories[-1] + totalcalories[-2] + totalcalories[-3])