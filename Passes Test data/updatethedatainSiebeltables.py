import function as f
import pandas as pd
import ibm_db
import ibm_db_dbi
import datetime


TestcaseExcelName = 'CRMTables1.xlsx'
sheetname = ['siebel.s_contact','siebel.s_contact_x','siebel.s_party_per','siebel.s_org_ext','siebel.s_org_ext_xm']


l1 = []
con = ibm_db.connect("DATABASE=bigsql;HOSTNAME=CANATBIMQA004;PORT=32051;PROTOCOL=TCPIP;UID=CA_SC_EDH_HDPQA;PWD=YD0uW@nt2Bother;", "", "")
conn = ibm_db_dbi.Connection(con)

index = 0
for index in range(0,len(sheetname)):
    DataFrame = pd.read_excel(TestcaseExcelName,sheet_name = sheetname[index])
    print(sheetname[index])
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
    print(ColumnHeaders)
    print(len(ColumnHeaders))

    if "_by" in ColumnHeaders:
        print("Yes, 'apple' is in the fruits list")

    for j in range(0, numberofRows[0]):
        for i in range(0, len(ColumnHeaders)):
            str1 = InsertDataFrame[ColumnHeaders[i]][j]
            # print(str1)
            if 'batch_id' in ColumnHeaders[i]:
                TimeStamp = datetime.datetime.strftime(datetime.datetime.now(), "%Y%m%d%H%M%S")
                l1.insert(i, TimeStamp)
            elif 'created' in ColumnHeaders[i]:
                created = str(datetime.datetime.strftime(datetime.datetime.now(), "%Y%m%d"))
                l1.insert(i, created)
            elif 'last_upd' in ColumnHeaders[i]:
                lastupd = str(datetime.datetime.strftime(datetime.datetime.now(), "%Y%m%d"))
                l1.insert(i, lastupd)
            elif '_by' in ColumnHeaders[i]:
                by = "priya"
                l1.insert(i, by)
            else:
                l1.insert(i, str1)
            #print(l1)

        listofvalues = str(l1)
        listofvalues = listofvalues.replace('[', '')
        listofvalues = listofvalues.replace(']', '')
        listofvalues = listofvalues.replace('nan', 'Null')
        #print(listofvalues)

        ListofColumnNames = str(ColumnHeaders)
        ListofColumnNames = ListofColumnNames.replace('[', '')
        ListofColumnNames = ListofColumnNames.replace(']', '')
        ListofColumnNames = ListofColumnNames.replace("'", '')
        ##print(ListofColumnNames)
        #SQLStartQuery = 'insert into ' + sheetname[index] + ' (' + ListofColumnNames + ')'

        SQLStartQuery = 'insert into ' + sheetname[index] + ' (' + ListofColumnNames + ') values (' + listofvalues + ");"
        print(SQLStartQuery)
        pd.io.sql.execute(SQLStartQuery, conn)
        conn.commit()
        l1.clear()

conn.close()

