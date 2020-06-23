import numpy as np

#np.random.seed(10)   #随机种子
t = np.random.randint(0,20,(3,4))
print(t)

#创建d0-dn维度的均匀分布的随机数组，浮点数，范围从0-1
t1 = np.random.rand(2,2)
print(t1)

#创建d0-dn维度的标准正态分布随机数，浮点数，平均数0，标准差1
t2 = np.random.randn(4,5)
print(t2)

#产生具有均匀分布的数组
t3 = np.random.uniform(0,20,(3,4))
print(t3)

#从指定正态分布中随机抽取样本，分布中心是loc（概率分布的均值），标准差是scale
t4 = np.random.normal(14,3,(2,3))
print(t4)
print("*"*100)

t5 = np.arange(6).reshape(2,3)
t5[[0,1],:] = t5[[1,0],:]   # 行交换
print(t5)
t6 = np.arange(6,12).reshape(2,3)
t6[:,[1,2]] = t6[:,[2,1]]    # 列交换
print(t6)
print("*"*50)
t7 = np.vstack((t5,t6))
print(t7)
print("*"*25)
t8 = np.hstack((t5,t6))
print(t8)
print("*"*50)

print(np.argmax(t7, axis=0))    #显示的是位置，而不是值
print(np.argmin(t8, axis=1))
print("*"*50)

p = np.tile(np.arange(0, 10, 2), (5, 1))
print(p)
print("*"*50)
value_sum = p.sum(axis=0)
print(value_sum)
value_mean = p.mean(axis=1)
print(value_mean)
value_median = np.median(p, axis=1)
print(value_median)
print(p.max(axis=0))
print(p.min(axis=1))
value_p = np.ptp(p, axis=1)
print(value_p)
value_std = p.std(axis=1)
print(value_std)
print("*"*50)

q1 = p<4
q2 = p[p<4]
print(q1)
print(q2)
print("*"*50)

r = np.where(p<4, 0, 1)
print(r)
print("*"*50)

s = np.clip(p, 2, 6)
print(s)


