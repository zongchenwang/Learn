1. 面向对象概述(Object Oriented, OO)
- 类和对象的概念
    - 类里面就包含两个主要东西"变量,函数"
    - 类: 抽象名词, 代表一个集合,共性的事物(一群学生)
    - 对象: 具体的事物,单个个体(一个学生)
        - 一个抽象,代表一大群事物
        - 一个个体,代表一类事物的摸一个个体
- 类中的内容,应该具有两个内容
    - 表明事物特征的,叫属性(变量)
        - 姓名,家庭地址,etc.....叫属性
    - 表明事物功能或动作,(称为函数)
2. 类的基本实现
- 类的命名
    - 遵守变量命名的规范
    - 大驼峰(由多个单词构成,每个单词首字母大写,单词和单词之间相连)
    - 尽量避开系统命名相似的命名
- 你如何声明一个类
    - 必须用class关键字
    - 类由属性和方法(for循环在这里用)构成,其他不允许出现
    - 成员属性定义可以直接使用变量赋值,如果没有纸,允许使用None
    - 案例 01.py
- 实例化类
            
           变量 = 类名() #实例化了一个对象
- 访问对象成员
   - 使用点操作符
                    
                 obj.成员属性名称
                 obj.成员方法
- 可以通过默认设置变量检查类和对象多有成员
    - 对象所有成员检查
    
            # dict前后各有两个下划线
            obj.__dict__
    - 类所有的成员
            # dict前后各有两个下划线
            class_name.__dict__
    想
 
 
 
 3. anaconda基本使用
 - anaconda 主要是一个虚拟环境管理器
 - 还是一个安装包管理器
 - conda list: 显示anaconda安装的包
 