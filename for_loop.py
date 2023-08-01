#Bigtin v1 7-31-23
#vars
i = 1
factor = 256
answer = 0
for i in range (1, factor):
    answer = factor / i
    
    if factor < factor/2:
        continue
    elif answer.is_integer():
        print('---\r',i)
        print(answer)
    
    else:
        continue
