try :
    f = open('sample.txt' , mode='r' , encoding='utf-8')
    print(f.read())
    print('-'*20)
    
except IOError as err :
    print(err)
else :
    f.close()
