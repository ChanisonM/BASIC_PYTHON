lat = eval(input("latitude : "))
print(f'latitude >> {lat} ')
if lat >= -90 and lat <= 90 :
    print('correct latitude')
else : 
    print('wrong latitude (-90 to 90)')

lon = eval(input("longitude : "))
print(f'longitude >> {lon}')
if lon >= -180 and lon <= 180 :
    print('correct longitude')
else :
    print('wrong longitude (-180 to 180)')