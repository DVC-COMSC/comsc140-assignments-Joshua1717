
x = (int(input("Enter a number: ")))
inputnumber = x
remainder = ''

while True:
    if(0 < x < 32767):
        mod = x % 2
        remainder = remainder + str(mod)
        x = (x // 2)
   
    elif x == 0:
        break
        
    else: 
        x = (int(input("Try again with a number between 0 and 32767: ")))
        inputnumber = x

print('The reverse binary vaule of', inputnumber, 'is', remainder)





    
   
#else: num = (int(input("Enter a number between 0 and 32767: ")))

