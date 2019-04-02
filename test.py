import math

a1 = 6541367999
# a1 = 9999
a2 = 7140229933
a = 100
total = (2 ** a) - 1
# 二进制表达式

b = b'\x00' * int(-(-a1//8))
total_temp = (str(b).replace('\\x', '')).replace("b'", '').replace("'", "")

def change(string, number):
    # number 0 表示第一位
    if string == 'f':
        temp = 15
    elif string == 'e':
        temp = 14
    elif string == 'd':
        temp = 13
    elif string == 'c':
        temp = 12
    elif string == 'b':
        temp = 11
    elif string == 'a':
        temp = 10
    else:
        temp = int(string)

    temp = temp | (2**number)

    if temp == 15:
        temp_2 = 'f'
    elif temp == 14:
        temp_2 = 'e'
    elif temp == 13:
        temp_2 = 'd'
    elif temp == 12:
        temp_2 = 'c'
    elif temp == 11:
        temp_2 = 'b'
    elif temp == 10:
        temp_2 = 'a'
    else:
        temp_2 = str(temp)
    return temp_2


def hex_position(number):
    # 第几个二进制位运算符的区间 （从第0个起算）
    # bin_position = number, 2)//1
    # 第几个16进制运算符的区间（从第0个起算）
    position = number//4
    residual = number % 4
    return int(position), int(residual)

def mod(string):
    # number 0 表示第一位
    if string == 'f':
        temp = []
    elif string == 'e':
        temp = [0]
    elif string == 'd':
        temp = [1]
    elif string == 'c':
        temp = [0, 1]
    elif string == 'b':
        temp = [2]
    elif string == 'a':
        temp = [0, 2]
    elif string == '9':
        temp = [1, 2]
    elif string == '8':
        temp = [0, 1, 2]
    elif string == '7':
        temp = [3]
    elif string == '6':
        temp = [0, 3]
    elif string == '5':
        temp = [1, 3]
    elif string == '4':
        temp = [0, 1, 3]
    elif string == '3':
        temp = [2, 3]
    elif string == '2':
        temp = [0, 2, 3]
    elif string == '1':
        temp = [1, 2, 3]
    elif string == '0':
        temp = [0, 1, 2, 3]

    return temp


for i in range(2, a1):
    for j in range(2, -(-a1//i)):

        p, r = hex_position(i*j-1)
        total_temp = total_temp[:p] + change(total_temp[p], r) + total_temp[p+1:]

# for t in range(len(total_temp)):
#     if total_temp[t] != 'f':
#         for w in mod(total_temp[t]):
#             print(t*4 + w+1)

with open('kkk.txt', 'w') as file:
    file.write(total_temp)














