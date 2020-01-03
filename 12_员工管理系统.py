
def show_menu():
    print('*' * 10 + '员工管理系统' + '*' * 10)
    print('1：添加员工信息')
    print('2：删除员工信息')
    print('3：修改员工信息')
    print('4：显示所有员工信息')
    print('5：退出管理系统')
    print('*' * 30)


employees = {}


def show_employees():
    if len(employees) == 0:
        print('当前没有员工信息！')
        return

    print('显示所有员工信息：')
    for emp_id, emp in employees.items():
        print(emp_id, emp.get('name'), emp.get('salary'))


def delete_employee():
    emp_id = input('请输入要删除的员工编号：')
    if employees.get(emp_id) is not None:
        del employees[emp_id]
        print('员工', emp_id, '删除成功！')
    else:
        print('员工编号不存在！')


def add_employee():
    print('开始添加员工信息！')
    employee_id = input('请输入员工编号：')
    if employees.get(employee_id) is not None:
        print('员工编号已存在，无法添加！')
        return

    name = input('请输入员工姓名：')
    salary = input('请输入员工工资：')
    employees[employee_id] = {'name': name, 'salary': salary}
    print('员工信息添加成功！')
    print('编号：', employee_id, '姓名：', name, '工资：', salary)


def edit_employee():
    employee_id = input('请输入要修改的员工编号：')
    if employees.get(employee_id) is None:
        print('员工编号不存在，无法修改！')
        return
    employee = employees[employee_id]
    print('员工编号：', employee_id, '姓名：', employee.get('name'), '工资：', employee.get('salary'))

    name = input('修改员工姓名为：')
    salary = input('修改员工工资为：')

    # 如果用户直接回车，表示不修改
    if name == '':
        name = employee.get('name')
    if salary == '':
        salary = employee.get('salary')

    employees[employee_id] = {'name': name, 'salary': salary}
    print('员工信息修改成功！')
    print('编号：', employee_id, '姓名：', name, '工资：', salary)


while True:
    show_menu()
    operation = input('请输入操作：')
    if operation == '1':
        add_employee()
    elif operation == '2':
        delete_employee()
    elif operation == '3':
        edit_employee()
    elif operation == '4':
        show_employees()
    elif operation == '5':
        print('退出管理系统!')
        break
    else:
        print('输入有误！')



