import random
file_name = 'lotto.txt'
file = open(file_name , mode='w+' , encoding='utf-8')
dash = '-'*30

def genarate_lotto(length , count) :
    result = []
    for i in range(0 , count) :
        lotto = ''
        for _ in  range(0 , length) :
            r = random.randint(0 , 9)
            lotto += str(r)
        result.append(lotto)
    return result
    
def write_lotto(numbers) :
    for (i , num) in enumerate(numbers):
        t = f'{num}\t'
        if i > 0 and (i+1) % 5 == 0 :
            if i != len(numbers) - 1 :
                t += '\n'
        print(t , end='\n' , file=file)
    print(dash , file=file)

print(f'รางวัลที่ 1' , file=file )
p = genarate_lotto(6 , 1)
write_lotto(p)

print(f'รางวัลเลขท้าย 2 ตัว' , file=file )
p = genarate_lotto(2 , 1)
write_lotto(p) 

print(f'รางวัลเลขหน้า 3 ตัว' , file=file )
p = genarate_lotto(3 , 2)
write_lotto(p) 

print(f'รางวัลที่ 2 ตัว' , file=file )
p = genarate_lotto(6 , 5)
write_lotto(p)  