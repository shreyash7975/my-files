#!/usr/bin/python3
import xlrd
import numpy as np
import matplotlib.pyplot as plt
file_location = "cl124/Desktop/file.xlsx"
workbook = xlrd.open_workbook(file_location)
first_sheet = workbook.sheet_by_index(0)
for col in range(first_sheet.ncols):
    x = first_sheet.cell_value(0,col)
    y = first_sheet.cell_value(1,col)
    yerr = first_sheet.cell_value(2,col)
plt.errorbar(x,y,yerr,fmt='r^')
plt.show()