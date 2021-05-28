#! /usr/bin/env python3
# -*- coding: utf-8 -*-


import pandas as pd


#TODO:ここでtdのループ

sheet = []
row = []






for i in range(len(td)):

    if i <= 6:
        continue

    row.append(td[i].text)

    if i%7 == 6:
        sheet.append(row)
        row = []


data    = pd.DataFrame(sheet)

