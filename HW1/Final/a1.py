# -*- coding: utf-8 -*-
"""
Created on Sat Sep 28 11:20:10 2019

@author: fghjk
"""
import numpy as np
import math
def five_x_cubed_plus_2(x):
    return math.pow(x,3)*5+2
def triple_up(listx):
    listx.reverse()
    result=[]
    while(len(listx)>2):
        templist=[]
        for x in range (1,4):  
            templist.append(listx.pop())
            result.append(templist)
    templist=[]
    for x in range (len(listx)):
        templist.append(listx.pop())
    result.append(templist)
    return result
def mystery_code(x):
    cl=[]
    dicttest = {
            "a": "V",
            "b": "W",
            "c": "X",
            "d": "Y",
            "e": "Z",
            "f": "A",
            "g":"B",
            "h":"C",
            "i":"D",
            "j":"E",
            "k":"F",
            "l":"G",
            "m":"H",
            "n":"I",
            "o":"J",
            "p":"K",
            "q":"L",
            "r":"M",
            "s":"N",
            "t":"O",
            "u":"P",
            "v":"Q",
            "w":"R",
            "x":"S",
            "y":"T",
            "z":"U",
            "A": "v",
            "B": "w",
            "C": "x",
            "D": "y",
            "E": "z",
            "F": "a",
            "G":"b",
            "H":"c",
            "I":"d",
            "J":"e",
            "K":"f",
            "L":"g",
            "M":"h",
            "N":"i",
            "O":"j",
            "P":"k",
            "Q":"l",
            "R":"m",
            "S":"n",
            "T":"o",
            "U":"p",
            "V":"q",
            "W":"r",
            "X":"s",
            "Y":"t",
            "Z":"u",
            }
    for ele in x:
        if dicttest.get(ele)!=None :
            cl.append(dicttest.get(ele))
        else:
            cl.append(ele)
    result=''.join(str(e) for e in cl)
    return result
def future_tense(x):
    result=[]
    dit={'Today':'Tommorrow',
         'Yestaurday':'Tommorrow',
         'today':'tommorrow',
         'Now':'Tommorrow',
         'now':'tommorrow',
         'yestaurday':'tommorrow',
         
         }
    vdit={'ate':'eat',
         'did':'do',
         'does':'do',
         'is':'be',
         'are':'be',
         'am' :'be',
         'was':'be',
         'were':'be',
         'went':'go',
         'had':'have',
         'has':'have',
}
    for ele in x:
        if dit.get(ele)!=None:
            result.append(dit.get(ele))
        if vdit.get(ele)!=None:
            result.append('will')
            result.append(vdit.get(ele))
        else:
            result.append(ele)
    return result

