class Parent:
    print('This is Parent')


class Child(Parent):
    print('This is Child')


# Child()会自动调用父类中的print
print('isinstance(Child(), Parent)：', isinstance(Child(), Parent))
print('type(Child())：', type(Child()))
