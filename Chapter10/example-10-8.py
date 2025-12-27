
# def is_number(value):
#     if value.isdigit(): return True
#     elif value.count('.') > 1 : return False
#     else :
#         for n in range(0 , len(value)):
#             x = value[n]
#             if (n == 0) and (x == '-' or x == '.' or x == '+'):
#                 continue
#             if x.isdigit() or x == '.' : continue
#             else : return False
#         return True

# value = input("Input Number : ")
# if is_number(value) : print(f'เลขที่ใส่เข้ามา : {value}')
# else : print(f'{value} ไม่ใช่ตัวเลข')



# def is_number(value) :
#     try :
#         float(value)
#         return True
#     except ValueError :
#         return False
    

def is_number(value) :
    try :
        int(value)
        return True
    except ValueError :
        return False
    
value = input("Input Number : ")
if is_number(value) :
    print(f'เลขที่ใส่เข้ามา : {value}')
else :
    print(f'{value} ไม่ใช่ตัวเลข' )