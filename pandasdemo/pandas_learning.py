import pandas as pd
import numpy as np

### Series
t = pd.Series([1, 2, 31, 2, 7])
print(t)
print(type(t))
print("*"*50)

t1 = pd.Series([1, 2, 31, 2, 7], index=list("abcde"))
print(t1)
print("*"*25)
t2 = t1.astype(float)
print(t2)
print("*"*25)
print(t1[t1>5])
print("*"*50)

tmp_dict = {"name": "Peter", "age": 23, "tel": 110}
t3 = pd.Series(tmp_dict)
print(t3)
print("*"*25)
print(t3.index)
print(t3.values)
print("*"*25)
print(t3[[0,2]])
print("*"*25)
print(t3[["age", "name"]])
print("*"*100)


### DataFrame
t4 = pd.DataFrame(np.arange(12).reshape(3,4))
print(t4)
print("*"*50)
t5 = pd.DataFrame(np.arange(6).reshape(2,3), index=list("xy"), columns=list("ABC"))
print(t5)
print("*"*50)

d1 = {"name": ["Qiqi", "Victor"], "age": [12, 24], "tel": [119, 112]}
t6 = pd.DataFrame(d1)
print(t6)
print("*"*25)
print(t6.dtypes)
print("*"*50)
d2 = {"name": "Lilei", "age": 44}
ListDict = [tmp_dict, d2]
t7 = pd.DataFrame(ListDict)
print(t7)
print("*"*50)