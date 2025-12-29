while True :
    try :
        x = input("Please Input Your Number : ")
        print(f'>> {x}')
        x = int(x)
        break
    except :
        print("Data not current !!")

print("Thank You !!!")