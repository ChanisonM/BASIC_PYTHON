end = 6
for i in range(1 , end) :
    for j in range(1 ,  end - (i - 1)) :
        print(j , ' ' , end='')
    print()