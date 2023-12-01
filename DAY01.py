lines = []
with open('DAY01INPUT.txt') as input:
    for line in input:
        lines.append(line.rstrip())

# #PART ONE
# values = []
# value = ""

# for line in lines:
#     value += (next(i for i in line if i.isnumeric())) 
#     value += (next(i for i in reversed(line) if i.isnumeric()))
#     values.append(int(value))
#     value = ""
# print(sum(values))

#PART TWO
values = []
numberobject = {"one": "one1one", "two": "two2two", "three": "three3three", "four": "four4four", "five": "five5five", "six": "six6six", "seven": "seven7seven", "eight": "eight8eight", "nine": "nine9nine"}

for line in lines:
    for key, value in numberobject.items():
        line = line.replace(key, value)
    line = "".join(filter(str.isdigit, line))
    values.append(int(line[0] + line[-1]))
print(sum(values))
