#-*- coding:utf-8 -*-

import sys
import subprocess
import datetime
import requests

from src.ReadXml import *
from src.LogModule import *

setDetailLogging()

def Login():

    conf = readxml()
    url = conf['Host'] + ':' + conf['Port']
    API = "/vill/login"

    loggerD.info('[*] Run funciton : ' + sys._getframe().f_code.co_name)

    value = {}
    value["username"] = '13720277761'
    value["password"] = 'X1234567890'

    try:

        rsp_login = requests.request(method='POST', url=url + API, params=value)

        rsp_json_data = rsp_login.json()
        # print (rsp_login.encoding)

        if rsp_json_data['retCode'] == 'success':
            # loggerD.info('[*] API Address: ' + url+API)
            loggerD.info('[*] Response Data: ' + rsp_login.text)
            loggerD.info('[*] Function pass \n ')
            return True
        else:
            loggerD.info('[*] Response Data: ' + rsp_login.text)
            loggerD.info('[*] Function failed \n ')
            return False

    except Exception as e:

        loggerD.error('[!] Function failed : ' + str(e))
        return False

def Login_errPwd():

    conf = readxml()
    url = conf['Host'] + ':' + conf['Port']
    API = "/vill/login"

    loggerD.info('[*] Run funciton : ' + sys._getframe().f_code.co_name)

    value = {}
    value["username"] = '13720277761'
    value["password"] = '1234562'                             # 写一个错误的密码

    try:

        rsp_login = requests.request(method='POST', url=url + API, params=value)

        rsp_json_data = rsp_login.json()
        # print (rsp_login.encoding)

        if rsp_json_data['retCode'] != 'success':
            # loggerD.info('[*] API Address: ' + url+API)
            loggerD.info('[*] Response Data: ' + rsp_login.text)
            loggerD.info('[*] Function pass \n ')
            return True
        else:
            loggerD.info('[*] Response Data: ' + rsp_login.text)
            loggerD.info('[*] Function failed \n ')
            return False

    except Exception as e:

        loggerD.error('[!] Function failed : ' + str(e))
        return False

def Login_blankPwd():

    conf = readxml()
    url = conf['Host'] + ':' + conf['Port']
    API = "/vill/login"

    loggerD.info('[*] Run funciton : ' + sys._getframe().f_code.co_name)

    value = {}
    value["username"] = '13720277761'
    value["password"] = ''                             # 写一个空的密码

    try:

        rsp_login = requests.request(method='POST', url=url + API, params=value)

        rsp_json_data = rsp_login.json()
        # print (rsp_login.encoding)

        if rsp_json_data['retCode'] != 'success':
            # loggerD.info('[*] API Address: ' + url+API)
            loggerD.info('[*] Response Data: ' + rsp_login.text)
            loggerD.info('[*] Function pass \n ')
            return True
        else:
            loggerD.info('[*] Response Data: ' + rsp_login.text)
            loggerD.info('[*] Function failed \n ')
            return False

    except Exception as e:

        loggerD.error('[!] Function failed : ' + str(e))
        return False

def Login_blankUser():

    conf = readxml()
    url = conf['Host'] + ':' + conf['Port']
    API = "/vill/login"

    loggerD.info('[*] Run funciton : ' + sys._getframe().f_code.co_name)

    value = {}
    value["username"] = ''
    value["password"] = '1'                             # 写一个空的密码

    try:

        rsp_login = requests.request(method='POST', url=url + API, params=value)

        rsp_json_data = rsp_login.json()
        # print (rsp_login.encoding)

        if rsp_json_data['retCode'] != 'success':
            # loggerD.info('[*] API Address: ' + url+API)
            loggerD.info('[*] Response Data: ' + rsp_login.text)
            loggerD.info('[*] Function pass \n ')
            return True
        else:
            loggerD.info('[*] Response Data: ' + rsp_login.text)
            loggerD.info('[*] Function failed \n ')
            return False

    except Exception as e:

        loggerD.error('[!] Function failed : ' + str(e))
        return False

if __name__ == '__main__':

    loggerD.info('########### Test start ########### ')

    R_Login = Login()
    R_Login_errPwd = Login_errPwd()
    R_Login_blankPwd = Login_blankPwd()
    R_Login_blankUser = Login_blankUser()

    loggerD.info('########### Test end ########### \n')

    if not (R_Login and  R_Login_errPwd and  R_Login_blankPwd and R_Login_blankUser) :
        assert False

