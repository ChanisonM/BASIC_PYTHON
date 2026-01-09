class Calculator():
    def is_number(self , x) :
        try :
            float(x)
        except ValueError  : return False
        else : return True

    def compute(self , a , b , op) :
        if self.is_number(a) and self.is_number(b) :
            if op == '/' and float(b) == 0 :
                return "ไม่สามารถหารศูนย์ได้"
            
            try :
                return eval(f'{a}{op}{b}')
            except Exception as err :
                return err
        else : return None

    def show_result(self , a , b , op) :
        print(
            f'{a} {op} {b} = ' + \
            f'{self.compute(a , b , op)}'
        )

cal = Calculator()
cal.show_result(2 , 2, '+')
cal.show_result('A'  , 2 , '%')
cal.show_result(2 , 0 , '/')
cal.show_result(2 , 10 , '**')