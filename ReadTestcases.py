import pandas as pd
import numpy as np
import SQLConnection as sql
import pandas.io.sql
from StyleFrame import StyleFrame, Styler
import function as f

#List of Testcases
TestcaseExcelName = 'MDMTestcases.xlsx'

#Pull the excel data into DataFrame.
SheetName = 'ProcessID'
DataFrameProcessID = f.ReadExcel(TestcaseExcelName,SheetName)

#Finding the maximum processID
maxProcessID = f.MaxProcessID(str(DataFrameProcessID['SQLQuery'][0]),1)
ProcessID = "Maximum processID = {}"
print(ProcessID.format(maxProcessID))

#Finding the second highest processID
secondhighestProcessID = f.MaxProcessID(str(DataFrameProcessID['SQLQuery'][0]),2)
ProcessID = "Second Highest processID = {}"
print(ProcessID.format(secondhighestProcessID))

#Finding the Raw Table Data Source
RawSheetName = 'MDMRaw_Tables'
DataFrameProcessID = f.ReadExcel(TestcaseExcelName,RawSheetName)

#Finding the Raw Table Data Count
Tablecount = len(DataFrameProcessID['SQLQuery'].values.tolist())
f.FindingCount(Tablecount,DataFrameProcessID,maxProcessID,RawSheetName)

#Pull  the Map Table Data into Data Frame
MapSheetName = 'MDMMAP_Tables'
DataFrameProcessID = f.ReadExcel(TestcaseExcelName,MapSheetName)

#Finding the Map Table Data Count
Tablecount = len(DataFrameProcessID['SQLQuery'].values.tolist())
f.FindingCount(Tablecount,DataFrameProcessID,maxProcessID,MapSheetName)

#Specfic method for finding difference
f.differentinCount(Tablecount,RawSheetName,MapSheetName)
print('Completed')

#specfic method for apply styles
f.applyStyle(MapSheetName)



















