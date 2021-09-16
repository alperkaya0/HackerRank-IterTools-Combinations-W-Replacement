# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations_with_replacement

inp = input().split(" ")
text = inp[0]
num = int(inp[1])

liste = list(combinations_with_replacement(text,num))







newL = []
for x in liste:
    temp = []
    for char in x:
        temp.append(char)
    temp.sort()
    newL.append(temp)
    



newL.sort()

for x in newL:
    temp = ""
    for char in x:
        temp += char
    print(temp)
