from curses.ascii import islower


FLAG  = open('message.txt').read()
output = ''
for i in FLAG.split():
    inv = inverse_mod(int(i), 41)
    print (str(int(i) * int(inv) %41)) 
    if inv < 27:
        output += chr(inv + 64)
    elif inv < 37:
        output += str(inv - 27)
    elif inv == 37:
        output += '_'
        
print(output)