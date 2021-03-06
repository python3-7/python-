# Python基础语法

注释 -----#标注的文本  
数字  
&nbsp;&nbsp;&nbsp;&nbsp;整数  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Python3开始不区分long和int,long被重新命名为int,所以只有int了,不再区分长整形短整形  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;进制0xa 十六进制 0o10 八进制 0b10二进制  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;bool,只有True和False两个值  
&nbsp;&nbsp;&nbsp;&nbsp;浮点数  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1.2、3.1415、-0.12、1.4e9等价于1.46*10**9，本质上使用了C语言的double类型  
&nbsp;&nbsp;&nbsp;&nbsp;复数：1+2j  

字符串  
&nbsp;&nbsp;&nbsp;&nbsp;使用'"单双引号引用的字符的序列  
&nbsp;&nbsp;&nbsp;&nbsp;'''和“”“单双三引号，可以跨行、可以在其中自由的使用单双引号  
&nbsp;&nbsp;&nbsp;&nbsp;r前缀：在字符串前面加上r或R前缀，表示该字符串不做特殊处理 
&nbsp;&nbsp;&nbsp;&nbsp;f前缀：3.6版本开始，新增f前缀，格式化字符串 

转义序列  
&nbsp;&nbsp;&nbsp;&nbsp;\\\ &nbsp;&nbsp;\t &nbsp;&nbsp;\r &nbsp;&nbsp;\n &nbsp;&nbsp;\\' &nbsp;&nbsp; \\"  
&nbsp;&nbsp;&nbsp;&nbsp;前缀r，把里面的所有字符当普通字符对待  
缩进  
&nbsp;&nbsp;&nbsp;&nbsp;使用4个空格缩进  
续行  
&nbsp;&nbsp;&nbsp;&nbsp;在行尾使用\  
&nbsp;&nbsp;&nbsp;&nbsp;如果使用各种括号，认为括号内是一个整体，内部跨行不用\   
标识符  
1. 一个名字，用来指代一个值
2. 只能是字母、下划线和数字
3. 只能以字母和下划线开头
4. 不能是python的关键字，例如def、class就不能作为标识符
5. Python是大小写敏感的  
约定：不允许使用中文，不要使用歧义单词，例如class_，在python中不要随便使用下划线开头的标识符  

常量  
&nbsp;&nbsp;&nbsp;&nbsp;一旦赋值就不能改变值得标识符，python中无法定义常量  
字面常量  
&nbsp;&nbsp;&nbsp;&nbsp;一个单独的量，例如12、"abc"、'2341321.03e-9'  
变量  
&nbsp;&nbsp;&nbsp;&nbsp;赋值后，可以改变值得标识符   

运算符Operator  
&nbsp;&nbsp;&nbsp;&nbsp;算术运算符：+ - * / % **，自然除/结果是浮点数，整除//。注：2.x中/和//都是整除  

位运算符  
&nbsp;&nbsp;&nbsp;&nbsp;& ： 按位与运算符：参与运算的两个值,如果两个相应位都为1,则该位的结果为1,否则为0  
&nbsp;&nbsp;&nbsp;&nbsp;| ： 按位或运算符：只要对应的二个二进位有一个为1时，结果位就为1。  
&nbsp;&nbsp;&nbsp;&nbsp;^ ：按位异或运算符：当两对应的二进位相异时，结果为1  
&nbsp;&nbsp;&nbsp;&nbsp;~ ：按位取反运算符：对数据的每个二进制位取反,即把1变为0,把0变为1 。  
&nbsp;&nbsp;&nbsp;&nbsp;<< : 左移动运算符：运算数的各二进位全部左移若干位，由 << 右边的数字指定了移动的位数，高位丢弃，低位补0。  
&nbsp;&nbsp;&nbsp;&nbsp;>> : 右移动运算符：把">>"左边的运算数的各二进位全部右移若干位，>> 右边的数字指定了移动的位数  

比较运算符  
&nbsp;&nbsp;&nbsp;&nbsp;== &nbsp;&nbsp;!=&nbsp;&nbsp;>&nbsp;&nbsp;<&nbsp;&nbsp;>=&nbsp;&nbsp;<=  
&nbsp;&nbsp;&nbsp;&nbsp;返回的是一个bool值  

逻辑运算符  
&nbsp;&nbsp;&nbsp;&nbsp;与或非 and &nbsp;&nbsp;or&nbsp;&nbsp; not  
&nbsp;&nbsp;&nbsp;&nbsp;短路运算符  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;and 如果第一个表达式是假False的话，整个结果一定是假  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;or 如果第一个表达式是真True的话，整个结果一定是真  

赋值运算符  
&nbsp;&nbsp;&nbsp;&nbsp;a = min(3,5)  
&nbsp;&nbsp;&nbsp;&nbsp;+= &nbsp;&nbsp;-=&nbsp;&nbsp;*=&nbsp;&nbsp;/=&nbsp;&nbsp;%=  等  
&nbsp;&nbsp;&nbsp;&nbsp;x = y = z = 10  
成员运算符  
&nbsp;&nbsp;in、not in  
身份运算符  
&nbsp;&nbsp;is、is not  

表达式Expression  
由数字、符号、括号、变量等的组合  
&nbsp;&nbsp;&nbsp;&nbsp;算术表达式  
&nbsp;&nbsp;&nbsp;&nbsp;逻辑表达式  
&nbsp;&nbsp;&nbsp;&nbsp;赋值表达式   
python中，***赋值即定义**，如果一个变量已经定义，赋值相当于重新定义  

### 单分支结构
if语句  
>if condition:  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;代码块

condition必须是一个bool类型，这个地方有一个隐式转换bool  
代码块  
&nbsp;&nbsp;类似于if语句的冒号后面的就是一个语句块  
&nbsp;&nbsp;在if、for、def、class等关键字后使用代码块  

### 多分支结构 
if...elif...else语句
>if condition1:  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;代码块1  
elif condition2:  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;代码块2  
elif condition3：  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;代码块3  
......  
else:  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;代码块  

多分支结构，只要有一个分支被执行，其他分支都不会被执行  
前一个条件被测试过，下一个条件相当于隐含着这个条件  

分支嵌套：嵌套结构，可以是分支、循环的嵌套；可以互相嵌套多层  

## 循环
while语句  
语法： 
>while condition:  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;block  

当条件满足即condition为True，进入循环体，执行block  


for语句  
语法  
>for element in iterable:  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;block  

当可迭代对象中有元素可以迭代，进入循环体，执行block  

range函数
>range( )  
一般与for循环搭配使用  
for i in range( )  

#### continue与break的区别
continue表示中断当前循环的当此执行，继续下一次循环  

break表示终止当前循环，当循环与if语句嵌套使用时，break不是跳出if，而是终止if外的break所在的循环  

相同点：都是循环的控制语句，只影响当前循环，如果循环嵌套，continue和break也只影响语句所在的那一层循环  


****

