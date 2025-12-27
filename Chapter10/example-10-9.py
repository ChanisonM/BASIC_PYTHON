import random
# def random_3_digits() :
#     a = random.randint(0,9)
#     b = random.randint(0,9)
#     c = random.randint(0,9)
#     r = [a , b , c]
#     return r

# data = random_3_digits()
# print(data)
# for x in random_3_digits() : print(x)

def random_3_digits() :
    return [random.randint(0 ,9) for _ in range(3)]

data = random_3_digits() 
print(data) 