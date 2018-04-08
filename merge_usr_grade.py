# -*- coding: utf-8 -*-
"""
Created on Sat Apr  7 23:43:17 2018

@author: kgicmd
"""

ROOT_PATH = "D:\\shx\\"
USR_FILE_PATH = "user_tag_value\\data_all.csv"
SCORE_FILE_PATH = "moc_term_score_summary\\moc_term_grade_summary.csv"
import os
os.chdir(ROOT_PATH)

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('ggplot')

def merge_usr_grade(usr_data, grade_data):
    """
    merge user and grade data
    """
    course_id_list = np.unique(usr_data["course_id"])
    for course_id in course_id_list:
        usr_data_slice = usr_data[usr_data["course_id"] == course_id]
        grade_data_slice = grade_data[grade_data["course_id"] == course_id]
        # merge two dataframes
        df_new = pd.merge(usr_data_slice, grade_data_slice, how='left',on=["user_id"])
        
        df_new.to_csv("merged_" + str(course_id) + ".csv")
    
    return 0
    
def load_data(file_name):
    data = pd.read_csv(file_name,encoding='utf8')
    return data

if __name__ == "__main__":
    usr_data = load_data(ROOT_PATH + USR_FILE_PATH)
    grade_data = load_data(ROOT_PATH + SCORE_FILE_PATH)
    
    merge_usr_grade(usr_data, grade_data)