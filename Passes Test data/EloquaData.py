import function as f
import pandas as pd
import ibm_db
import ibm_db_dbi
import datetime

tablename = 'eloqua.contact'
TestcaseExcelName = 'elq.xlsx'
sheetname = 'eloqua.contact'

#tablename = 'siebel.s_emp_per'
#TestcaseExcelName = 'elq.xlsx'
#sheetname = 'crm.s_emp_per'

l1 = []
con = ibm_db.connect("DATABASE=bigsql;HOSTNAME=CANATBIMQA004;PORT=32051;PROTOCOL=TCPIP;UID=CA_SC_EDH_HDPQA;PWD=YD0uW@nt2Bother;", "", "")
conn = ibm_db_dbi.Connection(con)

#List of Testcases




DataFrame = pd.read_excel(TestcaseExcelName,sheet_name = sheetname)
#print(DataFrame.columns)
InsertDataFrame = pd.DataFrame(DataFrame)
#print(InsertDataFrame)
str1 = ""
i = 0
#print(InsertDataFrame.shape)
numberofRows = list(InsertDataFrame.shape)
#print(numberofRows)
print("Total number of rows", numberofRows[0])
InsertDataFrame.columns = InsertDataFrame.columns.str.lower()
#print(InsertDataFrame.columns)
ColumnHeaders = InsertDataFrame.columns.values.tolist()
#print(ColumnHeaders)
print(len(ColumnHeaders))
for j in range(0, numberofRows[0]):
    for i in range(0, len(ColumnHeaders)):
        str1 = InsertDataFrame[ColumnHeaders[i]][j]
        # print(str1)
        if 'batch_id' in ColumnHeaders[i]:
            TimeStamp = datetime.datetime.strftime(datetime.datetime.now(), "%Y%m%d%H%M%S")
            l1.insert(i, TimeStamp)
        elif 'processid' in ColumnHeaders[i]:
            processID = datetime.datetime.strftime(datetime.datetime.now(), "%Y%m%d%H%M%S")
            l1.insert(i, processID)
        else:
            l1.insert(i, str1)
            #print(l1)

    listofvalues = str(l1)
    listofvalues = listofvalues.replace('[', '')
    listofvalues = listofvalues.replace(']', '')
    listofvalues = listofvalues.replace('nan', 'Null')
    print(listofvalues)

    ListofColumnNames = str(ColumnHeaders)
    ListofColumnNames = ListofColumnNames.replace('[', '')
    ListofColumnNames = ListofColumnNames.replace(']', '')
    ListofColumnNames = ListofColumnNames.replace("'", '')

    SQLStartQuery = 'insert into ' + tablename + ' (' + ListofColumnNames + ') values (' + listofvalues + ");"
    print(SQLStartQuery)
    #conn.open()
    pd.io.sql.execute(SQLStartQuery, conn)
    conn.commit()
    l1.clear()
conn.close()
    # pd.io.sql.execute(SQLStartQuery, con.conn)
    # con.conn.commit()
