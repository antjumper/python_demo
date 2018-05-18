""" 输入名字的练习 """
# name = input("enter your name:")
# print(name)

"""输入一个数字的练习"""
# num = int(input("Enter an integer:"))
# print(num)

"""输入表达式的练习"""
# result = eval(input("输入一个表达式："))
# print(result)

"""输入练习"""

# names = input("Enter names separated by commas: ").title().split(",")
# assignments = input("Enter assignment counts separated by commas: ").split(",")
# grades = input("Enter grades separated by commas: ").split(",")
#
# message = "Hi {},\n\nThis is a reminder that you have {} assignments left to \
# submit before you can graduate. You're current grade is {} and can increase \
# to {} if you submit all assignments before the due date.\n\n"
#
# for name, assignment, grade in zip(names, assignments, grades):
#     print(message.format(name, assignment, grade, int(grade) + int(assignment)*2))

"""异常处理"""
    # try:
    # except ValueError:
    # except ValueError:
    # except KeyboardInterrupt:

"""异常处理 练习"""


# def create_groups(items, num_groups):
#     try:
#             size = len(items) // num_groups
#     except ZeroDivisionError as e:
#             print("WARNING: {}".format(e))
#             return []
#     else:
#         groups = []
#         for i in range(0, len(items), size):
#             groups.append(items[i:i + size])
#     finally:
#         print("{} groups returned.".format(num_groups))
#     return groups
#
#
# print("Creating 6 groups...")
# for group in create_groups(range(32), 6):
#     print(list(group))
#
# print("\nCreating 0 groups...")
# for group in create_groups(range(32), 0):
#     print(list(group))

"""文件读取练习"""

# f.readline()读取一行

# /Users/puhui/Desktop/ceshi_text.txt

# 读取文件  r w 和 a "a"是添加模式


f = open('/Users/puhui/Desktop/ceshi_text.txt', 'r')
file_data = f.read() # f.write("Hello there!")  #
f.close()

# with 函数 使用完函数之后自动关闭文件 不用再调用close了

with open('/Users/puhui/Desktop/ceshi_text.txt', 'r') as f:
    file_data = f.read()