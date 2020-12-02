with open('input.txt') as f:
    content = f.readlines()
content = [int(x.strip()) for x in content] 

for ind, val1 in enumerate(content):
    for ind2, val2 in enumerate(content[(ind + 1):]):
        for val3 in (content[(ind + ind2 + 2):]):
            # print(val1, val2, val3)
            if val1 + val2 + val3 == 2020:
                print(val1)
                print(val2)
                print(val3)
                print(val1*val2*val3)
                break