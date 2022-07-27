# 在比特币测试网上发起一笔交易，再对交易原始内容进行解码
首先需要下载[Electrum 工具](https://electrum.org/#download)  
![image](https://github.com/MAR-523/-/blob/main/pic/1.png)  
在之后运行程序获得很多组钱包和私钥，这里选第一组  
![image](https://github.com/MAR-523/-/blob/main/pic/5.png)  
可以通过[水龙头](https://testnet-faucet.mempool.co/) 免费获取测试比特币  
可以在Electrum 工具处看到水龙头交易过来的比特币和对应的交易信息:  
![image](https://github.com/MAR-523/-/blob/main/pic/2.png)  
同时通过[网站BLOCKCYPHER](https://live.blockcypher.com/btc-testnet/)通过txid可以查询交易细节：  
![image](https://github.com/MAR-523/-/blob/main/pic/3.png)  
要求对**交易原始内容**进行分析，因此借助[Socain](https://chain.so/btc)输入txid后进行查询：  
![image](https://github.com/MAR-523/-/blob/main/pic/6.png)  
输出结果：  
```
{  
  "status": "success",  
  "data": {  
    "network": "BTCTEST",  
    "txid": "1cb8d4117ab54b4c71a897cb990eede3ac61853c65d4aa6c330f6faa9e923552",  
    "blockhash": "00000000000000103ee94fbfeabf2991be0046aa852123c84742f921c55b0e9b",  
    "block_no": 2288098,  
    "confirmations": 9,  
    "time": 1658922968,  
    "size": 222,  
    "vsize": 141,  
    "version": 2,  
    "locktime": 2288097,  
    "sent_value": "15.72772084",  
    "fee": "0.00000141",  
    "inputs": [  
      {  
        "input_no": 0,  
        "address": "tb1qafvv7md440wyp4pz99qjpu0yvcue4gf5944766",  
        "value": "15.72772084",  
        "received_from": {  
          "txid": "915349ada1ab6a211e1c588986e2b074d7fcbe3f8467749dd56d69ba29728022",  
          "output_no": 0  
        },  
        "script_asm": "",  
        "script_hex": "",  
        "witness": [  
          "304402202e97e53ba7983624358cda92f491d7c4a876dafff3a844bc3104876a68b8267e02207ac8d18914835874965dd4755f91fb81bf684bc200e2a04859c7add04815e37701",  
          "02321af3166192ad2aa2e89a1b7005760340c2ad1c914ba8adf94dfde7badb9a39"  
        ]  
      }  
    ],  
    "outputs": [  
      {  
        "output_no": 0,  
        "address": "tb1qpkw7ueygg4sghm3zf3n4pmaw9cklfnfdvrrepn",  
        "value": "0.00100000",  
        "type": "witness_v0_keyhash",  
        "req_sigs": null,  
        "spent": null,  
        "script_asm": "0 0d9dee648845608bee224c6750efae2e2df4cd2d",  
        "script_hex": "00140d9dee648845608bee224c6750efae2e2df4cd2d"  
      },  
      {  
        "output_no": 1,  
        "address": "tb1ql6fn2ra0tqjleuruy4zu4yw30hmjw6rcl9qtde",  
        "value": "15.72671943",  
        "type": "witness_v0_keyhash",  
        "req_sigs": null,  
        "spent": {  
          "txid": "169f8193ee70fdd583bd266dfadd09a99fe860f5301d4d9fbc8f4dcb2a21c9a8",  
          "input_no": 0  
        },  
        "script_asm": "0 fe93350faf5825fcf07c2545ca91d17df7276878",  
        "script_hex": "0014fe93350faf5825fcf07c2545ca91d17df7276878"  
      }  
    ],  
    "tx_hex": "0200000000010122807229ba696dd59d7467843fbefcd774b0e28689581c1e216aaba1ad4953910000000000feffffff02a0860100000000001600140d9dee648845608bee224c6750efae2e2df4cd2dc711bd5d00000000160014fe93350faf5825fcf07c2545ca91d17df72768780247304402202e97e53ba7983624358cda92f491d7c4a876dafff3a844bc3104876a68b8267e02207ac8d18914835874965dd4755f91fb81bf684bc200e2a04859c7add04815e377012102321af3166192ad2aa2e89a1b7005760340c2ad1c914ba8adf94dfde7badb9a39e1e92200"
  },  
  "code": 200,  
  "message": ""  
}  
``` 
  
可以看到交易原始数据为**0200000000010122807229ba696dd59d7467843fbefcd774b0e28689581c1e216aaba1ad4953910000000000feffffff02a0860100000000001600140d9dee648845608bee224c6750efae2e2df4cd2dc711bd5d00000000160014fe93350faf5825fcf07c2545ca91d17df72768780247304402202e97e53ba7983624358cda92f491d7c4a876dafff3a844bc3104876a68b8267e02207ac8d18914835874965dd4755f91fb81bf684bc200e2a04859c7add04815e377012102321af3166192ad2aa2e89a1b7005760340c2ad1c914ba8adf94dfde7badb9a39e1e92200**  
