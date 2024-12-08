# 60s-send
基于python实现自动每日定时推送60s新闻

# 部署教程


首先，登录[WXPusher](https://wxpusher.zjiecode.com/)
,创建一个应用

![image](https://github.com/user-attachments/assets/fba25576-2022-4ed3-b205-a64d86802c1b)


创建后注意保存好apptoken，这个token只会出现一次，如果忘记了要去应用管理->appToken 里重置。

之后，可以到这里获取到关注链接，用于分享给别人。

![image](https://github.com/user-attachments/assets/f320abe5-da5b-422d-ae33-32fe35a65cbd)


把刚才获取的appToken写到代码开头的appToken里边

再将源码放在一些定时任务平台即可，云函数、青龙面板等等。

这里以青龙面板为例，点进脚本管理.

![image](https://github.com/user-attachments/assets/6f4f5e47-10cd-4ed9-aed6-4a56bf90898a)


点击右上角的+号添加脚本。

![image](https://github.com/user-attachments/assets/f2b258f9-fbe3-47df-8540-5e93a4923102)


这里可以选择本地脚本，把上边的源码下载解压之后直接拖进去就行。

![image](https://github.com/user-attachments/assets/335cbc4c-aebc-4396-9ab3-4c5a4549624c)


然后，去这里添加定时任务即可。

![image](https://github.com/user-attachments/assets/a5f1280c-9514-4a7e-b0ab-40ed6fd397bd)


![image](https://github.com/user-attachments/assets/7d46e2b7-2395-48fc-aa8f-e7b73d52517a)


具体内容这样写就可以

![image](https://github.com/user-attachments/assets/5a04bb9a-5adf-4db4-af6d-ddad93b8ed3a)



```
task 60s.py

corn: 00 08 * * *
//每天早上八点运行
```

接下来去这里，添加环境变量，名称为：ddd_dt

![image](https://github.com/user-attachments/assets/33e92e93-2d4f-4a98-8b0e-2b44d5372a0f)


![image](https://github.com/user-attachments/assets/da463632-a5db-4591-801c-ef28343370c1)


![image](https://github.com/user-attachments/assets/1cf94cee-6193-4335-99f5-18669e9dae5c)


内容格式为：uid1#用户名1@uid2#用户名2

用户名会在这里显示。


![image](https://github.com/user-attachments/assets/bbb2ffd6-d911-451a-a046-015197dcd1d5)

用户的uid可以在别人关注你之后，去wxpusher中看到。


![image](https://github.com/user-attachments/assets/6f6e4412-6671-4bc6-adf6-3d9dd13a3a71)



<!--more-->
感谢：[60s接口支持](https://api.03c3.cn/)
