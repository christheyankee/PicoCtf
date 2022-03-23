from curses.ascii import isalpha, islower, isupper


message = open('message.txt').read()
key = 'KYDSZFEGTIURBNJXVWQAHLMPOC'
alp = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
key = list(key)
print(key)
for (i, char) in enumerate(message):
    if isalpha(char) and isupper(char):
        ascii_code = key.index(chr((ord(char) - 65) + 65))
        message = message[:i] + chr(ascii_code + 65) + message[i + 1:]
    if isalpha(char) and islower(char):
        ascii_code = key.index(chr((ord(char) - 97) + 65))
        message = message[:i] + chr(ascii_code + 97) + message[i + 1:]
print(message)