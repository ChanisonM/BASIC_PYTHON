def get_valid_number():
    while True :
        value = input("Please Input Number : ")
        try :
            num = float(value)
            return num
        except ValueError :
            print(f'❌ {value} ไม่ใช่ตัวเลขนะจ๊ะ ลองใหม่อีกครั้ง...')

my_num = get_valid_number()
print(f"✅ ขอบคุณ! คุณกรอกเลข: {my_num}")