## card 1 任务分解
### step 1  随机生成数字——random 模块
1.1 不重复——random.sample

1.2 弯路：random(1000,9999)——能避免首位为零的情况，但数字会重复使用

1.3 random.sample([0-9]),会出现首位为零的情况，想到分别从[0-9]取三位，从[1-9]取千位，但也会出现重复数字

1.4 randam.sample([0-9],4)，一次取完，出现首位为零但情况循环重取，知道首位不为零

### step 2 存储数字——利用 list 数组
2.1 很自然想到 list 数组存放各位数字，存取方便。常用的 list 方法有 list.pop、list.remove、list.insert、list.extend 

eg:list1 = [1,2,3],list2 = [2,3,4] list1.extend(list[2]) = [1,2,3,4] list1.insert(2,list[2]) = [1,2,4,3]

2.2 数组转化为数字 小学数学都学过 1000a + 100b + 10c + d = adcd

2.3 int 与 str  python 中很方便的转化 int(s) 转化为整型 str(s) 转化为字符串

### step 3 判断输入是什么——正则表达式
3.1 输入了一个字符串，我要报警，让玩家重新输入，怎么判断呢？尝试了用 str.isdigit()，该方法仅在对象是字符串才能使用，因此要注意转格式

3.2 利用正则表达式，太过艰辛（toulan），也被我放弃

## card2 逻辑构造

逻辑线很清楚：生成一个数————猜一个数————给出提示————改变指针————不对再猜————成果／失败
用 def 函数分开写会很清楚，想清楚就很简单。

## card3 py2 和 py3 的坑

py2 && py3 还是有比较大的差别的
- input() 和 raw_input() 前者输出的格式是 ，后者输出的是字符串
- / 和//, 2 中的 ／ 还是整数，到了 3 不得不用 ／／ ，被坑惨了，明明写好的逻辑改用 3 跑就不对了， 几 A 几 B 识别不出来
- print 3 比 2 多括号，不仅如此，3 的格式化输出符号也从外面移到括号内了