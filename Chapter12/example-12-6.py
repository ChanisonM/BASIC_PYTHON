from datetime import datetime

months_th = [
    "มกราคม", "กุมภาพันธ์", "มีนาคม", "เมษายน", "พฤษภาคม", "มิถุนายน",
    "กรกฎาคม", "สิงหาคม", "กันยายน", "ตุลาคม", "พฤศจิกายน", "ธันวาคม"
]

msg = "What is Your Birthday (dd / mm / yy) : "

while True :
    birthday = input(msg).replace(" ","")
    birthday.split() # ตัดช่องว่าหัว-ท้าย
    print(f'>> {birthday}')

    try :
        bd = datetime.strptime(birthday , '%d/%m/%Y')
        dmy = f'{bd.day} {months_th[bd.month - 1]} {bd.year + 543}'
        print(f'Your Birthday : {dmy}')
        break
    except :
        err = 'dd / mm / yy  not curect !! \n' \
        'Please Input Your Birthday (dd / mm / yy) Again !! '
        print(err)
