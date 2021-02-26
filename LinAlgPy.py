from sympy import *
from sympy.interactive import printing
printing.init_printing(use_latex = True)
import sympy as sp

A = Matrix([[1,2,2], [3,-2,1], [0,1,1]])
RA = A.rref()
NA = A.nullspace()
CA = A.columnspace()
EA = A.eigenvals()
EV = A.eigenvects()
RA = A.rank()
IA = A.inv()
LU = A.LUdecomposition()

lamda = sp.Symbol('lamda')
p = A.charpoly(lamda)
sp.factor(p.as_expr())

P, D = A.diagonalize()
starting_matrix = simplify(P*D*P.inv())
print(starting_matrix)
print(A)
