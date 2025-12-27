def sum_range(begin , end):
    sum = 0
    for x in range(begin , end + 1 ) :
        sum += x
    print(f'summary {begin} - {end} : {sum : ,.2f}')

sum_range(1,10)
sum_range(1,50)