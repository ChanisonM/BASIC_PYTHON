# isalnum() เป็นตัวอักขร หรือ ตัวเลขทั้งหมด
print('123214'.isalnum())
print('Pthon123'.isalnum())
print('asdas3.2'.isalnum())
print('asd swe'.isalnum())
print("----------------")

# isalpha() ต้องเป็นตัวอักขรทั้งหมด
print('asdasd'.isalpha())
print('123'.isalpha())
print("----------------")

# isdecimal() , isdigit() , isnumeric ต้องเป็นตัวเลขทั้งหมด
print('123213'.isdecimal())
print("3123".isdigit())
print('1454'.isnumeric())
print("----------------")

# islower() , isupper() , istitle , isspace 
print('python'.islower())
print('PYTHON'.isupper())
print("Welcom Python".istitle())
print(''.isspace())
print(' '.isspace())