import numpy as np
import random

t = np.array(range(10))
print(t)
print(type(t))  # <'numpy.ndarray'>
print("*"*50)

t1 = np.array([[1,2,3],[4,5,6]])
print(t1)
print(t1.shape)
print(t1.shape[0], t1.shape[1])
print("*"*50)

t2 = t1.flatten()
print(t2)
print(t2.shape)
mt = np.reshape(t1, -1)
print(mt)
print(mt.shape)
print("*"*50)

t3 = np.arange(2,8,2)
print(t3)
print(t3.dtype)   # int64
print("*"*50)

t4 = np.array(range(13,24), dtype=float)
print(t4)
print(t4.dtype)
print("*"*50)

t5 = np.array([0, 1, 1, 0, 0], dtype=bool)
print(t5)
print(t5.dtype)
print("*"*50)

t6 = t5.astype("int8")
print(t6)
print(t6.dtype)
print("*"*50)

t7 = np.array([random.random() for i in range(5)])
print(t7)
print(t7.dtype)
print("*"*50)

t8 = np.round(t7, 2)
print(t8)
print("*"*50)

t9 = np.arange(20).reshape((4,5)).astype("float")
print(t9)
print("*"*50)

t10 = np.transpose(t9)
print(t10)
print("*"*25)
t11 = t9.T
print(t11)
print("*"*25)
t12 = np.swapaxes(t9,0,1)
print(t12)
print("*"*100)

mm = np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(mm.shape)
pp = mm.reshape((mm.shape[0],mm.shape[1],1))
print(pp.shape)
tt = np.expand_dims(mm, axis=-1)
print(tt.shape)
print("*"*50)


