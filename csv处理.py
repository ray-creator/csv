#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 10 09:46:44 2021

@author: mac
"""
#import pandas as pd

import os

fname="温州代理商出货数据0805"

fo=open('input/'+fname+'.csv')
ls=[]
for line in fo:
    line = line.replace("\n","")
    ls.append(line.split(","))

fo.close()

backname=''

newname =fname+backname+'.csv'  #new file name

f=open('output/'+newname,'w')
for item in ls:
    f.write(','.join(item)+'\n')

f.close()


def csv_to_xlsx_pd():# csv to xls
    csv = pd.read_csv('output/'+newname, encoding='utf-8')
    csv.to_excel('1.xlsx', sheet_name='data')


# if __name__ == '__main__':
   #  csv_to_xlsx_pd()
