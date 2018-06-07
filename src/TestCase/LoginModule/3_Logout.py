#-*- coding:utf-8 -*-

import sys
import subprocess
import datetime
import requests

from src.ReadXml import *
from src.LogModule import *

setDetailLogging()
vill_token = ''

def Logout():

    conf = readxml()
    url = conf['Host'] + ':' + conf['Port']
    API = "/vill/logout"
    # headers = {"vill_token": vill_token}
    cookies = dict(vill_token=vill_token)

    loggerD.info('[*] Run funciton : ' + sys._getframe().f_code.co_name)

    value = {}
    # value["username"] = '13720277762'
    # value["password"] = 'X1234567890'
    # value["smsVerifyCode"] = '2222'

    try:

        # rsp_login = requests.request(method='GET', url=url + API, headers=headers)
        rsp_login = requests.request(method='GET', url=url + API, cookies=cookies)

        rsp_json_data = rsp_login.json()
        # print (rsp_login.encoding)

        if rsp_json_data['retCode'] == 'success':
            # loggerD.info('[*] API Address: ' + url+API)
            loggerD.info('[*] Response Data: ' + rsp_login.text)
            loggerD.info('[*] Function pass \n')
            return True
        else:
            loggerD.info('[*] Response Data: ' + rsp_login.text)
            loggerD.info('[*] Function failed \n')
            return False

    except Exception as e:

        loggerD.error('[!] Function failed : ' + str(e))
        return False

def Logout_err():

    conf = readxml()
    url = conf['Host'] + ':' + conf['Port']
    API = "/vill/logout"

    loggerD.info('[*] Run funciton : ' + sys._getframe().f_code.co_name)

    value = {}
    # value["username"] = '13720277762'
    # value["password"] = 'X1234567890'
    # value["smsVerifyCode"] = '2222'

    try:

        # rsp_login = requests.request(method='GET', url=url + API, headers=headers)
        rsp_login = requests.request(method='GET', url=url + API)

        rsp_json_data = rsp_login.json()
        # print (rsp_login.encoding)

        if rsp_json_data['retCode'] != 'success':
            # loggerD.info('[*] API Address: ' + url+API)
            loggerD.info('[*] Response Data: ' + rsp_login.text)
            loggerD.info('[*] Function pass \n')
            return True
        else:
            loggerD.info('[*] Response Data: ' + rsp_login.text)
            loggerD.info('[*] Function failed \n')
            return False

    except Exception as e:

        loggerD.error('[!] Function failed : ' + str(e))
        return False

def Login():
    global vill_token

    conf = readxml()
    url = conf['Host'] + ':' + conf['Port']
    API = "/vill/login"

    loggerD.info('[*] Run funciton : ' + sys._getframe().f_code.co_name)

    value = {}
    value["username"] = '13720277761'
    value["password"] = 'X1234567890'

    try:

        rsp_login = requests.request(method='POST', url=url + API, params=value)

        vill_token = rsp_login.cookies['vill_token']

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


if __name__ == '__main__':

    loggerD.info('########### Test start ########### ')

    R_Login = Login()
    R_Logout = Logout()
    R_Logout_err = Logout_err()

    loggerD.info('########### Test end ########### \n')

    if not (R_Logout and R_Login and R_Logout_err)  :
        assert False

