# import sys
with open('input.txt') as f:
    content = f.readlines()
content = [(x.strip()) for x in content] 

validCount = 0

for line in content:
    a, rest = int(line.split('-')[0]), line.split('-')[1]
    b, letter, word = int(rest.split(' ')[0]), rest.split(' ')[1].split(':')[0], rest.split(' ')[2]
    if (word[a - 1] == letter and word[b - 1] != letter) or (word[a - 1] != letter and word[b - 1] == letter) :
        validCount += 1
        # print("Bingo")
    

print(validCount)