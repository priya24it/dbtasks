import pandas as pd
import pandas.io.sql as SQL
import SQLConnection as con
import SQLConnectionQA as conQA
import datetime


RawFrame = pd.DataFrame()
TableCount = []
LoopVariable = ''
QueryList1 = []
AddValues = []
add =''
l1 = []
str1 = ''
SQLStartQuery = ''
numberofRows = ''
writer =pd.ExcelWriter("Res10.xlsx")

def ReadExcel(TestcaseExcelName,ProcessIDSheetName):
    ProcessID = pd.read_excel(TestcaseExcelName, sheet_name=ProcessIDSheetName)
    ProcessID = pd.DataFrame(ProcessID)
    return ProcessID

def MaxProcessID(sqlQuery,max):
    ProcessIDs = SQL.read_sql(sqlQuery, con.conn)
    ProcessIDs = pd.DataFrame(ProcessIDs)
    ProcessIDs = ProcessIDs['processid'].values.tolist()
    processid = ''
    if max == 1:
        processid = ProcessIDs[0]
    elif max == 2:
        processid = ProcessIDs[1]
    return processid



def FindingCount(CountofLoop,RawFrame,maxProcessID,MDMRawTable):
    #print('current data frame')
    #print(RawFrame['SQLQuery'])
    #print(maxProcessID)

    for i in range(CountofLoop):
       Count = con.conn.cursor()
       CountofEachTable = Count.execute(RawFrame['SQLQuery'][i]+" and processid in ("+maxProcessID+")")
      # CountofEachTable = Count.execute('select count(distinct mdmid) from map.contact_main where 1=1')
       Query = RawFrame['SQLQuery'][i]+" and processid in ("+maxProcessID+")"
       print(Query)
       for TableCount1 in CountofEachTable:
           QueryList1.insert(i,Query)
           TableCount.insert(i,TableCount1[0])

    RawFrame["DynamicQuery"] = pd.DataFrame(QueryList1)
    RawFrame["Count"] = pd.DataFrame(TableCount)
    RawFrame.to_excel(writer,MDMRawTable)
    #print(RawFrame)
    writer.save()
       #TableCount.clear()

def differentinCount(TableCount,RawSheetName,MapSheetName):
    dfexcelRaw = pd.read_excel("Res10.xlsx",sheet_name=RawSheetName)
    df = pd.DataFrame(dfexcelRaw)
    df = df[df.SQLQuery =='select count(*) from crm.contactid_stg where 1=1 ']
    AddValues = df['Count'].values.tolist()

    for i in range(TableCount):
        AddValues.append(AddValues[0])

    dfexcel = pd.read_excel("Res10.xlsx", sheet_name=MapSheetName)
    dfTarget = pd.DataFrame(dfexcel)
    for i in range(TableCount):
        dfTarget['TargetCount'] = pd.DataFrame(AddValues)
        dfTarget.to_excel(writer, sheet_name=MapSheetName)

    writer.save()

    dfTarget['Differnce'] = dfTarget['Count'] - dfTarget['TargetCount']
    dfTarget['Match?'] = dfTarget['TargetCount'] == dfTarget['Count']
    dfTarget.to_excel(writer, sheet_name=MapSheetName)
    writer.save()


def applyStyle(MapSheetName):
    dfMapExcel = pd.read_excel("Res10.xlsx", sheet_name=MapSheetName)
    dfStyles = pd.DataFrame(dfMapExcel)
    #dfStyles.style.applymap()
    styled = (dfStyles.style
              .applymap(lambda v: 'background-color: %s' % 'red' if v == False else ''))
    #styled.to_excel('Res10.xlsx', engine='openpyxl')
    styled.to_excel(writer, sheet_name=MapSheetName)
    writer.save()


def insertQuery(InsertDataFrame,tablename):
    str1 = ""
    i = 0
    print(InsertDataFrame.shape)
    numberofRows = list(InsertDataFrame.shape)
    print(numberofRows)
    print("Total number of rows",numberofRows[0])

    InsertDataFrame.columns = InsertDataFrame.columns.str.lower()
    print(InsertDataFrame.columns)

    ColumnHeaders = InsertDataFrame.columns.values.tolist()
    print(ColumnHeaders)
    print(len(ColumnHeaders))

    for j in range(0,numberofRows[0]):
        for i in range(0, len(ColumnHeaders)):
            str1 = InsertDataFrame[ColumnHeaders[i]][j]
            # print(str1)
            if 'mdmcreateddate' in ColumnHeaders[i]:
                TimeStamp = datetime.datetime.strftime(datetime.datetime.now(), "%Y%m%d")
                l1.insert(i, TimeStamp)
            elif 'processid' in ColumnHeaders[i]:
                processID = datetime.datetime.strftime(datetime.datetime.now(), "%Y%m%d%H%M%S")
                l1.insert(i, processID)
            else:
                l1.insert(i, str1)
            print(l1)

        listofvalues = str(l1)
        listofvalues = listofvalues.replace('[','')
        listofvalues = listofvalues.replace(']', '')
        print(listofvalues)

        ListofColumnNames = str(ColumnHeaders)
        ListofColumnNames = ListofColumnNames.replace('[', '')
        ListofColumnNames = ListofColumnNames.replace(']', '')
        ListofColumnNames = ListofColumnNames.replace("'", '')

        SQLStartQuery = 'insert into ' + tablename +' (' +ListofColumnNames+') values (' +listofvalues+ ");"
        print(SQLStartQuery)
       # conQA.conn.open()
        pd.io.sql.execute(SQLStartQuery, conQA.conn)
        conQA.conn.commit()
        l1.clear()
        #conQA.conn.close()
    #pd.io.sql.execute(SQLStartQuery, con.conn)
    #con.conn.commit()
    #con.conn.close()

def Pass1(InsertDataFrame):
    str1 = ""
    i=0
    InsertDataFrame.columns = InsertDataFrame.columns.str.lower()
    print(InsertDataFrame.columns)
   # str1 = InsertDataFrame['mdmid'].map(str) + ',' + InsertDataFrame['sourcecode'].map(str)
    #print(str1)
    ColumnHeaders = InsertDataFrame.columns.values.tolist()
    print(ColumnHeaders)
    for i in range(0,10):
        str1 = InsertDataFrame[ColumnHeaders[i]][1]
        #print(str1)
        if 'mdmcreateddate'  in ColumnHeaders[i]:
            TimeStamp = datetime.datetime.strftime(datetime.datetime.now(), "%Y%m%d")
            l1.insert(i, TimeStamp)
        else:
            l1.insert(i, str1)
    print(l1)









