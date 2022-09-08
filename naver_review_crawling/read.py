
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
print(hole.shape) 
# for i in text:
#     l = [0 for j in range(2500)]

# df_output = pd.DataFrame()

# for i in range(len(text)):
#     df_output[i] = pd.Series(text[i])
# df_output.to_excel('./output.xlsx')

# py = np.array()