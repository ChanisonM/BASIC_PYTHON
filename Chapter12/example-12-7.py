import random

numbers_th = [
    "ศูนย์","หนึ่ง", "สอง", "สาม", "สี่", "ห้า", 
    "หก", "เจ็ด", "แปด", "เก้า", "สิบ"
]

r = random.randint(0,10)
try :
    word = numbers_th[r]
    print(f'{r} is {word}')
except :
    print("Error !! Index over list")
finally :
    print(f"Number Random : {r}")