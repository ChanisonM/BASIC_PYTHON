import random
number = random.randint(1 , 100)
win = False
count = 0
max_count = 7
msg = ''
while not win :
    count += 1
    guess = int(input(f'random : {count} 1 - 100 : '))
    # print(f'No. >> {count} : {guess} => ' , end='')

    if guess > number :
        msg = f'less {guess}'
    elif guess < number :
        msg = f'more {guess}'
    elif guess == number :
        msg = f'Game Clear ^_^ \nRandom is {number}'
        win = True
    print(f'{msg}')

    if (not win) and (count == max_count) :
        print(f'your random {max_count} \n Game Over !! \n Random is {number}')
        break

