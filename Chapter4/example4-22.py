y = int(input("Intput Year Borth :: "))
print(f'Year Borth >> {y}')

gen = ''

if y <= 2443 :
    gen = "Lost Generation"
elif y >= 2444 and y <= 2467 :
    gen = "Greatest Generation"
elif y >= 2468 and y <= 2488 :
    gen = "Silent Generation"
elif y >= 2489 and y <= 2507 :
    gen = "Boomer Generation"
elif y >= 2508 and y <= 2519 :
    gen = "Generation X"
elif y >= 2520 and y <= 2538 :
    gen = "Generation Y"
elif 2539 <= y <= 2555 :
    gen = "Generation Z"

print(f'Generation >> {gen}')