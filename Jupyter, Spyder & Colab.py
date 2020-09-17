# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 17:11:52 2020

@author: WFH-PC19X0VM
"""

import pandas as pd

grab = pd.read_csv("C:/Users/WFH-PC19X0VM/Desktop/Data Science Workshop/FTW4-Github-Homework-2/DataSeerGrabPrizeData.csv")

grab.describe()

grab_cleaned = grab.dropna()

grab_cleaned.to_csv("GrabDataCleaned.csv")