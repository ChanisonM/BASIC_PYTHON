score = 0 
raters = 0
for i in range(1 , 8) :
    rate = int(input(f'คนที่ {i} ให้กี่ดาว (1 - 5) : '))
    if rate in range(1,6) :
        score += rate
        raters += 1
       
# print(f'score : {score}')
# print(f'raters : {raters}')

average = 0
stars = 0

if score > 0 :
    average = score / (raters * 5) # 7 / (7 * 5) = 7 / 35 = 0.4

if average >= 0.8 :
    stars = 5
elif average >= 0.6 :
    stars = 4
elif average >= 0.4 :
    stars = 3
elif average >= 0.2 :
    stars = 2 
elif average > 0 :
    stars = 1

print(f'average : {average : .2f}' , end="\n")
print(f'rating : {"*" * stars}')
