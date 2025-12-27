import random , string

# def lottery(length):
#     result =''
#     for _ in range(0 , length) :
#         r = random.randrange(0 , 10) 
#         result += str(r)
#     return result

# print(
#     f'รางวัลที่ 1 : {lottery(6)} \n'
#     f'รางวัลเลขที่ 3 ตัว {lottery(3)} , {lottery(3)}'
# )


def generate_lotto(*lengths) :
    """
    รับความยาวกี่รางวัลก็ได้ (args) 
    แล้วคืนค่ากลับไปเป็น List ของรางวัลที่สุ่มได้
    """
    result = []
    for length in lengths :
        num = ''.join(random.choices(string.digits , k=length))
        result.append(num)
    return result

prizes = generate_lotto(6 , 3 , 3 , 2)

print(f'รางวัลที่ 1 : {prizes[0]}')
print(f'เลขท้าย 3 : {prizes[1] , prizes[2]}')
print(f'เลขท้าย 2 : {prizes[3]}')



