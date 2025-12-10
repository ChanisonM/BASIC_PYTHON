# 1.
# temp = int(input('Enter Your Temp :: '))
# is_rainy = False 
# if temp > 30 or not is_rainy :
#     print('Perfect')
# else :
#     print("Change Plans")

# 2.
# has_membership = True 
# purchase_amont = 1500
# if has_membership:
#     print("Gold Discount") if purchase_amont > 1000 else print("Silver Discount")
# else :
#     print("Standrad Discount")

# 3.
# is_mumber = True
# is_weekend = False 
# print("Special Deal") if is_mumber and not is_weekend else print("Normal Price")

# 4.
# temp = 0
# print("None-Zero") if temp else print("Zero")

# 5.
# data_a = [1,2] # มองว่าเป็น True
# data_b = [] # มองว่าเป็น False
# print("Has Data") if data_a or data_b else print("empty")

# 6.
# x = 20 
# y = 10
# z = x % y
# print(z)
# if x % y == 0 and x > y :
#     print("A")
# elif x / y == 2 :
#     print("B")
# else :
#     print("C")

# 7.
# name = "Alice"
# if name == "alice" :
#     print("Lowcase")
# elif name != "alice" :
#     print("Not Lowcase")
# else :
#     print("Someting else")

value = 10.5
if type(value) is int :
    print("Integer")
elif type(value) is float :
    print("Float")
else :
    print("Someting else")