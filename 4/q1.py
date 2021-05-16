with open('c:/Users/Aryaman Singh/Desktop/Advent Calendar/4/input.txt') as f:
    content = f.readlines()
content = [(x.strip()) for x in content] 

print(content[:10])