import SQLConnection as con
import pandas as pd
import pandas.io.sql as SQL

excelWriter = pd.ExcelWriter('MDMBusinessData.xlsx')

TablesData = pd.read_excel('MDMBackupTables.xlsx',sheet_name='MDMBusinessTables')
TablesData = pd.DataFrame(TablesData)
ListofTableNames = TablesData['TableNames'].values.tolist()
CountofTables = len(TablesData['SQLQuery'].values.tolist())


ListofIDs = pd.read_excel('MDMBackupTables.xlsx',sheet_name='ListofIDs')
ListofIDs = pd.DataFrame(ListofIDs)
ListofIDs = ListofIDs['ID'].values.tolist()
ListofIDs = str(ListofIDs)
ListofIDs = ListofIDs.replace('[','')
ListofIDs = ListofIDs.replace(']','')

print(CountofTables)
#i= 0
for i in range(CountofTables):
    print(i)
    sql =TablesData['SQLQuery'][i] + ' and grid in ('+ListofIDs+')'
    #sql = TablesData[i]+' and grid in ('+ListofIDs+')'
    print(sql)
    f= open('sql.txt','a')
    f.write(str(sql))
    dfMainExcel = SQL.read_sql(sql,con.conn)
    dfMain = pd.DataFrame(dfMainExcel)
    print(dfMain)
    dfMain.to_excel(excelWriter, sheet_name=ListofTableNames[i])
    workbook = excelWriter.book
    worksheet = excelWriter.sheets[ListofTableNames[i]]

    format = workbook.add_format({'text_wrap': True})
    # Setting the format but not setting the column width.
    worksheet.set_column('C:C', 15, format)
    worksheet.set_column('D:D', 15, format)
    worksheet.set_column('E:E', 20, format)
    worksheet.set_column('F:F', 20, format)
    worksheet.set_column('G:G', 20, format)
    worksheet.set_column('H:H', 20, format)
    worksheet.set_column('I:I', 15, format)
    worksheet.set_column('A:A', 15, format)
    worksheet.set_column('B:B', 20, format)
    worksheet.set_column('J:J', 15, format)
    worksheet.set_column('K:K', 15, format)
    worksheet.set_column('L:L', 15, format)
    worksheet.set_column('M:M', 15, format)
    worksheet.set_column('N:N', 15, format)
    worksheet.set_column('O:O', 15, format)
    worksheet.set_column('P:P', 15, format)
    worksheet.set_column('Q:Q', 15, format)
    worksheet.set_column('R:R', 15, format)
    worksheet.set_column('S:S', 15, format)
    worksheet.set_column('T:T', 15, format)


f.close()
excelWriter.save()






