import random

secret_number = random.randint(1,10)
count_game = 0

print('=== Random Number Game ===')

while True :

    try :
        guess = int(input("Input Your Number : "))
        count_game += 1


        if guess == secret_number :
            print(f"🎉 ยินดีด้วย! คุณทายถูกแล้ว เลขนั้นคือ {secret_number}")
            print(f"📊 คุณใช้ความพยายามทั้งหมด: {count_game} ครั้ง")
            break
        elif guess < 1 or guess > 10 :
            print("⚠️ กรุณาทายเลขในช่วง 1-10 เท่านั้นนะ")
        elif count_game == 5 :
            print("--- Game Over ---")
            break
        else :
            remaining = 5 - count_game
            print(f"❌ ยังไม่ใช่ครับ (เหลือโอกาสอีก {remaining} ครั้ง)")
        
    except ValueError:
        print("⚠️ ผิดพลาด! กรุณาใส่เฉพาะตัวเลข 1-10 เท่านั้นครับ")

print("--- End Game ---")