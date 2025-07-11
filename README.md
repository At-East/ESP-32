# ESP-32 
## 简介
这个库包含了我在开发（实际上是玩）ESP-32时的方法以及编写的一些代码，包括
> 入门指南
> 实用程序
> 我的闲言碎语（）

***

当然，相应的链接也放在下面
> ESP-32购买链接：[text(https://e.tb.cn/h.hSwNhoIrf0Ygtvl?tk=lhdv4bTkY5r)]
> 参考的bilibili课程：[text(https://www.bilibili.com/video/BV1G34y1E7tE)]

***

## 入门指南

拿到ESP-32之后我们建议您下载thonny，并安装相应的驱动程序（这些程序在本库中的“drivers”文件夹中），安装Thonny的方法我们不再讲述，我们在此讲述如何安装驱动程序。

> 注意：无论是驱动程序还是Thonny，均不要安装在含有中文文件名的文件路径中！！！

驱动程序文件名是“ESP-32Driver.zip”，解压缩后找到“SETUP.EXE”打开并运行，然后点击“安装”
**注意：只有显示“驱动安装成功”才是安装完成，否则安装失败**

驱动安装成功后，可打开电脑设备管理器，点击“端口”看看有没有ESP-32设备（设备管理器的名称是CH340），并且还有相应的端口名称，比如COM X（X是1-N的正整数）
此后我们打开thonny，打开图片中的内容
![picture1](/readme/img/ "Picrure1.png")
并点击“configure interpreter”，选择自己开发板对应的端口，如图所示
![picture2](/readme/img/ "Picrure2.png")
这时返回主页，下方的“Shell”可能会报错，这是为什么呢？这是因为我们没有注入boot组件（，不过没关系，在上方“object”文件夹中找到“boot.py”文件，用thonny打开，并点击“运行”，这时组件注入完成，没有报错了，如下所示
![picture3](/readme/img/ "Picrure3.png")
 
***

## 实用程序

这一部分包含在文件夹“object”内，请您自己探索（
~~ 我不会告诉你我实际上也不怎么会 ~~ 不过我会慢慢更新的，相信我（）

## 我的闲言碎语
（待更新——2025.07.11，Bilibili World 2025 的第一天）