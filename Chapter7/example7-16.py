score = []
for i in range(6):
    n = int(input(f'Score of Studen / Person {i + 1} >> '))
    if n in range(0 , 101):
        score.append(n)

print(f'Score : {score}')
top = max(score)
print(f'Top :: {top}')

for i , sc in enumerate(score) :
    g = 'F'
    d = top - score[i]
    if d <= 10 : g = 'A'
    elif d <= 20 : g = 'B'
    elif d <= 30 : g = 'C'
    elif d <= 40 : g = 'D'
    print(f'Student {i + 1} Score >> {score[i]} Grade : {g}')

    
    # คำสั่ง d = top - score[i] 
    # มีวัตถุประสงค์เพื่อคำนวณว่า "คะแนนของนักเรียนคนปัจจุบัน ห่างจาก คะแนนสูงสุดของห้องเรียนเป็นจำนวนกี่คะแนน"
    # ตัวอย่าง:สมมติว่า คะแนนสูงสุด (top) คือ 95
    # นักเรียนคนที่ 3 มี คะแนน (score[i]) คือ 88
    # การคำนวณ: $d = 95 - 88$ผลลัพธ์: $d = 7$
    # ความหมาย: คะแนนของนักเรียนคนนี้ห่างจากคะแนนสูงสุดอยู่ 7 คะแนน