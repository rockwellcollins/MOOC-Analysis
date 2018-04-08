#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 22 12:48:56 2018

@author: kgicmd
"""

ROOT_PATH = "D:\\shx\\"
FILE_PATH = "user_tag_value\\"
import os
os.chdir(ROOT_PATH)

import codecs
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('ggplot')

# statistics for users
os.chdir(ROOT_PATH + FILE_PATH)

#f = open("000021_0", "r")
#line = f.readline()
#print(line)
#f.close()


def user_file_parse(file_path):
    """
    parse files for users information
    """
    data = np.zeros((1,13))
    f = open(file_path, "r",encoding="utf8")
    for line in f.readlines():
        line_split = line.replace('\x01',',').strip("\n").split(",")
        try:
            data = np.vstack((data, line_split))
        except ValueError:
            print("check this:")
            print(line_split)
    f.close()
    data = data[1:,]
    
    return data

tmp = np.zeros((1,13))
for file_name in os.listdir(ROOT_PATH + FILE_PATH):
    if file_name[0] == "0":
        print(file_name)
        file_path = ROOT_PATH + FILE_PATH + file_name
        data_tmp = user_file_parse(file_path)
        tmp = np.vstack((tmp, data_tmp))

tmp = tmp[1:,]
data_all = pd.DataFrame(tmp)
data_all.columns = ["user_id",
                    "user_nickname",
                    "email",
                    "birthday",
                    "gender",
                    "country",
                    "province",
                    "city",
                    "sign_up_since", # I'm not quite sure what exactly this means
                    "last_login_time",
                    "term_id",
                    "course_id",
                    "enroll_time"]

# split overall data according to course_id
course_id_list = np.unique(data_all["course_id"])
for course_id in course_id_list:
    data_slice = data_all[data_all["course_id"] == course_id]
    name = "users_of_" + str(course_id) + ".csv"
    data_slice.to_csv(name,encoding = "utf8")
    
data_all = data_all.drop_duplicates()
data_all.to_csv("data_all.csv",encoding = "utf8")