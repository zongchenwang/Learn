
'''
定义一个学生类,用来形容学生
'''

class Student():
    # 一个空类,pass 代表直接跳过
    # 此处pass必须有
    pass
# 定义一个对象
mingyue = Student()

# 在定义一个类,用来描述听Python的学生类
class PythonStuden():
    # 用 None 站位
    name = None
    age = 18
    course = "Python"
    #需要注意
    #1. def doHomework的缩进层级
    #2. 系统默认由一个self参数
    def do_HW(self):
        print("我在做作业")
        # 推荐写法在函数末尾return 语句
        return None

# 实例化一个叫yueyue的学生,是一个具体的人
yueyue = PythonStuden()
print(yueyue.name)
print(yueyue.age)
# 需要注意的是成员函数调用没有递进参数
yueyue.do_HW()
12