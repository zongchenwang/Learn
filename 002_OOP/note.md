class_name.__dict__

class A():       #一类人
    name ="dana" #成员
    age = 18     #成员
A.__dict__
月月 = student() # 归对象所有,月月就是对象

4. 类和对象的成员分析
- 类和对象都可以储存成员,成员可以归类所有,也可以归对象所有
- 类储存成员时使用的是与类关联的一个对象
- 对象要是访问一个成员时,如果对象中没有该成员,尝试访问类中的同名成员,
  如果对象中有此成员,一定访问此成员.
- 创建对象的时候,类中的成员不会放入对象当中,而是得到一个空的对象,没有成员
- 通过对象对类成员重新赋值或者通过对象添加成员时,对应成员会保存在对象中,而不会修改类成员

5. 关于self
- self在对象的方法中表示当前对象本身,如果通过对象调用一个方法,
  那么对象会自动传入到当前方法第一个参数里
# 6.面向对象的三大特征
- 封装
- 继承
- 多态

## 6.1 封装
- 成员变量,成员函数, 有些时候是不允许改变的
- 封装就是对对象的成员进行访问控制
- 封装里面的3个级别
        - 公开,public
        - 受保护的, protected
        - 私有的, private
- public,protected,private 不是关键字
- 只用了思想但是具体实现的时候,比较随和

# 怎么实现protected ?
- 判别对象的位置
    - 对象内部
    - 对象外部
    - 子类中
- 私有
        - 私有成员最高级别封装,只能在当前类或对象中访问
        - 在成员前面添加两个下划线即可
            
                class Person():
                    # name 是共有的成员
                    name = "liuying"
                    # 定义的时候在前面加两个下划线
                    # __age就是私有成员
                    __age = 18
        - python里的私有不是真私有,是一种成为name 命令的改名策略
          那要是想访问,可以使用对象._classname_attributename访问           
        