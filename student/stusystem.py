import os.path

filename = 'student.txt'


def main():
    while True:
        menum()
        choice = int(input('请选择'))
        if choice in [0, 1, 2, 3, 4, 5, 6, 7]:
            if choice == 0:
                answer = input('您确定要退出系统嘛?y/n')
                if answer == 'y' or answer == 'Y':
                    print('谢谢您的使用！！！')
                    break
                else:
                    continue
            elif choice == 1:
                insert()
            elif choice == 2:
                search()
            elif choice == 3:
                delete()
            elif choice == 4:
                modify()
            elif choice == 5:
                sort()
            elif choice == 6:
                total()
            elif choice == 7:
                show()
        else:
            print('您输入的数字错误，请您重新输入！')
            continue


def menum():
    print('========================学生信息管理系统================')
    print('------------------------功能菜单----------------------')
    print('\t\t\t\t\t\t1.录入学生信息')
    print('\t\t\t\t\t\t2.查找学生信息')
    print('\t\t\t\t\t\t3.删除学生信息')
    0
    print('\t\t\t\t\t\t4.修改学生信息')
    print('\t\t\t\t\t\t5.排序')
    print('\t\t\t\t\t\t6.统计学生总人数')
    print('\t\t\t\t\t\t7.显示所有学生信息')
    print('\t\t\t\t\t\t0.退出')
    print('-----------------------------------------------------')


def insert():
    student_list = []
    while True:
        id = input('请输入ID（如1001）：')
        if not id:
            print('您输入为空，退出添加学生信息')
            break
        name = input('请输入姓名：')
        if not id:
            print('您输入为空，退出添加学生信息')
            break
        try:
            english = int(input('请输入英语成绩：'))
            python = int(input('请输入Python成绩：'))
            java = int(input('请输入java成绩：'))
        except:
            print("输入无效，不是整型类型，请重新输入")
            break
        # 将学生信息保存到新创建空字典里面，然后再添加到列表里面进去
        student = {'id': id, 'name': name, 'english': english, 'python': python, 'java': java}
        student_list.append(student)
        answer = input('是否继续添加？y/n')
        if answer == 'y' or answer == 'Y':
            continue
        else:
            break

    # 退出循环后，将信息保存到文本文件中，save()
    save(student_list)
    print('学生信息录入完毕!!!')


def save(lst):
    try:
        stu_text = open(filename, 'a', encoding='utf-8')
    except:
        stu_text = open(filename, 'w', encoding='utf-8')
    for item in lst:
        stu_text.write(str(item) + '\n')
    stu_text.close()


def search():
    choice = int(input('请输入查找方式：1或2（1为要查询学生的ID，2为要查询学生的姓名）'))
    if choice in [1, 2]:
        if choice == 1:
            student_id = input('请输入要查询学生的ID：')
            if os.path.exists(filename):
                with open(filename, 'r', encoding='utf-8') as file:
                    student_old = file.readlines()
                    for item in student_old:
                        d = dict(eval(item))
                        if d['id'] == student_id:
                            print("已找到学生信息")
                            # 格式化输出找到的学生信息内容
                            format_title = '{:^6}\t{:^12}\t{:^8}\t{:^10}\t{:^10}'
                            print(format_title.format('ID', '姓名', '英语成绩', 'python成绩', 'java成绩'))
                            format_data = '{:^6}\t{:^12}\t{:^8}\t{:^10}\t{:^10}'
                            print(format_data.format(str(d['id']), str(d['name']), int(d['english']),
                                                     int(d['python']), int(d['java'])))
                            break

            answer = input('是否继续查询其他学生的信息?y/n')
            if answer == 'y' or answer == 'Y':
                search()
            else:
                return
        if choice == 2:
            student_name = input('请输入要查询学生的姓名：')
            if os.path.exists(filename):
                with open(filename, 'r', encoding='utf-8') as file:
                    student_old = file.readlines()
                    for item in student_old:
                        d = dict(eval(item))
                        if d['name'] == student_name:
                            print("已找到学生信息")
                            format_title = '{:^6}\t{:^12}\t{:^8}\t{:^10}\t{:^10}'
                            print(format_title.format('ID', '姓名', '英语成绩', 'python成绩', 'java成绩'))
                            format_data = '{:^6}\t{:^12}\t{:^8}\t{:^10}\t{:^10}'
                            print(format_data.format(str(d['id']), str(d['name']), int(d['english']),
                                                     int(d['python']), int(d['java'])))
                            break

            answer = input('是否继续查询其他学生的信息?y/n')
            if answer == 'y' or answer == 'Y':
                search()
            else:
                return
    else:
        print('您输入有误，请重新输入')
        return


def delete():
    while True:
        student_id = input('请输入要删除的学生id:')
        if student_id != '':
            if os.path.exists(filename):
                with open(filename, 'r', encoding='utf-8') as file:
                    student_old = file.readlines()
            else:
                student_old = []
            flag = False
            if student_old:
                with open(filename, 'w', encoding='utf-8') as file:
                    d = {}
                    for item in student_old:
                        d = dict(eval(item))  # 将字符串转换成字典
                        if d['id'] != student_id:
                            file.write(str(d) + '\n')
                        else:
                            flag = True  # 表示已经删除
                    if flag:
                        print(f'id为{student_id}的学生信息已经被删除')
                    else:
                        print(f'没有找到id为{student_id}的学生信息')
            else:
                print("无学生信息")
                break
            show()
            answer = input('是否继续删除?y/n')
            if answer == 'y' or answer == 'Y':
                continue
            else:
                break


def modify():
    show()
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as file:
            student_old = file.readlines()
    else:
        return
    student_id = input('请输入需要修改学生信息的id：')
    with open(filename, 'w', encoding='utf-8') as file:
        for item in student_old:
            d = dict(eval(item))
            if d['id'] == student_id:
                print('找到学生信息，可以修改它的信息了')
                while True:
                    try:
                        d['name'] = input('请输入姓名')
                        d['english'] = int(input('请输入英语成绩'))
                        d['python'] = int(input('请输入python成绩'))
                        d['java'] = int(input('请输入java成绩'))
                    except:
                        print('您的输入有误，请重新输入！！！')
                    else:
                        break
                file.write(str(d) + '\n')
                print('修改成功')
            else:
                file.write(str(d) + '\n')
    answer = input('是否继续修改其他学生的信息?y/n')
    if answer == 'y' or answer == 'Y':
        modify()


def sort():
    show()
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as file:
            student_list = file.readlines()
        student_new = []
        for item in student_list:
            d = dict(eval(item))
            student_new.append(d)
    else:
        return
    asc_or_desc = input('请选择升序还是降序（0.升序，1.降序）:')
    if asc_or_desc == '0':
        asc_or_desc_bool = False
    elif asc_or_desc == '1':
        asc_or_desc_bool = True
    else:
        print('您的输入有误，请重新输入')
        sort()
    mode = input('请选择排序方式(1.按英语成绩排序 2.按python成绩排序 3.按java成绩排序):')
    if mode == '1':
        student_new.sort(key=lambda x: int(x['english']), reverse=asc_or_desc_bool)
    elif mode == '2':
        student_new.sort(key=lambda x: int(x['python']), reverse=asc_or_desc_bool)
    elif mode == '3':
        student_new.sort(key=lambda x: int(x['java']), reverse=asc_or_desc_bool)
    else:
        print('您的输入有误，请重新输入')
        sort()
    show_student(student_new)


def total():
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as file:
            students = file.readlines()
            if students:
                print(f'一共有{len(students)}名学生')
            else:
                print("学生信息文件的内容为空")
    else:
        print("没有学生信息文件")
        return

def show_student(lst):
    format_title = '{:^6}\t{:^12}\t{:^8}\t{:^10}\t{:^10}'
    print(format_title.format('ID', '姓名', '英语成绩', 'python成绩', 'java成绩'))
    format_data = '{:^6}\t{:^12}\t{:^8}\t{:^10}\t{:^10}'
    for item in lst:
        # 格式化输出找到的学生信息内容
        print(format_data.format(str(item['id']), str(item['name']), int(item['english']),
                                 int(item['python']), int(item['java'])))
    return

def show():
    if os.path.exists(filename):
        format_title = '{:^6}\t{:^12}\t{:^8}\t{:^10}\t{:^10}'
        print(format_title.format('ID', '姓名', '英语成绩', 'python成绩', 'java成绩'))
        format_data = '{:^6}\t{:^12}\t{:^8}\t{:^10}\t{:^10}'
        with open(filename, 'r', encoding='utf-8') as file:
            students = file.readlines()
            for item in students:
                d = dict(eval(item))
                # 格式化输出找到的学生信息内容
                print(format_data.format(str(d['id']), str(d['name']), int(d['english']),
                                         int(d['python']), int(d['java'])))
    else:
        print('该学生信息文件不存在')
    return

if __name__ == '__main__':
    main()
