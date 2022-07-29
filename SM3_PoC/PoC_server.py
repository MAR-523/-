#coding=utf-8
from gmssl import sm3,func
import random
from json import dumps
from socket import socket,AF_INET,SOCK_DGRAM

secret_key = 13
n = 29
HOST = ''
PORT = 1000
client = socket(AF_INET,SOCK_DGRAM)
client.bind((HOST, PORT))

print("成功建立连接")

#此时成功从客户端获得(key,value)
key,addr = client.recvfrom(1024)
value,addr = client.recvfrom(1024)
key = int(key.decode(),16)
value = int(value.decode(),16)

#建立一个(key,value)的表
kv_table = []
for i in range(pow(2,16)): #控制表的大小
    h = sm3.sm3_hash(func.bytes_to_list((str(i) + str(random.randint(1,i+10))).encode('utf-8'))) #这里可以随意选择
    kv_table.append(h)
    
# 计算h^ab
hab=(pow(value,secret_key))%n

#计算根据k找到的集合
S = []
for t in kv_table:
    if t[:2] == key:
        S.append(hex((pow(t,secret_key))%n))

print("输出的数据集S为:",S)


# 向客户端发送hab与数据集S，并结束操作
client.sendto(hex(hab).encode(),addr)
json_S = dumps(S)
client.sendto(json_S.encode('utf-8'),addr)
client.close()

