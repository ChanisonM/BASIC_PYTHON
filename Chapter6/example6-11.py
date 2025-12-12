w = int(input('width picture : '))
h = int(input('height picture : '))
z = int(input('zoom (%) : '))

ratio = (100 - z) / 100

dw = w * ratio
dh = h * ratio

w -= dw
h -= dh

print(f'Size : {w:.0f} X {h:.0f}')