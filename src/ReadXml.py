#-*- coding:utf-8 -*-

import xml.etree.ElementTree as ET #xml的解析库

xmlfile_name = r'.\\conf\\config.xml'

def readxml(filename = xmlfile_name):
    tree = ET.parse(filename)        # 加载并且解析xml文件,tree为根节点.
    prames = tree.findall('prames')  # 找到所有名为‘prames’的tag，返回一个Element对象列表。
    # print (prames)
    dict = {}
    for prame in prames:
        for item in prame:
            if item.tag == 'prame':
                Item = item.attrib.get('Item', '')
                data = item.attrib.get('data', '')
                dict[Item] = data
    # print (dict)
    return dict

if __name__ == '__main__':

    readxml(xmlfile_name)