# v2sub
v2ray linux订阅切换脚本

首先，确认你的系统已经安装了python3,centos7由于库比较老，可能需要自行编译安装
食用方法：

``````
git clone https://github.com/xbblog95/v2sub.git;
cd v2sub;
chmod 777 v2sub;
./v2sub;
``````

截图
![avatar](https://i.loli.net/2019/05/13/5cd8d8df5020330894.png)

![avatar](https://i.loli.net/2019/05/13/5cd9071919ba651195.png)

![avatar](https://i.loli.net/2019/05/13/5cd907192b00a64490.png)

新增测速模式
方法：
``````shell
./v2sub speedtest; 
``````

测速模式会轮训订阅中所有节点 （单线程 curl cachefly的测速文件,如需测速更加精确，清将脚本中的testFileUrl后面的数字改成100mb或者更大，同时测速也将更慢，也更耗流量）
测速模式截图
![avatar](https://i.loli.net/2019/05/13/5cd9550ca95ef63725.png)

前面的数字就是序号，重新执行
``./v2sub;``输入对应的序号，即可选择该节点。
