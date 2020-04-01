import pandas as pd
import numpy as np

sourcejobexcel= pd.read_csv('currentprocessID.csv',low_memory = 'False',dtype='unicode')
sourcejob  = pd.DataFrame(sourcejobexcel)
sourcejob = sourcejob.iloc[:300, : 5]
sourcejob.fillna(0,inplace=True)
sourcejob.columns = sourcejob.columns.str.lower()
print(sourcejob.shape) #15237
#print(sourcejob.columns)

SourceRowIDs = sourcejob['row_id'].values.tolist()

targetjobexcel= pd.read_csv('previousprocessID.csv',low_memory = 'False',dtype='unicode')
targetjob  = pd.DataFrame(targetjobexcel)
targetjob = targetjob.iloc[:300, : 5]
targetjob.fillna(0,inplace=True)
targetjob.columns = targetjob.columns.str.lower()
print(targetjob.shape)  #17868

TargetRowIDs = targetjob['row_id'].values.tolist()

i = 0
l1 = []

df3 = pd.DataFrame()
for val_a in SourceRowIDs:
    if (val_a  in  TargetRowIDs):
        i = i + 1
        l1.append(val_a)

print("Number of contacts which exists in TargetRowIDs"+ str(i))

SourceComparisonData = sourcejob[sourcejob['row_id'].isin(l1)]
SourceComparisonData = SourceComparisonData.reset_index(drop=True)
SourceComparisonData = SourceComparisonData.sort_values(by=['row_id'],ascending=True)
SourceComparisonData = SourceComparisonData.reset_index(drop=True)
print(SourceComparisonData.shape)
print(SourceComparisonData)
SourceComparisonData.to_excel("Res7.xlsx")

TargetComparisonData = targetjob[targetjob['row_id'].isin(l1)]
TargetComparisonData = TargetComparisonData.reset_index(drop=True)
# TargetComparisonData.sort_values(by=['ROW_ID'],ascending=True, inplace=True)
TargetComparisonData = TargetComparisonData.sort_values(by=['row_id'],ascending=True)


print(TargetComparisonData.shape)
print(TargetComparisonData)
TargetComparisonData.to_excel("Res8.xlsx")
df4 = pd.DataFrame()

i = 1
for i,j in SourceComparisonData.iteritems():
    df4["df1"+ i] = SourceComparisonData[i]
    df4["df2" + i] = TargetComparisonData[i]
    df4[i + "Result"] =  SourceComparisonData[i] == TargetComparisonData[i]
    df4[i+"Result" ] = np.where((SourceComparisonData[i]) == TargetComparisonData[i], 'True', 'False')
df4.to_excel("Res1.xlsx")

styled = (df4.style.applymap(lambda v: 'foreground-color: %s' % 'Green' if v == False else ''))
styled.to_excel('Res12.xlsx')


def color_negative_red(val):
    """
    Takes a scalar and returns a string with
    the css property `'color: red'` for negative
    strings, black otherwise.
    """
    color = 'red' if val < 0 else 'black'
    return 'color: %s' % color


















