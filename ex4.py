formatter ="{} {} {} {}" 

# 定义变量formatter ，

print(formatter.format(1, 2, 3, 4))

# 取第一行定义的formatter字符串。
# 调用他的format函数， 这相当于告诉它执行一个叫format的命令行命令。
# 给format传递4个参数， 这些参数和formatter变量中的{}匹配，相当于将参数传递给了format这个命令。
# 在formater 上调用format的结果是一个新字符串，其中的{}被4个变量替换掉了，这就是print现在打印的结果。

print(formatter.format("one", "two", "three", "four"))
print(formatter.format(True, False, False, True))
print(formatter.format(
    "Try your",
    "Own tet here",
    "Maybe a poem",
    "Or a song about fear"
))