"""
The numpy exercises
"""

import numpy as np

# 2.a.
null_vector = np.zeros(10)
null_vector[4] = 1
print(null_vector)
print()

# 2.b.
range_vec = np.arange(10,50)
print(range_vec)
print()

# 2.c.
range_vec = range_vec[-1::-1]
print(range_vec)
print()

# 2.d.
mat3x3 = np.arange(0,9).reshape(3,3)
print(mat3x3)
print()

# 2.e.
print(np.argwhere(np.array([1,2,0,0,4,0]) == 0))
print()

# 2.f.
randvec = np.random.random(30)
print(randvec.mean())

# 2.g.
mat_2D = np.ones((4,4))
mat_2D[1:-1,1:-1] = 0
print(mat_2D)
print()

# 2.h.
chkboer = np.zeros((8,8))
chkboer[0::2,0::2] = 1
chkboer[1::2,1::2] = 1
print(chkboer)
print()

# 2.i.
chkbrd = np.tile(np.eye(2), (4,4)) 
print(chkbrd)
print()

# 2.j.
Z = np.arange(11)
Z[3:9] *= -1
print(Z)
print()

# 2.k.
Z = np.random.random(10)
Z = np.sort(Z)
print(Z)
print()

# 2.l.
A = np.random.randint(0,2,5)
B = np.random.randint(0,2,5)
equal = (A == B).all()
print(equal)
print()

# 2.m.
Z = np.arange(10, dtype=np.int32)
print(Z.dtype)
Z = Z.astype(np.float32)
print(Z.dtype)
print()

# 2.n.
A = np.arange(9).reshape(3,3)
B = A + 1
C = np.dot(A,B)
print(C)
D = C[list(range(A.shape[0])), list(range(B.shape[1]))]
print(D)

