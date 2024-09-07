import pandas as pd
import numpy as np
S1 = pd.Series([17,30,7150,25000],index = ["GC","PC","TS","Fees"])
S2 = pd.Series([6,np.NaN,726,33000],index = ["GC","PC","TS","Fees"])
S3 = pd.Series([np.NaN,1,100,27000],index = ["GC","PC","TS","Fees"])
S4 = pd.Series([22,24,46,23000],index = ["GC","PC","TS","Fees"])
S5 = pd.Series([7,np.NaN,673,15000],index = ["GC","PC","TS","Fees"])
DF = pd.DataFrame({"AP":S1,"Assam":S2,"Sikkim":S3,"TN":S4,"AIIMS":S5})
print(type(DF))
print(vars(DF))
DF["Fees"] = DF["Fees"] + (5/100) * DF["Fees"]
print(DF["Fees"])
