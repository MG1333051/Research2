#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
这个程序的目的是从scipy.csv中提取出label中含有defect关键字且patch不是空的  issuseID和patch的地址，
用来人工审核在bug修复的代码行中使用了动态特性patch文件
'''

import csv
import re
import logging

with open('E:/Research 2/dynamic features and bugs/numpy/bugs/IssueSummary/data/scipy/scipy.csv','r') as f:
      with open('E:/Research 2/dynamic features and bugs/numpy/bugs/IssueSummary/data/scipy/scip_new.csv', 'w') as g:
         
          reader = csv.reader(f) 
          writer =csv.writer(g)   
#           writer.writerow( ["number","id","reporter", "created_at",
#                                 "updated_at","closed_at","state","locked","assignee","milestone","comments",
#                                 "label_name","title","pull_request","user","labels",
#                                 "html_url","labels_url","url","events_url","diff",
#                                 "patch","comments_url","body" ] )
          writer.writerow( ["number","patch" ] )
          for line in reader:
              if ("defect"  in line[11]) and line[13] != None:     
                  print line[0], "    ", line[21],'\n'               
                  writer.writerow([line[0],line[21]])
                    


