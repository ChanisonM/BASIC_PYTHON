weight = eval(input("weight (kilogram) : "))
height = eval(input("height (cm) : "))

height /= 100 # cm => m
bmi = weight / (height ** 2)

print(f'BMI : {bmi : 0.2f}')
msg = 'ลักษณะรูปร่าง : '

if bmi >= 40 : msg += "อ้วนขั้นสุด"
elif bmi >= 35 : msg += "อ้วนขั้นที่ 2"
elif bmi >= 28.5 : msg += "อ้วนขั้นที่ 1"
elif bmi >= 23.5 : msg += "น้ำหนักเกิน"
elif bmi >= 18.5 : msg += "น้ำหนักอยู่ในเกณปกติ"
else : msg += "น้ำหนักต่ำกว้าเกณ"
print(msg)