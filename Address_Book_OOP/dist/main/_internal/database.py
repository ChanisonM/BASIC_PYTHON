import sqlite3

class AddressBookDB :
    # ฟังก์ชันนี้รันอัตโนมัติ
    def __init__(self , db_name = 'database.db'):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_table()
    
    # ฟังก์ชันสร้างตาราง address_book ในฐานข้อมูล
    def create_table(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS address_book(
                id INTEGER PRIMARY KEY AUTOINCREMENT ,
                name TEXT ,
                address TEXT ,
                phone TEXT ,
                email TEXT ,
                image_path TEXT
                            
            )'''
        )
        self.conn.commit()


    # ฟังก์ชัน เพิ่มข้อมูลลงตาราง address_book
    def insert(self , data) :
        # data หรือ ข้อมูล จะเป็น list เช่น ['ชื่อ', 'ที่อยู่', 'เบอร์', 'อีเมล']
        sql = 'INSERT INTO address_book VALUES(null , ? , ? , ? , ? , ? )'
        self.cursor.execute(sql , data)
        self.conn.commit()
        return self.cursor.rowcount
    

    # ฟังก์ชัน เรัยกดูข้อมูลในฐานข้อมูล ทั้งหมด
    def fetch_all(self):
        sql = 'SELECT * FROM address_book ORDER BY name COLLATE NOCASE ASC'
        self.cursor.execute(sql)
        return self.cursor.fetchall()
    
    # ฟังก์ชัน แก้ไข ข้อมูลในฐานข้อมูล
    def update(self , data , record_id):
        # data = [name, address, phone, email]
        sql = '''
                UPDATE address_book SET  
                name = ? , address = ? , phone = ? , email = ? , image_path = ? 
                WHERE id = ?
            '''
        self.cursor.execute(sql , data + [record_id])
        self.conn.commit()
        return self.cursor.rowcount
    
    # ฟังก์ชัน ลบข้อมูลในฐานข้อมูล
    def delete(self , record_id):
        sql = 'DELETE FROM address_book WHERE id = ? '
        self.cursor.execute(sql , [record_id])
        self.conn.commit()
        return self.cursor.rowcount
    
    def search(self , keyword):
        # ค้นหาชื่อที่มีคำที่กำหนด (ใช้ LIKE %...%)
        query = "SELECT * FROM address_book WHERE name LIKE ?"
        self.cursor.execute(query , ('%' + keyword +'%',))
        return self.cursor.fetchall()



    # ฟังก์ชันปิดฐานข้อมูลเพื่อคืนทรัพยากร์ของระบบ
    def close(self):
        self.conn.close()
       


if __name__ == '__main__' :
    db = AddressBookDB()

    # # ทดสอบเพิ่มข้อมูล
    # test_data = ['สมชาย สายลม', 'กรุงเทพฯ', '0812345678', 'somchai@email.com']
    # db.insert(test_data)
    # print("เพิ่มข้อมูลทดสอบเรียบร้อย!")

    # # ทดสอบดึงข้อมูลมาดู
    # rows = db.fetch_all()
    # print("ข้อมูลทั้งหมดในฐานข้อมูล:")
    # for r in rows :
    #     print(r)