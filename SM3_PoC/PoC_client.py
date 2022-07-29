#coding=utf-8
from gmssl import sm3,func
import sys
from json import loads,dumps
from socket import socket,AF_INET,SOCK_DGRAM

secret_key = 7
n = 29
username = b"201900"
password = b"460044"

HOST = '127.0.0.1'
PORT = 1000
client =socket(AF_INET, SOCK_DGRAM)

def get_inverse(value, p):
    for i in range(1, p):
        if (i * value) % p == 1:
            return i
    return -1

try:
    client.connect((HOST, PORT))
    print("连接成功")
except Exception:
    print('连接失败')
    sys.exit()
else:
    # 如果能够连接成功，则客户端计算一个(key,value)
    up=username+password
    h = sm3.sm3_hash(func.bytes_to_list(up))
    key = h[:2]
    value = str(hex(pow(int(h,16),secret_key)%n))

    #发送一组(key,value)，从服务器端接收H_ab与数据集S
    dst_addr = (HOST, PORT)
    key=key.encode('utf-8')
    value=value.encode('utf-8')
    client.sendto(key, dst_addr)
    client.sendto(value, dst_addr)
    H_ab,addr = client.recvfrom(8192)
    H_ab = int(H_ab.decode(),16)
    json_v,addr = client.recvfrom(8192)
    json_v = json_v.decode('utf-8')
    S = loads(json_v)
    print("得到的数据集S为:",S)

    #检查H_b是否在S中，即验证账号的安全性
    H_b = (pow(H_ab,get_inverse(secret_key,n-1)))%n
    tem = 1
    for i in S:
        if i == H_b:
            tem = 0
    if tem == 1:
        print('该账号:',username,'是安全的')
    else:
        print('账号',username,'是不安全的')
