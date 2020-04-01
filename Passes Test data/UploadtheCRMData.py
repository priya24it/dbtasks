import SQLConnection as con
import pandas as pd
import pandas.io.sql as SQL

excelWriter = pd.ExcelWriter('CRMTables1.xlsx')

TablesData = pd.read_excel('Listofnewtables.xlsx')
TablesData = pd.DataFrame(TablesData)
ListofTableNames = TablesData['TableNames'].values.tolist()
CountofTables = len(TablesData['SQLQuery'].values.tolist())


'''ListofIDs = pd.read_excel('Listofnewtables.xlsx')
ListofIDs = pd.DataFrame(ListofIDs)
ListofIDs = ListofIDs['ID'].values.tolist()
ListofIDs = str(ListofIDs)
ListofIDs = ListofIDs.replace('[','')
ListofIDs = ListofIDs.replace(']','') '''

print(CountofTables)
#i= 0
for i in range(CountofTables):
    print(i)
    sql =TablesData['SQLQuery'][i]
    #sql = TablesData[i]+' and grid in ('+ListofIDs+')'
    print(sql)
    f= open('sql.txt','a')
    f.write(str(sql))
    dfMainExcel = SQL.read_sql(sql,con.conn)
    dfMain = pd.DataFrame(dfMainExcel)
    print(dfMain)
    dfMain.to_excel(excelWriter, sheet_name=ListofTableNames[i])

f.close()
excelWriter.save()



