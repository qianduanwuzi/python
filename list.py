
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




