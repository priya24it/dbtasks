import function as f

ID = f.ReadExcel("ins.xlsx" , "mdmid")
print(ID)
mdmid = ID['mdmid'].values.tolist()
mdmid = str(mdmid)
#mdmid = ','.join(mdmid)
mdmid = mdmid.replace(']','')
mdmid = mdmid.replace('[','')
print(mdmid)