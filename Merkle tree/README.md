运行指导：以main.cpp作为主文件，余下两个作为函数库文件引入来运行。  
本实验为实现一个merkle tree，同时对于在其中和不在其中的点进行查询。  
merkle tree的主要原理为设置叶节点作为需要验证的消息，每个父节点为左右两个子节点哈希值并起来后计算的新的哈希值，直到得到根节点，才成功构造出一个merkle tree。  
具体的代码已经给出，以下需要验证三个问题：  
1.构造一棵有10k个叶节点的merkle tree
2.验证一个在其中的节点。  
3.验证一个不在其中的节点。  
以下为调用代码部分，这里使用的sha256函数来自网络。  
![image](https://github.com/MAR-523/-/blob/main/pic/merkle2.png)  
以下为运行结果，可以看到这个树为17层（不算最低一层叶节点的话），同时也通过了对于消息内容是否在其中的验证。  
![image](https://github.com/MAR-523/-/blob/main/pic/merkle1.png)  
