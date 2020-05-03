class Person():
    name = "muwj"
    name2 = "Tom"

    def get_name(self):
        return self.name

p1 = Person()
p1.get_name()
print(p1.name2)
print(p1.get_name())

Person.name = "mlm"
print(Person.name)  # 修改了类里面的属性，实例调用的结果也被修改
print(p1.name)

p1.name = "tcxq"
Person.name = "jjz"
print(p1.name)  # 当修改了实例的内容再修改类里面的内容，实例内容不能不修改，类的内容已经影响不到实例
print(Person.name)