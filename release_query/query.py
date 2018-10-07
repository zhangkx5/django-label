import xlrd
import pandas as pd
import json
from blog import models

def open_and_query_excel(request):
    f = open("./label_files/datas.json")
    datas = json.load(f)
    object = datas['allObjects']
    # for i in object:
    #     print(i['label'])
    # print(object)
    f.close()

    # df = pd.read_excel("./label_files/release.xlsx", usecols=[0, 1, 2, 12])
    # index = df.index.tolist()
    # print(index)
    # nrows = len(df)
    # rows = []
    # for i in range(0, nrows):
    #     row = list(df.ix[i])
    #     flag = 0
    #     for obj in object:
    #         if str(row[3]) == str(obj['label']):
    #             flag = 1
    #             break
    #     if flag == 0:
    #         rows.append(row)
    return object