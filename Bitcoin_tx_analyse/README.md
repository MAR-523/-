# 在比特币测试网上发起一笔交易，再对交易原始内容进行解码
首先需要下载[Electrum 工具](https://electrum.org/#download)  
![image](https://github.com/MAR-523/-/blob/main/pic/1.png)  
在之后运行程序获得很多组钱包和私钥，这里选第一组  
![image](https://github.com/MAR-523/-/blob/main/pic/5.png)  
可以通过[水龙头](https://testnet-faucet.mempool.co/) 免费获取测试比特币  
一系列准备操作完成之后  
进行比特币交易之后可以看到txid:  
![image](https://github.com/MAR-523/-/blob/main/pic/2.png)
同时通过[网站BLOCKCYPHER](https://live.blockcypher.com/btc-testnet/)通过txid可以查询交易细节：  
![image](https://github.com/MAR-523/-/blob/main/pic/3.png)  
要求对**交易原始内容**进行分析，因此借助SoCain输入txid后进行查询：  
![image](https://github.com/MAR-523/-/blob/main/pic/4.png)  
输出结果：  
**01000000015235929eaa6f0f336caad4653c8561ace3ed0e99cb97a8714c4bb57a11d4b81c010000006a473044022011d906321c6c538a298ae46fe317bba97ad897814ec9102dd001e12628789e8f022042955ad619531432774388fac48e16fc3c99755f18f2003e51de17c45ad9c9e90121037435c194e9b01b3d7f7a2802d6684a3af68d05bbf4ec8f17021980d777691f1dffffffff01640000000000001976a914df3488394c31e4d82660f9f685e12f8fa22e3dff88ac00000000**  
接下来对交易原始数据进行解码：  
**01000000**交易的版本号（固定长度四字节，这里填充为四个字节的数据后倒序）  
**01**交易输入的个数  
**5235929eaa6f0f336caad4653c8561ace3ed0e99cb97a8714c4bb57a11d4b81c**UTXO  
他这里是Little-Endian格式，实际上可以看到是这样的：  
![image](https://github.com/MAR-523/-/blob/main/pic/6.png)  
**01000000**UTXO的索引   
**6a**十六进制形式的解锁脚本的字节数  
**47**将47个字节的数据压入栈中  
**3044022011d906321c6c538a298ae46fe317bba97ad897814ec9102dd001e12628789e8f022042955ad619531432774388fac48e16fc3c99755f18f2003e51de17c45ad9c9e9**签名部分  
**01**SIGHASH_ALL指令  
**21**将21个字节的数据压入栈中  
**037435c194e9b01b3d7f7a2802d6684a3af68d05bbf4ec8f17021980d777691f1d**Big-Endian格式的公钥  
**ffffffff**顺序编号  
**01**交易个数  
**64000000000000**交易数额  
**19**锁定脚本长度  
**76a914df3488394c31e4d82660f9f685e12f8fa22e3dff88ac**锁定脚本  
**00000000**Time Lock  
(如果最后的Time Lock不为0的话那么前面ffffffff处的值小于ffffffff）


