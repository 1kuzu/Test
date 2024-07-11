import re
# '''1:用正则表达式查找文本模式
#    2:匹配Regex对象
#    3:利用括号分组
#    4:用管道匹配多个分组'''
# # #group()返回的数值类型是字符串
# # #groups()返回的数值类型的是一个元祖
# phoneNumRegex = re.compile(r'(\d{3})-(\d{4})-(\d{3})')
# mo = phoneNumRegex.search('我的电话号码是:138-1234-123')
# print('电话号码是'+mo.group())
# mo_all = mo.groups()
# print(type(mo_all))
# print(mo_all)
# for _ in mo_all:
#     print(_)

# #匹配许多文本中的一个
# heroRegax = re.compile(r'Batman|Tina Fey')
# mo1 = heroRegax.search('Batman and Tina Fey')
# print(mo1.group())

# #匹配多个模式中的一个这里的Bat作为一个前缀
# batRegax = re.compile(r'Bat(man|mobile|coter|bat)')
# mo2 = batRegax.search('Batmobile lost a wheel')
# print(mo2.group())

# #实现可选匹配
# batRegax = re.compile(r'Bat(wo)?man')
# # mo1 = batRegax.search('The advanture of Batman')
# mo3 = batRegax.search('The advanture of Batwoman')
# print(mo3.group())

# #用星号实现对分组的0到无数次匹配
# batRegax = re.compile(r'Bat(wo)*man')
# # mo1 = batRegax.search('The advanture of Batman')
# mo4 = batRegax.search('The advanture of Batwowowowowoman')
# print(mo4.group())

# #用加号匹配1到多次，要求至少出现了一次zb
# batRegax = re.compile(r'Bat(wo)+man')
# mo5 = batRegax.search('The advanture of Batman')
# # print(mo5.group())
# mo6 = batRegax.search('The advanture of Batwoman')
# print(mo6.group())



#用花括号匹配特定次数 {1,3}表示一到三次
batRegax = re.compile(r'Bat(wo){1,3}man')
mo7 = batRegax.search('The advanture of Batwowowoman')
print(mo7.group())

#贪心与非贪心匹配方法
batnonRegax = re.compile(r'Bat(wo){2,3}?')
mo8 = batnonRegax.search('The advanture of Batwowowo')
print(mo8.group())

greedHaragx = re.compile(r'(Ha){1,3}?')
mo9 = greedHaragx.search('HaHaHa')
print(mo9.group())

#findall方法 与search方法不同，会返回所有匹配的文本
phoneNumRegax = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo10 = phoneNumRegax.search('Cell:415-555-9999 Work:212-999-8789')
print(mo10.group)

phoneNumRegax = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo10 = phoneNumRegax.findall('Cell:415-555-9999 Work:212-999-8789')
for _ in mo10:
    print(f'phonenumber:{_}')

#字符分类
xmasRegex = re.compile(r'\d+\s\w+')
mo11 = xmasRegex.findall('12 drummers,11 pipers,19 lords')
print(mo11)

#建立自己的字符分类
#使用短横线可以表示字母和数字的范围，例如[a-zA-Z]可以匹配所有的字母
#例如使用[1-3]可以表示匹配1到3之间的所有数字

vowlRegex = re.compile(r'[1-3]')
mo12 = vowlRegex.findall('sndfaahwuibb11123hf78wuic')
print(mo12)

#插入字符和美元字符
beginWithHello = re.compile(r'^Hello')
mo13 = beginWithHello.search('Hello world!')
print(mo13.group())

#通配字符,使用.来替代除了换行符以外的所有字符
atRegex = re.compile(r'.at')
mo14 = atRegex.findall('The cat in the hat sat on the flat mat')
print(mo14)

#用点-星匹配所有的字符
nameRegex = re.compile(r'First Name:(.*) Last Name:(.*)')
mo15 = nameRegex.search('First Name:AL Last Name:Sweigart')
print(mo15.group(1))
print(mo15.group(2))

#用句点字符串来匹配换行符,加入re.DOTALL作为参数后可以匹配换行符
newlineRegex = re.compile('.*')
mo16 = newlineRegex.search('Serve the public trust. \nProtect the innocent')
print(mo16.group())


newlineRegex = re.compile('.*',re.DOTALL)
mo16 = newlineRegex.search('Serve the public trust. \nProtect the innocent')
print(mo16.group())

#不区分大小写的匹配,传入re.I或者re.IGNORECASE
robocop = re.compile(r'robocop',re.I)
mo17 = robocop.search('I am goOd Student RoboCop')
print(mo17.group()) 

#用sub()方法替换字符串 sub()中有两个参数第一个字符串是用来替换用的，第二个字符串是目标字符串
namesRegex = re.compile(r'Agent \w+')
target = 'Agent Alice gave the secrest documents to Agent Bob.'
mo18 = namesRegex.sub('CENSORED',target)
print(mo18)

agentnamesRegex = re.compile(r'Agent (\w)\w*')
mo18 = agentnamesRegex.sub(r'\1****','Agent Alice told Agent Carlor')
print(mo18)

#管理复杂的正则表达式，传入re.VERBOSE作为第二个参数忽略空白符和注释
phoneRegex = re.compile

#组合使用re.IGNORECASE re.DOTALL re.VERBOSE

















































