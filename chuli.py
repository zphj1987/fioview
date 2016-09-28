#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import os
import sys
import commands
import json
import csv
import codecs 

def main():
#版本
    fio_version=str(getjsonresult()["fio version"])
#unix时间
    unix_time=str(getjsonresult()["timestamp"])
#时间
    time=str(getjsonresult()["time"])
#读取带宽
    read_bw=str(getjsonresult()["jobs"][0]["read"]["bw"])
#读取IOPS
    read_iops=str(getjsonresult()["jobs"][0]["read"]["iops"])
#读取运行时间
    read_runtime=str(getjsonresult()["jobs"][0]["read"]["runtime"])


    print( "fio版本,%s"  %(fio_version))
    print('Unix时间,%s'  %(unix_time))            
    print('时间,%s'  %(time))
    print('Read BW,%s'  %(read_bw))
    print('Read Iops,%s'  %(read_iops))
    print('Read Runtime,%s'  %(read_bw))

    with open('fio.csv', 'wb') as csvfile:
        csvfile.write(codecs.BOM_UTF8)  
        spamwriter = csv.writer(csvfile, dialect='excel')
        spamwriter.writerow(['fio版本',fio_version])
        spamwriter.writerow(['Unix时间',unix_time])
        spamwriter.writerow(['时间',time])
        spamwriter.writerow(['Read BW',read_bw])
        spamwriter.writerow(['Read Iops',read_iops])
        spamwriter.writerow(['Read Runtime',read_runtime])



def getjsonresult():
    fioresult = commands.getoutput('cat fio.json')
    json_str = json.loads(fioresult)
    return json_str

if __name__ == '__main__':
    main()
