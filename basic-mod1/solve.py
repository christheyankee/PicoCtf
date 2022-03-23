from curses.ascii import islower


FLAG  = open('message.txt').read()
output = ''
for i in FLAG.split():
    i = int(i)%37
    if i < 26:
        output += chr(i + 65)
    elif i == 36:
        output += '_'
    else:
        output += str(i - 26)
print(output)