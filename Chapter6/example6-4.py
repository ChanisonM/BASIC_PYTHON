# 1 km =
ft = 3_280.84 #foot
yd = 1_093.61 # yard
ml = 0.62 # mile

# Head Table
print("กิโลกรัม \t ฟุต\t\t หลา\t\t ไมล์")
for km in range(1, 11) :
    print(
        f'{km}\t' ,
        f'{km * ft : ,.2f}\t',
        f'{km * yd : ,.2f}\t',
        f'{km * ml : ,.2f}',
        sep=''
    )