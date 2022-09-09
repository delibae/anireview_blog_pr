
import pandas as pd
import numpy as np

df_new = pd.read_pickle("./naver_review_crawling/75data_1.pkl")



name = df_new['Name'].values.tolist()
text =df_new['Review_txt'].values.tolist()
print(len(text[2]))

py = np.array(text,dtype=object)
# print(py)

hole = np.array([])

for i in text:
    t = np.array(i)
    t.reshape(-1,1)
    hole = np.append(hole, t)

hl = hole.tolist()

df = pd.DataFrame(columns=["Name","Review"])

df['Review'] = hole
print(df)

count = 0
for i in range(len(text)):
    l = len(text[i])
    if l == 0:
        pass
    else:
        df.loc[count,'Name'] = name[i]

    count += l

df.to_excel('./naver_review_crawling/excel_data/ml_data.xlsx')