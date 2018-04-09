# -*- coding: utf-8 -*-
"""
Created on Sun Apr  8 22:50:46 2018

@author: kgicmd
"""

ROOT_PATH = "D:\\shx\\"
FILE_PATH = "wda_mooc\\log.csv"

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('ggplot')

def load_log_data(file_name):
    data = pd.read_csv(file_name,encoding='utf8',low_memory=False)
    return data

def diff_time(data):
    """
    difference log_time of log data
    """
    data.sort_values(['uid','logtime'], inplace=True)
    data['diffs'] = log_data_sel['logtime'].diff()
    # mask data w/o other usrs
    mask = data.uid != data.uid.shift(1)
    data['diffs'][mask] = np.nan
    
    return data


if __name__ == "__main__":
    log_data = load_log_data(ROOT_PATH + FILE_PATH)
    
    log_data_sel = log_data[["logtime","uid","url"]]

    log_data_diff = diff_time(log_data_sel)
    
    log_data_diff.to_csv(ROOT_PATH + "log_diff.csv", encoding="utf8")