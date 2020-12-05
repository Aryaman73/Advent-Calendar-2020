with open('input.txt') as f:
    content = f.readlines()
content = [int(x.strip()) for x in content] 

for ind, val1 in enumerate(content):
    for val2 in content[(ind + 1):]:
        if val1 + val2 == 2020:
            print(val1)
            print(val2)
            print(val1*val2)
            break