string = input('Input your word >> ')
char = {}
for c in string :
    if c == ' ' :
        continue 
    if c in char.keys() :
        char[c] += 1
    else :
        char[c] = 1

for k in char.keys() :
    print(f'{k} : {char[k]}')