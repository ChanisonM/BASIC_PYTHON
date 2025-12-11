times = 0
valid_code = False 
while not valid_code : #valid_code : True ( not valid_code is False )
    times += 1
    code = int(input("enter your password : "))
    print(f'Insert {times} times : {code} : ' , end='')

    if code == 1234 :
        print("Correct")
        valid_code = True
    else :
        print("wrong")