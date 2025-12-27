import random 

def rand(start , end , length) :
    # chars = ''
    # for _ in range(length) :
    #     x = random.randint(ord(start) , ord(end))
    #     chars += chr(x)

    chars =  [chr(random.randint(ord(start) , ord(end))) for _ in range(length)]
    return ''.join(chars)

def random_A_Z(length) :
    result = rand('A' , 'Z' , length)
    return result

def random_a_z(length) :
    return rand('a' , 'z' , length)
    
print(f'Uppercase : {random_A_Z(5)}')
print(f'Lowercase : {random_a_z(7)}')