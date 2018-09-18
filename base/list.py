
# 有序集合 list
list = ['chennan', 'yangping']

# -1表示最后一个元素  -表示倒数第几个
print(list[-1])
print(list[len(list)-1])

print(list[0])
print(list[-2])

# 追加元素
list.append('chena')
print(list)

# 元素插入到指定的位置
list.insert(1, 'Jack')
print(list)

# 要删除指定位置的元素 pop(i)
list.pop(1)
print(list)


# tuple
# 另一种有序列表叫元组：tuple。tuple和list非常类似，但是tuple一旦初始化就不能修改(指向不变)
classmates = ('Michael', 'Bob', 'Tracy')
print(classmates, classmates[0])

# Python在显示只有1个元素的tuple时，也会加一个逗号,，以免你误解成数学计算意义上的括号。
t = (1,)

