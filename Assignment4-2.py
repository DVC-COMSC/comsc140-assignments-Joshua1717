string = (input("Type a word or sentence or type Done, done, or d, to exit: "))
exit_Done = 'Done'
exit_done = 'done' 
exit_d = 'd'

while True:
    
    if string == exit_Done:
        break
    if string == exit_done:
        break
    if string == exit_d:
        break

    reverse = ''
    for i in range(len(string), 0, -1):  
        reverse += string[i-1]

    print('The reverse of', string, 'is', reverse)

    string = (input("Type a word or sentence or type Done, done, or d, to exit: "))

    
  
        

