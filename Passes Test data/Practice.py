import function as f
import pandas as pd
import ibm_db
import ibm_db_dbi
import datetime

tablename = 'eloqua.contact'
TestcaseExcelName = 'CRMTables.xlsx'
sheetname = ['siebel.s_user','siebel.s_contact','siebel.s_contact_x','siebel.s_contact_xm','siebel.s_postn_con','siebel.s_per_comm_addr','siebel.s_party_per','siebel.s_org_ext','siebel.s_org_syn','siebel.s_org_ext_x','siebel.s_org_ext_xm','siebel.s_emp_per','siebel.s_chrctr','siebel.s_call_lst','siebel.s_addr_per']


for i in  range(0,len(sheetname)):
    DataFrame = pd.read_excel(TestcaseExcelName,sheet_name = sheetname[i])
    #print(DataFrame.columns)
    InsertDataFrame = pd.DataFrame(DataFrame)
    #print(InsertDataFrame)

    #print(InsertDataFrame.shape)
    numberofRows = list(InsertDataFrame.shape)
    #print(numberofRows)
    print("Total number of rows", numberofRows[0])