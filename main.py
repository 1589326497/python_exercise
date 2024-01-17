import math  # 模块引用
from statistics import median, mean  # 只引入这个模块里的median,mean两个函数
from statistics import *  # 将模块中所有函数全部引用 有点象 using namespace std

print(mean([13, 45, 21]))  # 不需要带上模块的名字
print(median([13, 45, 21]))

# 1 ----------空值类型 None 字符串 str 整数 int 浮点型 float 布尔 bool
b1 = False
b2 = True
print(math.log2(10))

n = None
# 2 ----------type 返回变量类型
print(type(n))
print(type(b2))
is_at_home = True
# 3 ---------- input("这是提示消息") 输入
user_age = 60
print(user_age)

# 4 ----------if判断
if user_age > 60:
    print("指令正确")
elif user_age == 60:
    print("考虑一下")
else:
    if not is_at_home:
        print("指令正确")
    else:
        print("指令错误")

# 5 ---------逻辑运算 and or not

# 6 ---------链表 python的链表可以放不同的类型
list1 = [1, 23, 45, 56, "he he", 23.6]
list2 = [1, 5, 6, 2, 3, 78, 1, 67]
list1.insert(2, 21)
list1.append(23)
list1.remove(56)  # 将56移除
print(53 // 2)  # 除完后向下取整
print(list1)
print(list1[4])
print(sorted(list2))
print(sum(list2))  # 求和
print("最大值" + ":", max(list2))
print(min(list2))
print(len(list1))  # len和c中的string()类似

# 7 ----------元组 元组不可变
pair = ()

# 8 ----------字典 key value
dictionary = {1: "a",
              2: "b",
              3: "c"}
dictionary[4] = "d"  # 向字典中加入对组

key = 1
print("当前字典收录的元素个数：" + str(len(dictionary)))
if key in dictionary:
    print("找到了:", dictionary[key])
else:
    print("没有找到")

# 9-----------for循环
for key in dictionary.items():  # 返回对组
    print(key)

for i in range(1, 100):  # 遍历1到99
    print(i)

# 10-----------while循环
print("_____________")
list3 = [12, 34, 56, 3, 21, 5, 6, 87]
list3.sort()
i = 0
size = 0
result = 0
while i < len(list3):
    print(list3[i])
    size += list3[i]
    i += 1  # python里不能i++这种写法
if size == 0:  # 0不能作为被除数和除数
    result = 0
else:
    result = size / len(list3)
print("平均值为：", result)

# 11----------- format 格式函数
print("""
    圆周率是：{pi}
    这个数字为：{num}
""".format(pi=3.1415926, num=23))


# 12 ----------函数
def calculate():
    # 接下来是一些定义函数的代码
    a = 9
    return a  # 不写return默认返回vale


print(calculate())


# 13 ----------面向对象编程
class CuteCat:
    def __init__(self, cat_name, cat_age):  # 初始化函数 有点像c++里的构造函数 用来定义属性
        self.name = cat_name  # 加self.编译器会把name看作类的属性，不加就是普通的赋值
        self.age = cat_age

    def speak(self):
        print("喵" * self.age)


cat1 = CuteCat('Lambtn', 2)  # 创建对象用=，对象名后加（）这点与c不同
print(f"小猫的名字:{cat1.name}小猫的年龄:{cat1.age}")  # 加f可以把{ }转出来

CuteCat1 = CuteCat  # 如果不加（）就变成了对类的别名引用
cat2 = CuteCat1('jojo', 4)
print(f"小猫的名字:{cat2.name}小猫的年龄:{cat2.age}")
cat2.speak()


# 14 ----------类继承
class Employee:  # 员工基类
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def print_id(self):
        print(f"员工名字：{self.name},工号:{self.id}")


class FullTimeEmployee(Employee):  # 正式员工
    def __init__(self, name, id, salary):
        super().__init__(name, id)
        self.salary = salary

    def calculate_monthly_pay(self):
        return self.salary


class partTimeEmployee(Employee):  # 日结员工
    def __init__(self, name, id, day_salary, work_days):
        super().__init__(name, id)
        self.day_salary = day_salary
        self.work_days = work_days

    def calculate_monthly_pay(self):
        return self.day_salary * self.work_days


zhangshan = FullTimeEmployee("张三", "1001", 6000)
lisi = partTimeEmployee("李四", "1002", 230, 15)
zhangshan.print_id()
print(zhangshan.calculate_monthly_pay())

# 15 ----------文件操作
# r 只读模式 w写入模式 encoding为编码格式 默认为系统默认的模式

# 读文件
f = open("file/text.txt", 'r', encoding="utf-8")
print(f.read())  # 用read方法读取全部内容
print(f.readline())  # 读一行
lines = f.readlines()  # 把每行内容存储到列表里
for line in lines:
    print(line)

f.close()  # 关闭文件

with open("file/text01.txt", 'r', encoding="utf-8") as f:
    print(f.readline())

# 写文件 如果文件里有内容 用w会先清空文件 如果是附件内容 用a
# with open("file/text02.txt", 'w',encoding="utf-8") as f:
#     f.write("hello")
with open("file/text02.txt", 'r+', encoding="utf-8") as f:  # 用r+模式不光可以读也可以写
    f.write("hello world")
    print(f.readline())

# 16 ----------捕捉异常
try:
    # 可能产生错误的代码
    height = input("输入您的身高")
except ValueError:
    print("输入不为合格数字，请重新运行程序")
except:
    print("发生了未知错误")
else:
    print("程序正常执行:", height)
finally:
    print("程序结束运行")

# 17 ----------测试 断言
assert 1 + 2 < 6


# Traceback (most recent call last):
#   File "D:\python test\python练习\main.py", line 194, in <module>
#     assert 1+2>6
# AssertionError

# 18 ----------高阶函数  可将函数作为参数传入的函数
def apply(func, x, y):
    return func(x, y)


def add(x, y):
    return x + y


def multiply(x, y):
    return x * y


result1 = apply(add, 3, 4)  # 结果为 7
result2 = apply(multiply, 3, 4)  # 结果为 12

print(result1)
print(result2)

# 18 ----------匿名函数 lambda
# python里的lambda函数“ ：”后只能有一个语句，这点与C++不同
result3 = apply(lambda num1, num2: num1 / num2, 34, 2)
print(result3)

#解包操作
persons_list = [{'name': 'John', 'age': 30}, {'name': 'Alice', 'age': 25}]

for person in persons_list:
    name, age = person.items()
    print(f"Name: {name[1]}, Age: {age[1]}")
