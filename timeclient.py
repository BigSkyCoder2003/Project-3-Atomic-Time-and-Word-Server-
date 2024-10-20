import sys
import socket
import time

webAddress = 'time.nist.gov'
remotePort = 37

print('Welcome... to time.')

s=socket.socket()

remote = (webAddress,remotePort)

s.connect(remote)

def system_seconds_since_1900():
    """
    The time server returns the number of seconds since 1900, but Unix
    systems return the number of seconds since 1970. This function
    computes the number of seconds since 1900 on the system.
    """

    # Number of seconds between 1900-01-01 and 1970-01-01
    seconds_delta = 2208988800

    seconds_since_unix_epoch = int(time.time())
    seconds_since_1900_epoch = seconds_since_unix_epoch + seconds_delta

    return seconds_since_1900_epoch

data  = s.recv(4)
nistTime = int.from_bytes(data, 'big')
print(f'UNIX NIST TIME:{nistTime}\nUNIX LOCAL SYSTEM TIME:{system_seconds_since_1900()}')
time_difference = abs(nistTime - system_seconds_since_1900())
if nistTime >0:
    print(f'TIME DIFFERENCE:{time_difference} second(s) off')
s.close()
        



        