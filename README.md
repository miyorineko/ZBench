# Zench

又一個Linux VPS測評腳本

## 說明

平時測試VPS的時候一直是靠著 **Bench.sh** 來測試的，最近看到 **Oldking**大佬 的 **SuperBench** 也很方便。我自己把這兩者的腳本結合在一起，然後加入 **Ping** 以及 **路由測試** 功能。比較懶人，簡單快捷。方便VPS測評站的朋友們使用。因為會生成測評報告，可以很方便地分享給其他朋友看自己的測評數據。

範例(Demo)：[https://www.zhujiboke.com/zbench-example.html](https://www.zhujiboke.com/zbench-example.html)

## 腳本命令

如果中文版出現亂碼等情況，請換成英文版。

中文版：

    wget -N --no-check-certificate https://raw.githubusercontent.com/FunctionClub/ZBench/master/ZBench-CN.sh && bash ZBench-CN.sh
    
英文版：

    wget -N --no-check-certificate https://raw.githubusercontent.com/FunctionClub/ZBench/master/ZBench.sh && bash ZBench.sh
    
## 效果圖

![1.png](1.png)


![2.png](2.png)

## 引用

* Bench.sh ( [https://teddysun.com/444.html](https://teddysun.com/444.html) )
* SuperBench ( [https://www.oldking.net/350.html](https://www.oldking.net/350.html) )
* python實現ping程序 ( [https://www.s0nnet.com/archives/python-icmp](https://www.s0nnet.com/archives/python-icmp) )
* Python 設置顏色 ( [http://www.pythoner.com/357.html](http://www.pythoner.com/357.html) )
* Kirito's Blog ( [https://www.ixh.me](https://www.ixh.me) )
