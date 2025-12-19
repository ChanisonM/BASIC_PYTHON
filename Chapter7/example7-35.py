data = [
    ['Thailand' , 'Japan'] ,
    ['UK' , 'Germany'] ,
    ['USA' ,'Canada']
]
# print(data[0])
# print(data[0][1])
# print(data[1])
# print(data[1][0])
# print(data[2])
# print(data[2][1])


# for d in data :
#     for c in d :
#         print(c , end=' ')


for i , d in enumerate(data) :
    print(i + 1 , end=': ')
    for j , c in enumerate(d):
        if j < 1 :
            print(c)

    