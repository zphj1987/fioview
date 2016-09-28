#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import os
import sys
import commands
import json
import csv
import codecs 

def main():
    print "fio版本,%s"  %(str(getjsonresult()["fio version"]))
    print('Unix时间,%s'  %(str(getjsonresult()["timestamp"]))) 
    print('时间,%s'  %(str(getjsonresult()["time"]))) 
    read_bw=str(getjsonresult()["jobs"][0]["read"]["bw"])
    print('Read BW,%s'  %(read_bw))

    with open('fio.csv', 'wb') as csvfile:
        csvfile.write(codecs.BOM_UTF8)  
        spamwriter = csv.writer(csvfile, dialect='excel')
#        spamwriter.writerow(['fio版本']+[str(getjsonresult()["fio version"])])
        spamwriter.writerow(['fio版本',str(getjsonresult()["fio version"])])
        spamwriter.writerow(['Unix时间',str(getjsonresult()["timestamp"])])
        spamwriter.writerow(['时间',str(getjsonresult()["time"])])
        spamwriter.writerow(['Read BW',read_bw])



def getjsonresult():
    fioresult = commands.getoutput('cat fio.json')
    json_str = json.loads(fioresult)
    return json_str

if __name__ == '__main__':
    main()
