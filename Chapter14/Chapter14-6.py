class Calculator :
    pi = 3.141

    @staticmethod
    def add(a , b):
        return a + b
    
    @staticmethod 
    def subtract(a , b):
        return a - b
    
    @staticmethod
    def get_pi():
        return Calculator.pi # Ref. Class Attribute
    
    @staticmethod
    def increment(a) :
        return Calculator.add(a , 1)
    
    @staticmethod 
    def decrement(a) :
        return Calculator.add(a , -1)
    
    @staticmethod
    def multiply(a , b) :
        return a * b
    
    @staticmethod 
    def double_value(a):
        return Calculator.multiply(a , 2)
    
    def square(a):
        return Calculator.multiply(a , a)
    
    def cube(a):
        return Calculator.multiply(a , Calculator.square(a))
                                        # (1) square(10) จะทำ 10 * 10 ซึ่งได้ผลลัพธ์เป็น 100
                        # (2) 10 * 100 จึงได้ผลลัพธ์เท่ากับ 1,000 ครับ
    
print(
    # Calculator.add(10 , 20) ,
    # Calculator.subtract(20 , 5) ,
    # Calculator.get_pi() ,
    # Calculator.increment(99) , 
    # Calculator.decrement(99) ,
    # Calculator.multiply(2 , 2) ,
    # Calculator.double_value(10) , 
    Calculator.square(10) ,
    Calculator.cube(10)
)