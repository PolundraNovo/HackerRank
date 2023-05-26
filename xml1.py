# Task: https://www.hackerrank.com/challenges/xml-1-find-the-score/problem?isFullScreen=true

import sys
import xml.etree.ElementTree as etree

def get_attr_number(node):
    # your code goes here
    res = 0
    for item in node.iter():
        if  item.attrib !={}:         
#            print(item.attrib, len(item.attrib))
            res += len(item.attrib)
#            attr_dict.update(item.attrib)
#    print(attr_dict)
    return res

    
if __name__ == '__main__':
    sys.stdin.readline()
    xml = sys.stdin.read()
    tree = etree.ElementTree(etree.fromstring(xml))
#    tree = etree.parse('test.xml')
    root = tree.getroot()
    print(get_attr_number(root))

