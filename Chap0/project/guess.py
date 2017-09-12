# -*- coding: utf-8 -*-
import random
import re
from sys import argv


list1 = [0,1,2,3,4,5,6,7,8,9]
list3 = random.sample(list1, 4)
while list3[0]== 0:
    list3 = random.sample(list1, 4)
#print(list3)

i = 0
a = 0
b = 0
guesstimes = 0

while (guesstimes <= 10):
    guess_num = input("猜测一个四位数：")
    while not str(guess_num).isdigit():
        guess_num = input('请确保输入的是纯数字！请重新输入：')
    guess_num = int(guess_num)
    while not int(guess_num)>= 1000 and int(guess_num) <= 9999:
        guess_num = input('请输入1000-9999范围内四位数!')
    guess_num = int(guess_num)
    b1 = guess_num // 1000
    b2 = (guess_num // 100) % 10
    b3 = (guess_num // 10) % 10
    b4 = guess_num % 10
    list4 = [b1,b2,b3,b4]
    for i in range(0,4):
        if list4[i] == list3[i]:
            a = a + 1
        if list4[i] in list3  and list4[i] != list3[i]:
            b = b + 1
        i = i + 1
    print("%rA%rB"%(a,b))
    guesstimes = guesstimes + 1
    leavetimes = 10 - guesstimes
    print("还有%s次机会" %leavetimes)
    i = 0
    a = 0
    b = 0
    if guess_num == 1000*list3[0]+100*list3[1]+10*list3[2]+list3[3]:
        print('恭喜你！猜对了')
        break
    if leavetimes == 0:
        print('你失败了！游戏结束！')
        break
