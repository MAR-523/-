本部分的内容为对sm2算法实现PGP协议，PGP协议包括非对称加密和对称加密两部分，这里sm2应用于非对称加密，而使用AES作为对称加密的算法。  
![PGP设置](https://github.com/MAR-523/-/blob/main/pic/PGP.png)  
主要流程为先对于AES的密钥也就是会话密钥进行sm2公钥加密，再将明文部分利用AES进行加密，之后将两部分内容拼接在一起，发送给接收方。
![PGP调用](https://github.com/MAR-523/-/blob/main/pic/PGP1.png)  
此为输出结果的展示。  
PZueRXt7Q8uR2yKgY5/b6PB/ZCIfaUaJngNTgsgL16iU0THvXh2fv2jQHQ/r0fRMjCx7JDOE9aqpn6R8lXadnljJwGr+8i+2gKaSd3KwM3rEQxcDsaOtfd8EAfA+dairrIEa5XE99SGZW4DnZ7OCxEn0XPQpXaodQ6CUz/rN1dw=  
