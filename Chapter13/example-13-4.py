try :
    with open('animals.txt' , mode='w+' , encoding='utf-8') as f:
        f.write('Animals List\n')
        f.write('lion\n')
        f.write('ant\n')
        a = ['cat\n' ,
             'dog\n',
             'pig',
             'dolphin']
        f.writelines(a)
except IOError as err :
    print(err)