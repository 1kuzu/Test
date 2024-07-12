import traceback
import logging
#抛出异常
# raise Exception("这是一条异常信息")
#使用try except语句处理异常信息
#取得回溯字符串
# try:
#     raise Exception("一条抛出异常信息")
# except : 
#     print("异常的优雅处理")
#     with open('traceback.txt','w',encoding='UTF-8') as f:
#         f.write(traceback.format_exc())
#         print("已经将回溯信息写入")


#断言
# assert 3>5

#logging模块使用日志
logging.basicConfig(level=logging.DEBUG,format='%(asctime)s - %(levelname)s - %(message)s')
logging.debug('Start of program')

def factorial(n):
    logging.debug('Start of factorial(%s%%)' % (n))
    total = 1
    for i in range(n+1):
        total *= i
        logging.debug('i is ' + str(i)+  ', total is '+ str(total))
    logging.debug('End of factorial(%s%%)' %(n))
    return total

print(factorial(5))
logging.debug('End of program')




    



