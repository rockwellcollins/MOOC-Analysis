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

import multiprocessing as mp

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
    # warning: this is tooooooo slow :-(
    data = np.zeros((1,41))
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

#tmp = np.zeros((1,41))
#for file_name in os.listdir(ROOT_PATH + FILE_PATH):
#    if file_name[0] == "0":
#        print(file_name)
#        file_path = ROOT_PATH + FILE_PATH + file_name
#        data_tmp = log_file_parse(file_path)
#        tmp = np.vstack((tmp, data_tmp))

def parse_line(line):
    line_split = line.replace('\x01',',').strip("\n").split(",")
    return line_split

def log_parse_fast(file_path):
    """
    a fast alternative with multi-thread processing
    """
    f = open(file_path, "r",encoding="utf8")
    
    pool = mp.Pool(processes=7) # depends on you
    res_fast = [pool.apply_async(parse_line, line) for line in f.readlines()]
    
    data = np.zeros((1,41))
    for res_line in res_fast:
        data = np.vstack((data, res_line.get()))
    f.close()
    return data[1:,]

for file_name in os.listdir(ROOT_PATH + FILE_PATH):
    if file_name[0] == "0":
        print(file_name)
        file_path = ROOT_PATH + FILE_PATH + file_name
        data_tmp = log_parse_fast(file_path)