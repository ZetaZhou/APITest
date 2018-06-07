#-*- coding:utf-8 -*-

import sys
import subprocess
import datetime
import requests

from src.ReadXml import *
from src.LogModule import *

setDetailLogging()
vill_token = ''

def ModifyPwd():
    global vill_token
    conf = readxml()
    url = conf['Host'] + ':' + conf['Port']
    API = "/vill/updatePwd"
    cookies = dict(vill_token=vill_token)

    loggerD.info('[*] Run funciton : ' + sys._getframe().f_code.co_name)

    value = {}
    value["curPwd"] = 'X1234567890'
    value["newPwd"] = 'X1234567890'
    value["confirmPwd"] = 'X1234567890'

    try:

        # rsp_login = requests.request(method='GET', url=url + API, headers=headers)
        rsp_login = requests.request(method='POST', url=url + API, params = value, cookies = cookies)
        vill_token = rsp_login.cookies['vill_token']
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
    R_ModifyPwd = ModifyPwd()
    R_ModifyPwd_reset = ModifyPwd_reset()
    R_ModifyPwd_err = ModifyPwd_err()

    loggerD.info('########### Test end ########### \n')

    if not (R_ModifyPwd and R_Login and R_ModifyPwd_reset and R_ModifyPwd_err)  :
        assert False

