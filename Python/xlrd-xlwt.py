import xlrd
import xlwt
from xlrd import xldate_as_tuple
import time
from tkinter import filedialog

# excel的读写操作


# 对话框打开文件并获取文件名
def openfile():
    # 对话框打开文件并获取文件名
    return filedialog.askopenfilename(title=u'选择文件')


# 对话框打开文件并保存文件
def savefile():
    # 对话框打开文件并编辑自己想要保存的文件名
    return filedialog.asksaveasfilename(title='保存文件', defaultextension='.xls')


#  1、常用单元格中的数据类型
#  0. empty（空的）,1 string（text）, 2 number, 3 date, 4 boolean, 5 error， 6 blank（空白表格）
#
# 打开Excel文件到工作簿
workbook = xlrd.open_workbook(openfile())
# 通过索引打开工作表
sheet = workbook.sheet_by_index(0)
sheet1 = workbook.sheets()[0]
# 通过工作表名打开工作表
sheet2 = workbook.sheet_by_name('Sheet1')
# 返回book中所有工作表的名字
names = workbook.sheet_names()

# 行的操作
nrows = sheet.nrows  # 获取该sheet中的有效行数

rowx = nrows - 1
sheet.row(rowx)  # 返回由该行中所有的单元格对象组成的列表

sheet.row_slice(rowx)  # 返回由该列中所有的单元格对象组成的列表

sheet.row_types(rowx, start_colx=0, end_colx=None)  # 返回由该行中所有单元格的数据类型组成的列表

sheet.row_values(rowx, start_colx=0, end_colx=None)  # 返回由该行中所有单元格的数据组成的列表

sheet.row_len(rowx)  # 返回该列的有效单元格长度

# 列的操作
ncols = sheet.ncols  # 获取列表的有效列数
colx = ncols - 1
sheet.col(colx, start_rowx=0, end_rowx=None)  # 返回由该列中所有的单元格对象组成的列表

sheet.col_slice(colx, start_rowx=0, end_rowx=None)  # 返回由该列中所有的单元格对象组成的列表

sheet.col_types(colx, start_rowx=0, end_rowx=None)  # 返回由该列中所有单元格的数据类型组成的列表

sheet.col_values(colx, start_rowx=0, end_rowx=None)  # 返回由该列中所有单元格的数据组成的列表

# 单元格操作
cell = sheet.cell(rowx, colx)
# 返回单元格对象

sheet.cell_type(rowx, colx)  # 返回单元格中的数据类型

sheet.cell_value(rowx, colx)  # 返回单元格中的数据


def cellvaluetostr(cell):
    '''获取单元格文本（去掉前后空格,
    日期格式输出YYYY-MM-DD,
    参数：Excel单元格对象）'''
    thiscell = cell
    if thiscell.ctype == 0:  # 空
        return ''
    elif thiscell.ctype == 1:  # 文本
        thiscell.value = thiscell.value.strip()
    elif thiscell.ctype == 2 and thiscell.value % 1 == 0.0:  # 整数
        thiscell.value = int(thiscell.value)
        thiscell.value = str(thiscell.value)
    elif thiscell.ctype == 2 and thiscell.value % 1 != 0.0:  # 浮点
        thiscell.value = str(thiscell.value)
    elif thiscell.ctype == 3:  # 日期型
        # print(thiscell.value)
        date = xldate_as_tuple(thiscell.value, 0)
        # print(date)
        thiscell.value = str(date[0]) + '-' + str(date[1]) + '-' + str(date[2])

        # print(thiscell.value)
        return thiscell.value

    elif thiscell.ctype == 4:  #
        return str(thiscell.value)
    return thiscell.value


DATEFORMAT = {"%Y-%m-%d", "%Y.%m.%d", "%Y%m%d", "%Y/%m/%d", "%Y-%m"}


def changedateformat(strdate):
    '''#文本日期转换到固定格式：
    成功：返回YYYY-MM-DD
    失败:返回 空字符串'''
    thisstrdate = strdate
    fanhui = ''
    for i in DATEFORMAT:
        try:
            timeArray = time.strptime(thisstrdate, i)
            fanhui = str(time.strftime("%Y-%m-%d", timeArray))
        except:
            pass
    return fanhui


# -----------------------------------xlwt--------------------------------------

# 创建一个workbook 设置编码
workbook = xlwt.Workbook(encoding='utf-8')
# 创建一个worksheet  参数 cell_overwrite_ok=True 表示写入可覆盖（可选参数）
sheet = workbook.add_sheet('sheet1', cell_overwrite_ok=True)

# 生成样式
style = xlwt.XFStyle()  # 初始化样式
font = xlwt.Font()  # 为样式创建字体
font.name = 'Times New Roman'
font.bold = True  # 黑体
font.underline = True  # 下划线
font.italic = True  # 斜体字
font.colour_index = 4  # 设置字体颜色 颜色取值范围是0-71
font.height = 720
style.font = font  # 设定样式

alignment = xlwt.Alignment()
alignment.horz = 2  # 设置水平位置，1是左对齐，2是居中，3是右对齐
# 设置自动换行
alignment.wrap = 1  # 0 不自动换行 , 1 自动换行
style.alignment = alignment

# 添加边框
borders = xlwt.Borders()
borders.left = 1
borders.right = 1
borders.top = 1
borders.bottom = 1
borders.bottom_colour=0x3A    
style.borders = borders



# 设置单元格格式
# xlwt 中设置单元格样式主要是通过 XFStyle 这个类来完成的，XFStyle 类中属性与单元格属性的对应关系如下：

XFStyle属性名	对应单元格属性	值类型
num_format_str	数字	        str
font	        字体	        Font类实例
alignment	    对齐	        Alignment类实例
borders	        边框	        Borders类实例
pattern	        填充	        Pattern类实例
protection	    保护	        Protection类实例

# 在num_format_str数据性中设置EXCEL自定义格式即可设置单元格格式为文本类型

# 设置单元格格式为文本
style1 = xlwt.XFStyle()  # 设置单元格格式为文本
style1.num_format_str = '@'   # 设置单元格格式为文本
for i in range(0, 500):
    for j in range(0, 30):
        sheet1.write(i, j, style=style1)



# 写入excel
# 参数对应 行, 列, 值
# 不带样式写入数据
sheet.write(1, 0, '要写入的数据')
# 带样式写入数据
sheet.write(5, 0, '要写入的数据', style)
# 写入超链接
sheet.write(4, 4, xlwt.Formula('HYPERLINK("http://www.google.com";"Google")'))

# 设置列宽
# 如下代码表示设置第0列20倍字符宽度
sheet.col(0).width = 256 * 20

# 设置行高
# xlwt 不能直接设置行高，但是可以通过设置字体来改变行高
# 如下代码表示第0行设置'font:height 720;'字体高度
sheet.row(0).set_style(xlwt.easyxf('font:height 720;'))

# 合并单元格
# 合并第1行到第2行的第0列到第3列 并按样式“style”写入数据到单元格。
worksheet.write_merge(1, 2, 0, 3, '要写入的数据', style)

# 保存
workbook.save(savefile())
