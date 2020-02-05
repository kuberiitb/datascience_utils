import pandas as pd
import numpy as np

dtypesDict = trainData.dtypes.to_dict()
dtypesList = {}
for col, t in dtypesDict.items():
        if t not in dtypesList:
            dtypesList[t] = [col]
        else:
            dtypesList[t].append(col)
