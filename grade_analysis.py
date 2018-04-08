#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 22 14:02:41 2018

@author: kgicmd
"""

ROOT_PATH = "D:\\shx\\"
FILE_PATH = "moc_term_score_summary\\"
import os
os.chdir(ROOT_PATH)

import codecs
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('ggplot')

# statistics for users
os.chdir(ROOT_PATH + FILE_PATH)

f = open("000000_0","r")
line = f.readline()
print(line)
f.close()


def test_score_parse(file_path):
    """
    parse files of users testing information
    """
    data = np.zeros((1,20))
    f = open(file_path, "r",encoding="utf8")
    for line in f.readlines():
        line_split = line.strip("\n").split("\x01")
        try:
            data = np.vstack((data, line_split))
        except ValueError:
            print("check this:")
            print(line_split)
    f.close()
    data = data[1:,]
    
    return data

for file_name in os.listdir(ROOT_PATH + FILE_PATH):
    if file_name[0] == "0":
        file_path = ROOT_PATH + FILE_PATH + file_name
        data_tmp = test_score_parse(file_path)
        
data_tmp = pd.DataFrame(data_tmp)

data_tmp.columns = ["id",
                    "gmt_create",
                    "gmt_modified",
                    "course_id",
                    "user_id",
                    "test_score",
                    "assignment_score",
                    "exam_score",
                    "discuss_score",
                    "outside_score",
                    "total_score",
                    "tc_uptime",
                    "bonus_score",
                    "total_score_plus_bonus",
                    "cert_send_status",
                    "chargecert_mark",
                    "charge_cert_send_status",
                    "count_reply",
                    "count_vote",
                    "time" # I don't know what this is, check w/ admin
                    ]

data_tmp.to_csv("moc_term_grade_summary.csv", encoding = "utf8")