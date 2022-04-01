#!/usr/bin/python3 -u
from Crypto.Cipher import DES
import binascii
import itertools
import pwn
import string
import random

def pad(msg):
    block_len = 8
    over = len(msg) % block_len
    pad = block_len - over
    return str(msg + " " * pad).encode('utf-8')

def single_encrypt(m, KEY1):
    msg = pad(binascii.unhexlify(str(m).rstrip()).decode())
    cipher1 = DES.new(KEY1, DES.MODE_ECB)
    return binascii.hexlify(cipher1.encrypt(msg)).decode()

def single_decrypt(msg, KEY1):
    cipher1 = DES.new(KEY1, DES.MODE_ECB)
    return cipher1.decrypt(binascii.unhexlify(msg))

def double_encrypt(m, KEY1, KEY2):
    msg = pad(m)

    cipher1 = DES.new(KEY1, DES.MODE_ECB)
    enc_msg = cipher1.encrypt(msg)
    cipher2 = DES.new(KEY2, DES.MODE_ECB)
    return binascii.hexlify(cipher2.encrypt(enc_msg)).decode()

def double_decrypt(msg, KEY1, KEY2):
    cipher1 = DES.new(KEY2, DES.MODE_ECB)
    enc_msg = cipher1.decrypt(binascii.unhexlify(msg))
    cipher2 = DES.new(KEY1, DES.MODE_ECB)
    return cipher2.decrypt(enc_msg)

def generate_key():
    base = "".join(random.choice(string.digits) for _ in range(6))
    key = pad(base)
    return key

conn = pwn.remote('mercury.picoctf.net', 5958)
conn.recvuntil("Here is the flag:\n")
flag = conn.recvline().decode('utf-8').strip()
conn.recvuntil("What data would you like to encrypt? ")
conn.sendline('111111')
target = conn.recvline().decode('utf-8').strip()
conn.close()
lookup = {}
potential_keys = []
progress_1 = pwn.log.progress(message="Decrypting")
progress_1.status("Computing ENC(m)")
for combo in itertools.product(string.digits, repeat=6):
    key = pad(''.join(combo))
    lookup[single_encrypt('111111', key)] = key
progress_1.status("Computing DEC(c)")
for combo in itertools.product(string.digits, repeat=6):
    key = pad(''.join(combo))
    candidate_pt = binascii.hexlify(single_decrypt(target, key)).decode()
    if candidate_pt in lookup:
        potential_keys.append({lookup[candidate_pt], key})
progress_1.status("Retrieving flag")
for (key1, key2) in potential_keys:
    try:
        progress_1.success()
        pwn.log.success(message=str(double_decrypt(flag, key1, key2).decode()))
        break
    except:
        continue