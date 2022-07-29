本任务的内容为对于SM3算法进行优化，SM3的实现代码来自于网络，进行了一定的调整与修改。  
![image](https://github.com/MAR-523/-/blob/main/pic/sm3.png)  
这里对于SM3的优化主要是采用了SIMD方式，即单指令多数据集，应用的位置主要是在消息扩展的过程中，因为消息扩展过程里存在指令独立的情况，可以同时运行，因而引入SIMD的相关库函数，可以进行并行的操作。  
![image](https://github.com/MAR-523/-/blob/main/pic/sm33.png)  
这里给出了原始代码和修改后的代码，可以看到使用SIMD可以对于SM3算法的运行进行加速，但效果并不是十分的理想，如果想要得到更好的结果，还需要后续对于算法更加深入的分析。  
以下是修改前和修改后的时间消耗，分别都是在运行100000次的情况下。  
![image](https://github.com/MAR-523/-/blob/main/pic/sm31.png)  
![image](https://github.com/MAR-523/-/blob/main/pic/sm32.png)  
