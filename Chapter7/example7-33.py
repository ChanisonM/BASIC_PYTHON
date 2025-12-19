info = {'name' : 'Chanison' , 'age' : 28 , 'height' : 150 , 'single' : True}
for k , v in info.items():
    print(f'Key => {k} \t  value => {v}')

print()
nums_text = {'one':'หนึ่ง' , 'two' : 'สอง', 'three' : 'สาม' }
print(f'three {nums_text.get('three')}')
print(f'one {nums_text.get('one')}')