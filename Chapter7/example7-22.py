constellations = ('ปีชวด' , 'ปีฉลู ', 'ปีขาล' , 'ปีเถาะ' , 'ปีมะโรง' , 'ปีมะเส็ง' , 'ปีมะเมีย' , 'ปีมะแม')
symbols = ('หนู',
'วัว',
'เสือ',
'กระต่าย',
'มังกร',
'งู',
'ม้า',
'แพะ',
'ลิง',
'ไก่',
'สุนัข',
'หมู')

year_begin = 2566
year_end = 2570
for y in range(year_begin , year_end + 1) :
    n = (y + 5) % 12 
    print(n)
    print(
        f'ปี {y} ตรงกับปีนักษัตร : {constellations[n]}\t'
        f'สัตว์ลัญลักษณ์ {symbols[n]}'
    )
