import function as f

#List of Testcases
TestcaseExcelName = 'Datasetup.xlsx'

SheetName = ['std.contact_main','std.contact_email','std.contact_job','std.contact_phone','std.contact_relationship','std.contact_address']

for i in range(0,len(SheetName)):
    InsertDataFrame = f.ReadExcel(TestcaseExcelName,SheetName[i])
    f.insertQuery(InsertDataFrame,SheetName[i])






