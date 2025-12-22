# from Error import Error

code_format =" *9999*XXXXXXXXXX#"
code = input(f'Please inseat code format {code_format} : ')
errors = []


if len(code) != 17 :
    errors.append(f"Format length must be exactly 17 characters (Current: {len(code)})")
else :
    for i , c in enumerate(code) :
        if i in [0,5] and c != '*' :
            errors.append(f'Index {i+1}: expected "*"')
        elif i in range(1,5) and c != '9' :
            errors.append(f'Index {i+1}: expected "9"')
        elif i in range(6,16) and not c.isdigit():
            errors.append(f'Index {i+1}: expected digit (0-9)')
        elif i == 16 and c != '#' :
            errors.append(f'Index {17}: expected "#"')

if not errors :
    print(f"✅ Code {code} is correct!")
else :
    print("❌ Invalid Password:")
    for err in set(errors) :
        print(f'    -{err}')