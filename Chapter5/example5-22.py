code = 1234
max_times = 3
times = 0

while True:
    times += 1
    c = int(input(f' Plase Code No.{times} : '))
    print(f'times : {times} >> Code : {c} ' , end='')
    if c == code :
        print("Correct")
        break
    else :
        print("Wrong")
    
    if times == max_times :
        print(f'fail password {max_times} times is cancel')
        break
