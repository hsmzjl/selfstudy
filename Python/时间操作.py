# 引入模块
import time, datetime


# 2.1 str类型的日期转换为时间戳
# 字符类型的时间
tss1 = '2013-10-10 23:40:00'
# 转为时间数组
timeArray = time.strptime(tss1, "%Y-%m-%d %H:%M:%S")
print timeArray
# timeArray可以调用tm_year等
print timeArray.tm_year   # 2013
# 转为时间戳
timeStamp = int(time.mktime(timeArray))
print timeStamp  # 1381419600


# 结果如下
time.struct_time(tm_year=2013, tm_mon=10, tm_mday=10, tm_hour=23, tm_min=40, tm_sec=0, tm_wday=3, tm_yday=283, tm_isdst=-1)
2013
1381419600


# 2.2 更改str类型日期的显示格式
tss2 = "2013-10-10 23:40:00"
# 转为数组
timeArray = time.strptime(tss2, "%Y-%m-%d %H:%M:%S")
# 转为其它显示格式
otherStyleTime = time.strftime("%Y/%m/%d %H:%M:%S", timeArray)
print otherStyleTime  # 2013/10/10 23:40:00

tss3 = "2013/10/10 23:40:00"
timeArray = time.strptime(tss3, "%Y/%m/%d %H:%M:%S")
otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
print otherStyleTime  # 2013-10-10 23:40:00


# 2.3 时间戳转换为指定格式的日期
# 使用time
timeStamp = 1381419600
timeArray = time.localtime(timeStamp)
otherStyleTime = time.strftime("%Y--%m--%d %H:%M:%S", timeArray)
print(otherStyleTime)   # 2013--10--10 23:40:00
# 使用datetime
timeStamp = 1381419600
dateArray = datetime.datetime.fromtimestamp(timeStamp)
otherStyleTime = dateArray.strftime("%Y--%m--%d %H:%M:%S")
print(otherStyleTime)   # 2013--10--10 23:40:00
# 使用datetime，指定utc时间，相差8小时
timeStamp = 1381419600
dateArray = datetime.datetime.utcfromtimestamp(timeStamp)
otherStyleTime = dateArray.strftime("%Y--%m--%d %H:%M:%S")
print(otherStyleTime)   # 2013--10--10 15:40:00


# 2.4 获取当前时间并且用指定格式显示
# time获取当前时间戳
now = int(time.time())     # 1533952277
timeArray = time.localtime(now)
print timeArray
otherStyleTime = time.strftime("%Y--%m--%d %H:%M:%S", timeArray)
print otherStyleTime

# 结果如下
time.struct_time(tm_year=2018, tm_mon=8, tm_mday=11, tm_hour=9, tm_min=51, tm_sec=17, tm_wday=5, tm_yday=223, tm_isdst=0)
2018--08--11 09:51:17


# datetime获取当前时间，数组格式
now = datetime.datetime.now()
print now
otherStyleTime = now.strftime("%Y--%m--%d %H:%M:%S")
print otherStyleTime

# 结果如下：
2018-08-11 09:51:17.362986
2018--08--11 09:51:17


