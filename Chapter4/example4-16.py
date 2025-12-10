scroe = int(input("Scroe (0 - 100 ) : "))
print(f'scroe >> {scroe}')

if scroe >= 80 : grade ='A'
elif scroe >= 70 : grade = 'B'
elif scroe >= 60 : grade = 'C'
elif scroe >= 50 : grade = 'D'
elif scroe < 50 : grade = "F"

print(f'Score : {scroe} Grade : {grade}')