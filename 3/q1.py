def myFunction(shift_right, shift_down):
    with open('c:/Users/Aryaman Singh/Desktop/Advent Calendar/3/input.txt') as f:
        content = f.readlines()
        content = [(x.strip()) for x in content] 

    position = 0    #from left, index 0
    max_right = len(content[0])
    count = 0

    line_ind = 0
    while line_ind < len(content): 
        line = content[line_ind]
        if line[position] == '#':
            count += 1
            line = line[:position] + 'X' + line[position + 1:]
        else:
            line = line[:position] + 'O' + line[position + 1:]
        # print(line)
        position = (position + shift_right) % max_right
        line_ind += shift_down

    return count

print(myFunction(3, 1))
print(myFunction(1, 1)*myFunction(3, 1)*myFunction(5, 1)*myFunction(7, 1)*myFunction(1, 2))
