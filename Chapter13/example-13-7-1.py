import time 
from datetime import datetime

print("เริ่มการบันทึกอัตโนมัติทุก 10 วินาที... (กด Ctrl+C เพื่อหยุด)")

try :
    with open('log_auto.txt' , mode='a+' , encoding='utf-8') as log_auto :
        while True :
            dt = datetime.now().replace(microsecond=0)
            data = "บันทึกสถานะระบบปกติ"

            log_auto.write(f'{dt} --- {data}\n')
            log_auto.flush()
            
            print(f"บันทึกแล้วเมื่อเวลา: {dt}")
            
            time.sleep(10)
except IOError as err :
    print(err)
except KeyboardInterrupt as err:
    print(err)

