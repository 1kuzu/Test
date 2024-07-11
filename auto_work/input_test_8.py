import pyinputplus as pyip
# response = pyip.inputNum('确认是数字：')
# print(response)

#关键字参数min,max,greaterThan和lessThan
#设定一个输入数字的区间
# response = pyip.inputNum('确认是数字',min=4)
# print(response)
# response = pyip.inputNum('确认是数字',greaterThan=4)
# print(response)
# response = pyip.inputNum('确认是数字',lessThan=4)
# print(response)
# response = pyip.inputNum('确认是数字',max=4)
# print(type(response))

#关键字参数blank,除非设置参数blank为Trur，否则不允许输入空格字符
# response = pyip.inputNum('确认数字：',blank=True)
# print(response)

#关键字参数limit,timeout defalut分别作用是限制输入次数可以输入的次数是limit-1，输入时间，以及使用这些参数发生错误后返回的结果.
# response = pyip.inputNum('输入数字：',limit=3)
# print(response)
# response = pyip.inputNum('输入数字：',timeout=10)
# print(response)
# response = pyip.inputNum('输入数字：',limit=2,default='N/A')
# print(response)

#关键字参数allowRegexes和blockRegexes用正则表达式以接受其他类型的数字或者拒绝接受指定类型的数字
# response = pyip.inputNum('输入数字:',allowRegexes=[r'(I|V|X|L|C|D|M)+',r'zero'])
# print(response)
# response = pyip.inputNum('输入数字:',allowRegexes=[r'(i|v|x|l|c|d|m)+',r'zero'])
# print(response
# response = pyip.inputNum('输入数字:',blockRegexes=[r'[02468]$'])
# print(response)

#将自定义验证函数传递给inputCustom()
def addUptoTen(numbers):
    numbersList = list(numbers)
    for num ,digit in enumerate(numbersList):
        numbersList[num] = int(digit)
    if sum(numbersList)!=10:
        raise Exception('必须返回和为10 not%s' %(sum(numbersList)))
    return int(numbers)

response = pyip.inputCustom(addUptoTen)
print(response)






