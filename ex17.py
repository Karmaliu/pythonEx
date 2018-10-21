class MyStuff(object):
    
    def __init__(self):
        # __init__ 实例化对象调用这个函数，对你创建的空对象实现了初始化
        # self 是空对象可以对它进行类似模块，字典等操作，为它设置变量u 
        self.tangerine = "And now a thousand years between"
        
    def apple(self):
        print("I AM CLASSY APPLES!")

thing = MyStuff()
thing.apple()
print(thing.tangerine)