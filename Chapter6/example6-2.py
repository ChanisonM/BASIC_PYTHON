start = 2560
end = 2600
start -= 543
end -= 543

print(f' ระหว่างปี {start} - {end} ปีที่เป็นอธิสุรทินคือ : ')
for year  in range(start , end + 1) :
    if (year % 400 == 0) or (year % 100 != 0 and year % 4 == 0 ):
        print(f'{year + 543}' , ' ' , end='')