import math
import random
import time
import string

#SM3算法
IV=['7380166f','4914b2b9','172442d7','da8a0600','a96f30bc','163138aa','e38dee4d','b0fb0e4e']
T_all=['79cc4519','7a879d8a']


def str2byte(m): #str转换成byte数组
    m_mid=len(m)
    m_byte=[]
    m_bytearray=m.encode('utf-8')
    for i in range(m_mid):
        m_byte.append(m_bytearray[i])
    return m_byte

def FF(x,y,z,j):
    if j<=15:
        return x^y^z
    else:
        return (x&y)|(x&z)|(y&z)

def GG(x,y,z,j):
    if j<=15:
        return x^y^z
    else:
        return (x&y)|(~x&z)


def leftmov(m,num):  #向左移动
    num=num%32
    m=bin(m).replace('0b','').zfill(32)
    m_left=m[num:]+m[:num]
    return int(m_left,2)
    
def P0(x):
    return x^leftmov(x,9)^leftmov(x,17)
def P1(x):    
    return x^leftmov(x,15)^leftmov(x,23)
    
#消息填充
def msgpop(m):
    m=str(m) #输入的内容作为str
    lenth=len(m)
    l=lenth*8
    m_midarray=str2byte(m)
    m_midarray.append(128) #1000 0000=128
    need0=64-lenth-1-8
    for i in range(need0):
        m_midarray.append(0)
    arr_len=len(m_midarray)
    string=""
    for j in range(arr_len):
        string+=bin(m_midarray[j]).replace('0b','').zfill(8)
    add_len=bin(l).replace('0b','').zfill(64)
    string+=add_len
    return string

#消息扩展和迭代压缩
def msgexpd(m):
    B1=[]
    B2=[]
    T=[]
    T.append(int(T_all[0],16))
    T.append(int(T_all[1],16))
    for i in range(16):
        mid_str=m[32*i:32+32*i]
        B1.append(int(mid_str,2)) 
    for j in range(16,68):
        num=B1[j-16]^B1[j-9]^leftmov(B1[j-3],15)
        mid=P1(num)
        re=mid^leftmov(B1[j-13],7)^B1[j-6]
        B1.append(re)
    for k in range(64):
        mid=B1[k]^B1[k+4]
        B2.append(mid)
    #return B1,B2 B1是W,B2是W'
    #print(B1,B2)
    iv=[]
    for i in range(8):
        iv.append(int(IV[i],16))
    A=iv[0]
    B=iv[1]
    C=iv[2]
    D=iv[3]
    E=iv[4]
    F=iv[5]
    G=iv[6]
    H=iv[7]
    toolnum=2**32
    for j in range(64):
        if j<=15:
            mid1=(leftmov(A,12)+E+leftmov(T[0],j))%toolnum
        else:
            mid1=(leftmov(A,12)+E+leftmov(T[1],j))%toolnum
        SS1=leftmov(mid1,7)#SS1
        SS2=(SS1^leftmov(A,12))%toolnum
        TT1=(FF(A,B,C,j)+D+SS2+B2[j])%toolnum
        TT2=(GG(E,F,G,j)+H+SS1+B1[j])%toolnum
        D=C
        C=leftmov(B,9)
        B=A
        A=TT1
        H=G
        G=leftmov(F,19)
        F=E
        E=P0(TT2)
    
    v_new=[]
    v_new.append(A^iv[0])
    v_new.append(B^iv[1])
    v_new.append(C^iv[2])
    v_new.append(D^iv[3])
    v_new.append(E^iv[4])
    v_new.append(F^iv[5])
    v_new.append(G^iv[6])
    v_new.append(H^iv[7])
    return v_new

def sm3(msg): #sm3整合
    mid1=msgpop(msg)
    v_new=msgexpd(mid1)
    final=""
    miwen=""
    for i in range(8):
        final+=bin(v_new[i]).replace('0b','').zfill(32)
    return final
#256位的输出


#生日攻击
def getlist(n,max_num):
    randlist=[]
    while len(randlist1)<n:
        x=random.randint(0,max_num)
        if x not in randlist:
            randlist.append(x)
    return randlist

def birth(n):
    max_num=2**n
    rand_num=int(max_num**0.25)
    #rand_num=int(max_num**0.5)

    while True:
        lst1_val=[]
        lst2_val=[]
        lst1=getlist(rand_num,max_num)
        lst2=getlist(rand_num,max_num)
        for i in range(rand_num):
            lst1_val.append(sm3(lst1[i])[0:n])
            lst2_val.append(sm3(lst2[i])[0:n]) 
        col=set(lst1_val)&set(lst2_val)
        if not col:
            continue
        else:
            col=str(list(col)[0])
            num1=lst1_val.index(col)
            num2=lst2_val.index(col)
            if lst1[num1]==lst2[num2]:
                continue
            else:
                break
    print('前',n,'位相等,find x1:',lst1[num1],' and x2:',lst2[num2])

#开始测试
t1=time.time()
birth(n) #需要前n位相等，求出这两个数并且计算花费时间
t2=time.time()
print("用时：",t2-t1)
