#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 10 09:46:44 2021

@author: mac
"""
import openpyxl
import pandas as pd
import xlrd
import csv

import os
fname="温州代理商出货数据0805"

excel_reader=pd.ExcelFile('input/'+fname+'.xlsx')  # 指定文件
sheet_names = excel_reader.sheet_names  # 读取文件的所有表单名，得到列表
#df_data =  excel_reader.parse(sheet_name=sheet_names[i])  # 读取表单的内容，i是表单名的索引，等价于pd.read_excel('文件.xlsx', sheet_name=sheet_names[i])

fo=open('input/'+fname+'.csv')
fo.name
ls=[]
for line in fo:
    line = line.replace("\n","")
    ls.append(line.split(","))

fo.close()

ls.insert()

backname=''

newname =fname+backname  #new file name

f=open('output/'+newname+'.csv','w')
for item in ls:
    f.write(','.join(item)+'\n')

f.close()


def csv_to_xlsx_pd():# csv to xls
    csv = pd.read_csv('output/'+newname+'.csv', encoding='utf-8')
    csv.to_excel('output/'+newname+'.xlsx',sheet_name=sheet_names[0],index=None)


if __name__ == '__main__':
    csv_to_xlsx_pd()


