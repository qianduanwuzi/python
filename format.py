# format % 
print('my name is %s' % 'chennan')
print('my name is %s, you can call me %s' % ('chennan', 'wuzi'))

print('%2d-%02d' % (3, 1))
print('%.2f' % 3.1415926)


# 小明的成绩从去年的72分提升到了今年的85分，请计算小明成绩提升的百分点，并用字符串格式化显示出'xx.x%'，只保留小数点后1位：
s2 = 85
s1 = 75
r = (s2-s1)/s1*100
print('%.1f %%' % r)