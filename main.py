students = []
def show_menu():
    print("\n=====学生成绩管理系统=====")
    print("1.添加学生")
    print("2.删除学生")
    print("3.修改学生")
    print("4.按学号查询")
    print("5.按姓名查询")
    print("6.显示全部学生信息")
    print("7.成绩统计")
    print("8.排序")
    print("9.保存数据")
    print("0.退出")
def add_student():
    print("\n=====添加学生=====")
    while True:
        student_id = input("请输入学号：").strip()
        if not student_id:
            print("学号不能为空，请重新输入！")
            continue

        is_duplicate = False
        for stu in students:
            if stu["id"] == student_id:
                is_duplicate = True
                break
        if is_duplicate:
            print("该学号已存在，请勿重复添加！")
            continue

        name = input("请输入姓名：").strip()
        if not name:
            print("姓名不能为空，请重新输入")
            continue

        try:
            math_score = float(input("请输入数学成绩："))
            english_score = float(input("请输入英语成绩："))
            python_score = float(input("请输入python成绩："))
        except ValueError:
            print("成绩必须是数字，请重新输入！")
            continue

        if not (0 <= math_score <= 100 and 0 <= english_score <= 100 and 0 <= python_score <= 100):
            print("成绩必须在0-100之间")
            continue

        student = {
            "id": student_id,
            "name": name,
            "math": math_score,
            "english": english_score,
            "python": python_score,
        }
        students.append(student)
        print(f"成功添加学生：{name}(学号{student_id})")
        break


def show_all_students():
    print("\n=====全部学生信息=====")
    if not students:
        print("当前暂无学生数据！")
        return

    print(f"{'学号':<10}{'姓名':<8}{'数学':<8}{'英语':<8}{'Python':<8}")
    print("-" * 50)
    for stu in students:
        print(
            f"{stu['id']:<10}{stu['name']:<8}{stu['math']:<8}"
            f"{stu['english']:<8}{stu['python']:<8}"
        )


def main():
    while True:
        show_menu()
        choice = input("请选择功能：").strip()
        if choice == "1":
            add_student()
        elif choice == "2":
            print("【删除学生】")
        elif choice == "6":
            show_all_students()
        elif choice == "0":
            print("感谢使用，再见！")
            break
        else:
            print("无效选项，请重新输入！")


if __name__ == "__main__":
    main()
