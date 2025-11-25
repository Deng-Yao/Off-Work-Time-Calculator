
# 下班时间计算器 (Off Work Time Calculator)
在某公司上班摸鱼期间，写了个方便计算下班时间的python程序。*程序使用 tkinter 库实现（Python标准库，无需额外安装），并添加了详细注释。*
## 界面预览：
![alt text](软件预览.png)![alt text](软件预览2.png)![alt text](软件预览3.png)![alt text](软件预览4.png)


### 下班时间核心计算逻辑：
标准工作时长：从 8:30 到 17:45，总时长为9小时15分钟（包含中午1h15分吃饭午休时间）。

早上上班弹性打卡时间：早上 8:30 到 9:30。

**计算规则：**

如果打卡时间在 8:30 或之前，下班时间固定为 17:45；
如果打卡时间在 8:30 到 9:30 之间，下班时间 = 打卡时间 + 9小时15分钟；
如果打卡时间在9:30以后，则迟到。

为了简化处理，我们可以统一将下班时间计算为：打卡时间 + 9小时15分钟，然后与 17:45 取一个较晚的时间。

### *可以根据自己公司的考勤时间在代码相应位置修改*
![alt text](image.png)

### *程序封装*
使用**PyInstaller**将Python程序打包成一个独立的 .exe 文件

`pip install pyinstaller`


在国内通过清华镜像源下载速度可能会更快：`pip install -i https://pypi.tuna.tsinghua.edu.cn/simple pyinstaller`
#### *封装详细步骤*
1. 打开命令提示符(CMD)。

2. 使用 cd 命令切换到你存放脚本的那个文件夹。例如：
`cd D:\Off-Work-Time-Calculator\`

3. 执行打包命令,这里有几个非常有用的参数：

* --onefile 或 -F：将所有内容打包成 一个单独的 .exe 文件。这是最推荐的方式，非常清爽。

* --windowed 或 -w：这是一个 至关重要的参数！因为你的程序是一个GUI应用，这个参数会告诉程序在运行时 不要弹出黑色的命令行窗口。如果不加这个参数，你的计算器后面会一直跟着一个黑框。

* --icon=your_icon.ico 或 -i your_icon.ico：指定程序的图标。

推荐的打包命令 (将下面这行命令复制到你的命令提示符中并执行):

`pyinstaller --onefile --windowed --icon="icon.ico" app.py`

如果你没有准备图标，可以使用这个简化版命令：

`pyinstaller --onefile --windowed app.py`

4. 当命令执行完毕且没有报错时，打包就成功了！
回到你的项目文件夹 (`D:\Off-Work-Time-Calculator\`)，你会发现多了几个新的文件夹和文件：

* `build\`：存放了构建过程中的临时文件，打包成功后可以删除。

* `dist\`：distribution (分发) 的缩写，你的最终成果就在这里！

* `calculator.spec`：一个配置文件，PyInstaller根据它来打包。你可以编辑它进行更高级的定制。

打开 dist 文件夹，你会在里面找到一个名为 `app.exe` 的文件,双击运行!现在，你的“下班时间计算器”已经可以像一个普通的Windows程序一样运行了，并且你可以把它拷贝到任何Windows电脑上使用。

