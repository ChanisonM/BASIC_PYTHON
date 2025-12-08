time_seconds = int(input("กำหนดเป็นวินาที : "))
print(f'time_seconds : {time_seconds}')
hours = time_seconds // 3600
remain = time_seconds % 3600
minutes = remain // 60
seconds = remain % 60

print(f'hours : {hours}')
print(f'minutes : {minutes}')
print(f'seconds : {seconds}')