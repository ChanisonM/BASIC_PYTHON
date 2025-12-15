a = [1,2,3,3,4,4,5]
i = a.index(3) # .index() หาตัวเลข 3 ที่เจอเป็นตัวแรก แล้วแสดง index ออกมา 
print(f'index of {i}') 

if 4 in a :
    print(f'index of {a.index(4)}')

a.insert(2,3.5)
print(a)

if 2 in a :
    a.remove(2)
    print(a)