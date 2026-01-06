from datetime import datetime

print('ถ้าต้องการยกเลิก กด <enter> โดยไม่ต้องใส่ข้อมูล')
try :
    while True :
        with open('log.txt' , mode='a+' , encoding='utf-8') as logfile :
            data = str(input('สิ่งที่เกิดขึ้นในขณะนี้ >> '))
            if data == '' : 
                break
            dt = datetime.now().replace(microsecond=0)
            logfile.write(str(dt) + '--' + data + '\n')


except IOError as err :
    print(err)

