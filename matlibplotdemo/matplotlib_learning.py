import matplotlib.pyplot as plt
import matplotlib.font_manager as ftm
import random

#使字体支持汉字
my_font = ftm.FontProperties(fname="/System/Library/Fonts/PingFang.ttc")

### 绘制折线图
x = range(60)
y_cd = [random.randint(10,28) for i in range(60)]
y_pa = [random.randint(10,32) for i in range(60)]

## 设置图片大小
plt.figure(figsize=(20,8), dpi=80)

## 绘图
plt.plot(x, y_cd, label='成都', color="cyan", linestyle='--')
plt.plot(x, y_pa, label='巴黎', color="orange", linestyle="-.")

## 设置x轴的刻度
_xtick_labels = ["9时{}分".format(i) for i in range(30, 59)]
_xtick_labels += ["10时{}分".format(i) for i in range(0, 30)]
# 取步长
plt.xticks(list(x)[::3], _xtick_labels[::3], rotation=45, fontproperties=my_font)

## 添加描述信息
plt.xlabel("时间", fontproperties=my_font)
plt.ylabel("温度 单位(摄氏度)", fontproperties=my_font)
plt.title("成都与巴黎9点30分到10点30分的温度变化情况", fontproperties=my_font)

## 添加图例
plt.legend(prop=my_font,loc='upper right')

## 绘制网格
plt.grid(alpha=0.4, linestyle=":")

## 保存
#plt.savefig("./figure.png")

## 显示
plt.show()




### 绘制散点图
day_3 = range(1,32)
day_10 = range(41, 72)
ht_3 = [10, 12, 15, 11, 12, 13, 8, 9, 9, 14, 15, 16, 15, 20, 21, 21, 22, 21, 24, 27, 18, 20, 23, 22, 25, 21, 19, 18, 21, 25, 24]
ht_10 = [27, 22, 22, 25, 21, 22, 21, 24, 23, 17, 18, 13, 14, 14, 15, 16, 20, 21, 17, 16, 16, 15, 16, 16, 15, 15, 19, 17, 19, 16, 14]

plt.figure(figsize=(20, 8), dpi=80)

plt.scatter(day_3, ht_3, label="3月")
plt.scatter(day_10, ht_10, label="10月")

_x = list(day_3) + list(day_10)
_xtick_ht_labels = ["3月{}日".format(i) for i in day_3]
_xtick_ht_labels += ["10月{}日".format(i-40) for i in day_10]
plt.xticks(_x[::2], _xtick_ht_labels[::2], rotation=45, fontproperties=my_font)

plt.xlabel("日期", fontproperties=my_font)
plt.ylabel("当日最高温度", fontproperties=my_font)
plt.title("成都3月与10月当日最高温度", fontproperties=my_font)

plt.legend(prop=my_font)

plt.grid(alpha=0.5)

plt.show()


### 绘制条形图
a = ["阿里巴巴", "腾讯", "美团", "京东", "拼多多", "百度", "网易", "腾讯音乐娱乐", "爱奇艺", "新浪微博"]
b = [5690, 4608, 760, 514, 440, 438, 392, 192, 153, 104]

plt.figure(figsize=(20,8), dpi=80)

plt.bar(range(len(a)), b, width=0.4)

plt.xticks(range(len(a)), a, fontproperties=my_font)

plt.xlabel("公司", fontproperties=my_font)
plt.ylabel("市值 单位：亿美元", fontproperties=my_font)
plt.title("2019中国互联网公司市值排名 数据来源：网易新闻", fontproperties=my_font)

plt.grid(alpha=0.1, linestyle=":")

plt.show()

### 绘制横的条形图
plt.figure(figsize=(20,8), dpi=80)

plt.barh(range(len(a)), b, height=0.3, color='orange')

plt.yticks(range(len(a)), a, fontproperties=my_font)

plt.ylabel("公司", fontproperties=my_font)
plt.xlabel("市值 单位：亿美元", fontproperties=my_font)
plt.title("2019中国互联网公司市值排名 数据来源：网易新闻", fontproperties=my_font)

plt.grid(alpha=0.1, linestyle=":")

plt.show()

### 绘制多个条形图
movie = ["囧妈", "姜子牙", "唐人街探案"]
income_14 = [14323, 8009, 10010]
income_15 = [10021, 10162, 12100]
income_16 = [9742, 13210, 11892]

plt.figure(figsize=(20,8), dpi=80)

interval = 0.3
x_14 = list(range(len(movie)))
x_15 = [i+interval for i in x_14]
x_16 = [i+interval*2 for i in x_14]

plt.bar(x_14, income_14, width=0.3, label="1月14日")
plt.bar(x_15, income_15, width=0.3, label="1月15日")
plt.bar(x_16, income_16, width=0.3, label="1月16日")

plt.xticks(x_15, movie, fontproperties=my_font)

plt.xlabel("电影", fontproperties=my_font)
plt.ylabel("票房收入， 单位：万元", fontproperties=my_font)
plt.title("2020年1月14日至1月16日各电影票房收入", fontproperties=my_font)

plt.legend(prop=my_font)

plt.show()


### 绘制直方图
term = [140, 135, 145, 106, 135, 122, 126, 142, 112, 78, 105, 140, 145, 137, 137, 109, 129, 129, 139, 131, 135, 139, 105, 130, 127,
        127, 139, 139, 134, 123, 101, 137, 120, 135, 116, 138, 100, 120, 141, 114, 128, 135, 130, 142, 117, 108, 115, 110, 107, 120,
        100, 111, 104, 124, 124, 105, 114, 103, 117, 121, 125, 116, 144, 130, 117, 124, 124, 98, 111, 101, 132, 119, 115, 122, 104,
        108, 110, 144, 104, 141, 134, 139, 125, 110, 112, 120, 110, 121, 103, 144, 135, 104, 144, 102, 112, 111, 125, 122, 125, 128,
        132, 132, 132, 107, 143, 74, 142, 124, 115, 128, 112, 110, 124, 132, 118, 121, 121, 128, 116, 142, 140, 126, 117, 124, 106,
        126, 101, 145, 125, 121, 139, 103, 106, 110, 120, 104, 102, 124, 136, 140, 133, 143, 142, 110, 137, 121, 129, 117, 101, 124,
        104, 123, 135, 104, 107, 142, 108, 139, 129, 89, 122, 124, 128, 103, 133, 145, 120, 106, 145, 102, 127, 127, 138, 100, 136,
        103, 102, 140, 113, 110, 111, 131, 128, 126, 117, 104, 136, 101, 119, 100, 122, 110, 124, 145, 111, 114, 141, 139, 133, 115,
        131, 105, 141, 141, 98, 144, 129, 121, 124, 111, 101, 138, 112, 144, 124, 123, 107, 138, 100, 139, 102, 123, 106, 119, 128,
        141, 109, 142, 116, 132, 118, 133, 112, 113, 143, 105, 110, 132, 70, 116, 110, 111, 132, 128, 105, 108, 145, 132, 121, 107]


## 计算组数
dist = 5  #组距
num_bins = (max(term)-min(term))//dist + 1

plt.figure(figsize=(20,8), dpi=80)

plt.subplot(2,1,1)
plt.hist(term, num_bins)
plt.xticks(range(min(term), max(term)+dist, dist))
plt.title("频数分布直方图", fontproperties=my_font)
plt.grid(alpha=0.6)

plt.subplot(2,1,2)
plt.hist(term, num_bins, density=True)
plt.xticks(range(min(term), max(term)+dist, dist))
plt.title("频率分布直方图", fontproperties=my_font)
plt.grid(alpha=0.6)

plt.show()