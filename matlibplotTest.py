##import matplotlib.pyplot as plt
##import random
### 保证生成的图片在浏览器内显示
###%matplotlib inline
### 保证能正常显示中文(Mac)
##plt.rcParams['font.family'] = ['Arial Unicode MS']
##
### 模拟海南一天的温度变化
##
### 生成x轴的24小时
##hainan_x = [h for h in range(0, 24)]
##
### 生成y轴的温度随机值(15, 25)
##hainan_y = [25,30,45,25,30,45,25,30,45,25,30,45,25,30,45,25,30,45,25,30,45,25,30,45]
##
### 设置画板属性
##plt.figure(figsize = (10, 8), dpi = 100)
##
### 往画板绘图
##plt.plot(hainan_x, hainan_y, label="海南")
##
### 模拟北京一天内温度的变化
##
### 生成x轴的24小时
##beijing_x = [h for h in range(0, 24)]
##
### 生成y轴的温度随机值(5, 10)
##beijing_y = [random.randint(5, 10) for t in range(0, 24)]
##
### 往画板绘图
##plt.plot(beijing_x, beijing_y, label="北京")
##
##
### 模拟河北一天内温度的变化
##hebei_x = beijing_x
##hebei_y = [random.randint(1, 5) for t in range(0, 24)]
### 自定义绘制属性: 颜色color="#0c8ac5", linestyle"-"""--""-.":", 线宽linewidth, 透明度alpha
##plt.plot(hebei_x, hebei_y, label="河北",color="#823384", linestyle=":", linewidth=3, alpha=0.3)
##
##
### 坐标轴显示设置
##
##
##
### 生成24小时的描述
##x_ = [x_ for x_ in range(0, 24)]
##x_desc = ["{}时".format(x_desc) for x_desc in x_]
##
### 设置x轴显示 24小时
##plt.xticks(x_, x_desc)
##
### 生成10至30度的描述
##y_ = [y_ for y_ in range(0, 30)][::2]
##y_desc = ["{}℃".format(y_desc) for y_desc in y_]
##
##
### 设置y轴显示温度描述
##plt.yticks(y_, y_desc)
##
### 指定x y轴的名称
##plt.xlabel("时间")
##plt.ylabel("温度")
##
### 指定标题
##plt.title("一天内温度的变化")
##
### 显示图例
##plt.legend(loc="best")
## 
### 将数据生成图片, 保存到当前目录下
##plt.savefig("./t.png")
### 在浏览器内展示图片
##plt.show()




import numpy as np
import matplotlib.pyplot as plt
import xlrd
pm = xlrd.open_workbook("pm.xlsx")
sheet2_name = pm.sheet_names()[1]
sheet1 = pm.sheet_by_name('31')
sheet2 = pm.sheet_by_name('32')
sheet3 = pm.sheet_by_name('33')






rows = sheet2.row_values(4,6)
cols = sheet1.col_values(8,19)
cols2 = sheet2.col_values(8,4)
cols3 = sheet3.col_values(8,4)


cols.extend(cols2)
cols.extend(cols3)





##sheet2.cell(4,5).value.encode('utf-8')
##sheet2.cell_value(1,0).encode('utf-8')
##sheet2.row(1)[0].value.encode('utf-8')


count = len(cols)
print(count)
data = [float(i) for i in cols]
##print(data)
# 数据的直方图
plt.figure()
plt.subplot(2,1,1)
plt.hist(data,bins=84,facecolor='g',edgecolor='b',histtype='bar')

plt.xlabel('Grade')
plt.ylabel('Numbers of students')
#添加标题
plt.title('Paper Test ')
t= " Institute of Automation"
plt.text(72, 4.5, t,size=15,style='oblique', ha='center',va='top',wrap=True)

plt.grid(True)



sheetc1 = pm.sheet_by_name('23')
sheetc2 = pm.sheet_by_name('24')
sheetc3 = pm.sheet_by_name('25')
sheetc4 = pm.sheet_by_name('26')
sheetc5 = pm.sheet_by_name('27')
sheetc6 = pm.sheet_by_name('28')
sheetc7 = pm.sheet_by_name('29')
sheetc8 = pm.sheet_by_name('30')



cols = sheetc1.col_values(8,8)
cols2 = sheetc2.col_values(8,4)
cols3 = sheetc3.col_values(8,4)
cols4 = sheetc4.col_values(8,4)
cols5 = sheetc5.col_values(8,4)
cols6 = sheetc6.col_values(8,4)
cols7 = sheetc7.col_values(8,4)
cols8 = sheetc8.col_values(8,4)


cols.extend(cols2)
cols.extend(cols3)
cols.extend(cols4)
cols.extend(cols5)
cols.extend(cols6)
cols.extend(cols7)
cols.extend(cols8)

count = len(cols)
print(count)
data2 = [float(i) for i in cols]
##print(data)
##plt.figure()
plt.subplot(2,1,2)
# 数据的直方图
plt.hist(data2,bins=172,facecolor='r',edgecolor='b',histtype='bar')

plt.xlabel('Grade')
plt.ylabel('Numbers of students')
#添加标题

t= " Institute of Computer"
plt.text(85, 7, t,size=15,style='oblique', ha='center',va='top',wrap=True)
plt.annotate('me', xy=(137, 1), xytext=(138, -1),arrowprops=dict(width=0.5,facecolor='black', shrink=0.05))
plt.grid(True)

plt.show()


