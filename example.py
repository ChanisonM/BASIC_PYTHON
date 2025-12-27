import random
# def create_order(customer_name , *items , **details):
#     """
#     ฟังก์ชันรับออเดอร์:
#     - customer_name: ชื่อลูกค้า (บังคับใส่)
#     - *items: รายการอาหาร (กี่อย่างก็ได้)
#     - **details: ข้อมูลเพิ่มเติม เช่น 'โต๊ะ', 'หมายเหตุ'
#     """
#     print(f'---- Order for {customer_name} ---')

#     for _ in range(3) : print("-" , end='')
#     print()

#     if items :
#         print(f'Items : {', '.join(items)}')

#     for key , value in details.items():
#         print(f'{key.capitalize()} : {value}')
    
#     order_id = random.randint(1000,9999)
#     print(f'Order ID : {order_id}')
#     print()

# create_order("Chanison", "Pizza", "Pasta", "Coke", table=5, note="No spicy")


# def check_kwargs(**details):
#     # ลองสั่ง print ดูว่ามันหน้าตาเป็นยังไง
#     print(details)


# check_kwargs(table=5, note="No spicy")


def calculate_bill(customer , price , **extras) :
    total = price
    # 1. ดึงเลขโต๊ะออกมา (ถ้าไม่ระบุมา ให้เป็นคำว่า 'Take away')
    table = extras.get('table' ,'Take away')
    # 2. เช็คว่าถ้าเป็น 'นั่งทานที่โต๊ะ' ให้บวกค่า Service Charge 20 บาท
    if 'table' in extras :
        service_charge = 20
        total += service_charge
        print(f'Cutomer {customer} No. {table}')
        print(f'Sevice Charge {service_charge} Bath')
    else :
        print(f'Customer {customer} (Take away)')
    
    # 3. ดึงส่วนลด (ถ้ามี)
    discout = extras.get('discount' , 0) # ถ้าไม่มี ให้ส่วนลดเป็น 0
    total -= discout
    print(f'Discount {discout} bath')
    print(f'{total} bath')
    print('-'*20)

# --- ทดลองเรียกใช้แบบต่างๆ ---
# เคสที่ 1: นั่งทานที่โต๊ะ 5 และมีส่วนลด 50 บาท
calculate_bill("Somchai", 500, table=5, discount=50)

# เคสที่ 2: สั่งกลับบ้าน (ไม่ส่งค่า table มา)
calculate_bill("Wichai", 300)
    
