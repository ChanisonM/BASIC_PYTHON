tp_thai_digits =('๐','๑',	'๒',	'๓',	'๔', '๕',	'๖',	'๗',	'๘',	'๙')
tp_digit_words = (
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
)
number = input("กำหนดตัวเลขอารบิคเป็นจำนวนเต็มบวก >> ")
number = tuple(number)
thai_digit =''
thai_word = '' 
for i in number :
    i = int(i)
    thai_digit  += tp_thai_digits[i]
    thai_word += tp_digit_words[i]

print(f"เลขไทย :  {thai_digit}")
print(f'คำอ่าน : {thai_word}')