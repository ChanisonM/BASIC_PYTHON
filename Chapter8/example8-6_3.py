import random , string 
pool = string.ascii_letters + string.digits + string.punctuation
# string.ascii_letters = ข้างในประกอบด้วย: string.ascii_lowercase + string.ascii_uppercase
# ค่าของมันคือ: 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
# string.digits = มันคือ String ที่รวมตัวเลขฐานสิบทั้งหมดเอาไว้ครับ ค่าของมันคือ: '0123456789'
# string.punctuation = รวมสัญลักษณ์พิเศษเช่น !, @, #, $
password = ''.join(random.choice(pool) for i in range(6))
print(f'Your Password is : {password}')