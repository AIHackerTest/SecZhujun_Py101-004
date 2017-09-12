# -*- coding: utf-8 -*-
import csv
def row_csv2dict(csv):
    dict_club={}
    with open('weather_info.txt',"r", encoding = "utf-8") as f:
        reader=csv.reader(f,delimiter=',')
        for row in reader:
            dict_club[row[0]]=row[1]
    return dict_club

def help():
	print('输入城市名查询天气')
	print('输入history查询历史')
	print('输入quit退出')

def main():
    file = row_csv2dict(csv)
    file.items()
    history = []
    help()
    print("请输入城市：")
    while True:
        city = input()
        if city == 'help':
        	help()
        elif city in file:
        	print(file.get(city))
        	city = city + ' ' + file.get(city)
        	history.append(city)
        	#print(history)
        elif city == 'history':
        	for i in history:
        		print(i)
        elif city == 'quit':
        	break
        else:
        	print('输入有误')


main()
