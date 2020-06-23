import numpy as np

def fill_ndarray(t):
    for i in range(t.shape[1]):
        tmp_col = t[:, i]
        nan_num = np.count_nonzero(tmp_col != tmp_col)
        if nan_num != 0:
            # 两种方式找nan， !=和isnan
            tmp_not_nan_col = tmp_col[tmp_col == tmp_col]
            tmp_col[np.isnan(tmp_col)] = tmp_not_nan_col.mean()

    return t

if __name__== '__main__':
    p = np.nan
    print(p == p)
    print("*"*50)
    t = np.arange(12).reshape(3, 4).astype(float)
    t[1, 2:] = np.nan
    print(t)
    print("*" * 50)
    t1 = fill_ndarray(t)
    print(t1)