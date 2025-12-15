thai_words =[
'ศูนย์',
'หนึ่ง',
'สอง',
'สาม',
'สี่',
'ห้า',
'หก',
'เจ็ด',
'แปด',
'เก้า'
]

digit = int(input("Please your number only on digit >> "))
if digit in range(0 ,10) :
    read = thai_words[digit]
    print(f'Reed >> {read}')
else :
    print("Please enter a single digit number (0-9) only.")