#-*- coding:utf-8 -*-

import os
import sys
from src.LogModule import *
import datetime

testcast_url = '.\\TestCase\\'
# file_dir = os.getcwd()
setInfoLogging()            # 初始化logging句柄
passCount = 0
failCount = 0

def getFileName():

    # for root, dirs, files in os.walk(testcast_url):
    #     print(root)  # 当前目录路径
    #     print(dirs)  # 当前路径下所有子目录
    #     print(files)  # 当前路径下所有非目录子文件

    for case in os.walk(testcast_url):
        case_dict['root'] = case[0]
        case_dict['files'] = case[2]
        if len(case_dict['files']):
            for i in case_dict['files']:
                if i[-3:] == '.py':
                    list_case.append(case_dict['root']+ '\\' + i)

def StartTest():
    global passCount
    global failCount

    getFileName()
    # print (list_case)

    for case in list_case:

        # 设置用例开始时间
        starttime = datetime.datetime.now()
        loggerA.info('[*] TestCase >>>   %s   <<<  Started !  ' % (case))

        # 执行用例
        # a = subprocess.Popen('python .\\TestCase\\' + case, stdout=subprocess.PIPE, shell=True)             #shell = True 允许命令已字符串形式传入
        # print (a.stdout.read())
        sign = os.system('python ' + case)
        if not sign:
            result = 'Pass'
            passCount += 1
        else:
            result = 'Failed'
            failCount += 1

        # 设置用例结束时间
        endtime = datetime.datetime.now()
        Usetime = endtime-starttime
        loggerA.info('[*] TestCase >>>   %s   <<<  Ended ! '% (case))
        loggerA.info('Result [ %s ] ==> Used (%sS) \n' %(result, Usetime))

if __name__ == '__main__':
    case_dict = {}
    list_case = []
    StartTest()
    loggerA.info('[*] All Result [passCount] : [ %d ] / [failCount] : [ %d ]  ' % (passCount, failCount))
