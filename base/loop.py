# for in
arr = ['a', 'b']
for i in arr:
    print(i)

sum = 0
for x in range(101):
    sum = sum + x
print(sum)

# range(0, 5)
print(range(5))
# [0,1,2,3,4]
print(list(range(5)))

# while   break退出循环   continue语句，跳过当前的这次循环，直接开始下一次循环
n = 99
sum = 0
# 计算99之内奇数和
while n > 0:
    sum = sum + n
    n = n -2
print(sum)