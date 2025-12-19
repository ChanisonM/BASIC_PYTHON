odd_nums ={'odd': [1 , 3, 5 , 7 ] , 'even' : range(2,9,2)}
for key in odd_nums :
    print(f'{key} : ' , end=' ')
    for v in odd_nums[key] :
        print(f'{v}' , end=' ')
