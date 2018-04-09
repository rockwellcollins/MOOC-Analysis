# -*- coding: utf-8 -*-
"""
Created on Tue Apr  3 22:05:24 2018

@author: kgicmd
"""

ROOT_PATH = "D:\\shx\\"
FILE_PATH = "wda_mooc\\"
import os
os.chdir(ROOT_PATH)

import codecs
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('ggplot')
import datetime
from time import time

# statistics for users
os.chdir(ROOT_PATH + FILE_PATH)

#f = open("000000_0", "r")
#line = f.readline()
#print(line)
#f.close()


def log_file_parse(file_path):
    """
    parse files for users information
    """
    data = []
    f = open(file_path, "r",encoding="utf8")
    
    for line in f.readlines():
        line_split = line.replace('\x01',',').strip("\n").split(",")
        data.append(line_split)
    f.close()
    
    return data


if __name__ == "__main__":
    start = time()
    start_time = datetime.datetime.fromtimestamp(start).strftime('%Y-%m-%d %H:%M:%S')
    print("#"*20)
    print(start_time)
    for file_name in os.listdir(ROOT_PATH + FILE_PATH):
        if file_name[0] == "0":
            print(file_name)
            file_path = ROOT_PATH + FILE_PATH + file_name
            data_tmp = log_file_parse(file_path)
            data_tmp_df = pd.DataFrame(data_tmp)
            data_tmp_df.columns = ["logtime",
                                   "login_type",
                                   "filter",
                                   "version",
                                   "session_seq",
                                   "hostname",
                                   "character_set",
                                   "screen_resolution",
                                   "screen_color",
                                   "language",
                                   "flash_version",
                                   "refer",
                                   "url",
                                   "os",
                                   "browser",
                                   "browser_version",
                                   "uid",
                                   "sid",
                                   "first_session",
                                   "last_session",
                                   "current_session",
                                   "ip",
                                   "region",
                                   "event_category",
                                   "event_operation",
                                   "event_label",
                                   "daily_newuser",
                                   "hourly_newuser",
                                   "search_keyword",
                                   "search_engine",
                                   "referral",
                                   "source",
                                   "medium",
                                   "utm_source",
                                   "utm_medium",
                                   "utm_campaign",
                                   "custom_data",
                                   "dt",
                                   "type",
                                   "url",
                                   "refer",
                                   "idk"]
            data_tmp_df.to_csv("log.csv", encoding = "utf8")
            #data_to_csv(data_tmp, ROOT_PATH + FILE_PATH)
    end = time()
    end_time = datetime.datetime.fromtimestamp(end).strftime('%Y-%m-%d %H:%M:%S')
    print("#"*20)
    print(end_time)