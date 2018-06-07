#-*- coding:utf-8 -*-

import sys
import subprocess
import datetime
import requests

from src.ReadXml import *
from src.LogModule import *

setDetailLogging()

def FirstLogin():

    conf = readxml()
    url = conf['Host'] + ':' + conf['Port']
    API = "/vill/firstLogin"

    loggerD.info('[*] Run funciton : ' + sys._getframe().f_code.co_name)

    value = {}
    value["username"] = '13720277762'
    value["password"] = 'X1234567890'
    # value["smsVerifyCode"] = '2222'

    try:

        rsp_login = requests.request(method='POST', url=url + API, params=value)

        rsp_json_data = rsp_login.json()
        # print (rsp_login.encoding)

        if rsp_json_data['retCode'] == 'success':
            # loggerD.info('[*] API Address: ' + url+API)
            loggerD.info('[*] Response Data: ' + rsp_login.text)
            loggerD.info('[*] Function pass ')
            return True
        else:
            loggerD.info('[*] Response Data: ' + rsp_login.text)
            loggerD.info('[*] Function failed ')
            return False

    except Exception as e:

        loggerD.error('[!] Function failed : ' + str(e))
        return False



if __name__ == '__main__':

    loggerD.info('########### Test start ########### ')

    R_FirstLogin = FirstLogin()

    loggerD.info('########### Test end ########### \n')

    if not R_FirstLogin :
        assert False

