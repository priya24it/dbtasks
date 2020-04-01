import pyodbc
import pandas as pd
import numpy as np
#CANATHSTDEVDB12\SQL5;
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=CANATHSTUATDB21\SQL5;'  # CANATHSTUATDB21\SQL5
                      'Database=MDM_UAT;'
                      )

