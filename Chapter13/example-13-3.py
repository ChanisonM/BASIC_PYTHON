try :
    with open('sample.txt' , mode='r' , encoding='utf-8') as f :
        lines = f.readlines()
    print(lines)
    for (i , line) in enumerate(lines) :
        lines[i] = str(line).rsplit('\n')
    print(lines)
except IOError as err:
    print(err)
