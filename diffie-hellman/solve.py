from curses.ascii import isalpha, isdigit, islower, isupper


FLAG  = open('message.txt').read()
p = 13
g = 5
a = 7
b = 3
s = pow(g, a * b, p)
for (i, char) in enumerate(FLAG):
    if isalpha(char) and isupper(char):
        ascii_code = (ord(char) - 65 - s) % 26
        FLAG = FLAG[:i] + chr(ascii_code + 65) + FLAG[i + 1:]
    if isalpha(char) and islower(char):
        ascii_code = (ord(char) - 97 - s) % 26
        FLAG = FLAG[:i] + chr(ascii_code + 97) + FLAG[i + 1:]
    if isdigit(char):
        new_char = (int(char) - s) % 10
        print(char, str(new_char))
        FLAG = FLAG[:i] + str(new_char) + FLAG[i + 1:]
print(FLAG)