rudeWords = ['xx' , 'yy' , 'zz']
msg = 'asdasd xx  asdasd yy zz '
print(f'message : {msg}',end='\n')
for r in rudeWords :
    msg = msg.replace(r , '***')

print()
print(f'New Message {msg}' ,sep='\n')