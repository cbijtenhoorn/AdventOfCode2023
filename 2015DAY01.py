# with open('2015DAY01INPUT.txt') as input:
#     for line in input:
#         instructions = [*line]
instructions = open("2015DAY01INPUT.txt").read()

counter = 0
# index = 0 #PART TWO
for step in instructions:
    # index += 1 #PART TWO
    if step == '(':
        counter += 1
    if step == ')':
        counter -= 1
    # if counter < 0: #PART TWO
    #     break
    

# print(counter)
# print(index) #PART TWO