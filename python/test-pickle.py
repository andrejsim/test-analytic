import pickle
import numpy as np
import os
import timeit

myarr = np.zeros((1000, 1000))

# with open('./data/file.bin', 'w+b') as f:
#     f.write(myarr)
#
# with open("./data/save.p", "w+b") as f:
#     pickle.dump(myarr, f)

%timeit
np.fromfile(open('../data/file.bin', 'rb')).size
%timeit
pickle.load(open("../data/save.p", "rb")).size

# Client:
import socket

HOST = 'localhost'
PORT = 50007
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
arr = ([1,2,3,4,5,6],[1,2,3,4,5,6])
data_string = pickle.dumps(arr)
s.send(data_string)

data = s.recv(4096)
data_arr = pickle.loads(data)
s.close()
print('Received: '+str(repr(data_arr)))


#---Server:
import socket

HOST = 'localhost'
PORT = 50007
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)
conn, addr = s.accept()

while 1:
    data = conn.recv(4096)
    if not data: break
    conn.send(data)
conn.close()