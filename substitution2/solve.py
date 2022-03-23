from curses.ascii import isalpha, islower, isupper


message = open('message.txt').read()
key = {
    'A' : '?', 'B' : '?', 'C' : '?', 'D' : '?', 'E' : '?', 'F' : 'O', 
    'G' : '?', 'H' : 'G', 'I' : 'L', 'J' : 'E', 'K' : 'H', 'L' : 'U', 
    'M' : 'S', 'N' : '?', 'O' : 'D', 'P' : 'I', 'Q' : 'F', 'R' : 'N', 
    'S' : 'M', 'T' : '?', 'U' : 'P', 'V' : 'R', 'W' : '?', 'X' : 'T', 
    'Y' : 'C', 'Z' : 'Y'
}
print(key)
for (i, char) in enumerate(message):
    if isalpha(char) and isupper(char):
        conv = key[chr((ord(char) - 65) + 65)]
        message = message[:i] + chr(ord(conv)) + message[i + 1:]
    if isalpha(char) and islower(char):
        conv = key[chr((ord(char) - 97) + 65)]
        message = message[:i] + chr(ord(conv) - 65 + 97) + message[i + 1:]
print(message)