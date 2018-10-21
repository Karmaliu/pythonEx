# 隐式继承

class Parent(object):
    
    def implicit(self):
        print("PARENT implicit()")

class Child(Parent):
    pass

dad = Parent()
son = Child()

dad.implicit()
son.implicit()

# 显示覆盖

class Parent_(object):

    def override(self):
        print("PARENT override()")

class Child_(Parent):

    def override(self):
        print("CHILD override()")

dad_ = Parent_()
son_ = Child_()

dad_.override()
son_.override()

# 在运行前或者运行后替换

class Parent__(object):

    def altered(self):
        print("PARENT altered()")

class Child__(Parent__):

    def altered(self):
        print("CHILD, BEFORE PARENT altered()")
        super(Child__,self).altered()
        print("CHILD, AFTER PARENT altered()")

dad__ = Parent__()
son__ = Child__()

dad__.altered()
son__.altered()
