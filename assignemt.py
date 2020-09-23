#!/usr/bin/env python
#task3 to pass the nested objects and key and get the same output 

def safeget(dct, mykey):
    keys=mykey.split('/')
    for key in keys:
        try:
            dct = dct[key]
        except keyerror:
            return  None
        return dct
    dct = {'x':{'y':{'z'}}}
    print(safeget(dct,'x/y/z'))
