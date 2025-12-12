year = int(input('ปี ค.ศ ที่ต้องการตรวจสอบ : '))
if (year % 400 == 0) or (year % 100 != 0 and year % 4 == 0) :
    print(f'ปี ค.ศ {year} เป็นปีอธิกสุรทิน')
else :
    print(f'ปี ค.ศ {year} ไม่เป็นปีอธิกสุรทิน')