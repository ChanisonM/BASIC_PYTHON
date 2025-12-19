count = {'one' : 'หนึ่ง' , 'two' : 'สอง' , 'three' : 'สาม' }
values = count.values()
print(f'ค่าของสมาชิกทั้งหมด : ', end='')
for v in values :
    print(f'{v}' , end=' ')
print()
if 'สาม' in count.values() :
    print('has 3 in ',*count.values())
if 'ห้า' not in count.values() :
    print('not has 5 ' ,*count.values())