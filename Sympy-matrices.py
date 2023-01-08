#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 23 00:03:51 2022

@author: ahsensenertambay
"""


#Examining the sympy library matrices documentation 
from sympy.matrices import Matrix, eye, zeros, ones, Identity ,diag, GramSchmidt
from sympy.abc import a,b,c,d,e,f

#Let's begin creating a matrix :)
M = Matrix([[a,b,c], [d,e,f]])

#You can also create a matrix by entrying your list and sized.
#Example for creating a 2*4 matrix:
M= Matrix(2, 4, [a, b, c, 4, 5, 6,0,7])


#You can create a list for indicator function and then use the indicator for crating the matrix:
f=(a,b,c,d,8,9,0,1)
M=Matrix(2, 4, f)


#Special matrices:
eye(4) #identity matrix
zeros(2) #zero matrix
ones(3) #all entries are one
diag(1, Matrix([[1, 2], [3, 4]])) #diagonal matrix


#You can create submatrics 3*3:
M[0:3, 0:3]
M.shape

#Calling a specific column or row:
M.row(0)
M.col(-1)


#Calling the value of your matrix element in  a specific row and column
M[1,2]
M[0,1]


#If you just enter a value, you call the element as if in a 1-d list, 
#even though the matrix is 2-d.
M[4]

#Calling the matrix specific columns entries:
M[0:3,2]

#If you want to add a row your current matrix:
M = Matrix([M,(1,2,3,4)])


#Replaceing your entries:
M[2,2] = M[0,3] = 7

#You can use a symbol and replace your symbol to other symbol or a value
#Advantage of Sympy
from sympy import  Symbol
from sympy.abc import x

x = Symbol('x')
M = eye(3) * x
M
M.subs(x, 4)


x=4
sqrt(x)


#A row or column delete or insert:
M.row_del(0)
M.col_del(1)

M = M.row_insert(1, Matrix([[0, 4]]))
M = M.col_insert(0, Matrix([1, -2]))


#Join two matrices:
M2 = Matrix(([1,2,3,4],[5,6,7,8],[8,9,10,11]))
M.row_join(M2) 


#You can use arithmetic operations with matrixes:
M+M2
M2-M
M = Matrix([M,(0,2,1,4)])
M2= Matrix([M2,(1,6,2,7)])
M*M2
M2**2 #for M^2


#Aritchmetic operations with vectors:
v1 = Matrix([1,2,3])
v2 = Matrix([4,5,6])
v3 = v1.cross(v2)

#Operations on entries:
# All entries multipy 2:
M = eye(3)
2*M

#Another way you can create an indicator
f = lambda x: 2*x
eye(3).applyfunc(f)




#Calculating determinant your matrices:
M = Matrix(( [1, 2, 3], [3, 6, 2], [2, 0, 1] ))
M.det()
M2 = eye(3)
M2.det()
M3 = Matrix(( [1, 0, 0], [1, 0, 0], [1, 0, 0] ))
M3.det()


#invense a matrix:
D1 = Matrix([[x, y], [1, x*y]]).inv('ADJ')
D1.inv()
D1.inv(method="LU")

#Transpose a matrix:
D1.T

#Testing equation matrices:
v1 = Matrix([(1,1,1,1)])
v2=  ones(1,4)
v1.equals(v2)

#Row reduction with a symbol:
from sympy.abc import x,y,z
P= Matrix(3,3,[1,0,1,0,1,2,0,0,0])
D= Matrix (3,3,[1,0,1,0,2,4,2,x,6])
             
#R2-R1:
D.row(1)-D.row(0)    

#R2/2
D.row(1)/2
    

#If you want to a rows includes symbol entry then you can not + or - operations
#Then you can use following codes
#For R3-2:
for j in range(3):
        element = D[2, j]
        if element.is_symbol:  
             expression = element - 2
             D[2, j] = expression         
        else:  
             D[2, j] = element - 2  



#Matrices echolon form:    
M = Matrix([[1,1,0,1], [0,1,2,3], [1,1,1,2]])
M.echelon_form()


#Matrices Row Reduced Echolon Form:
M.rref()


#Pivots:
rref_matrix, rref_pivots = M.rref()
rref_matrix
rref_pivots 


#Testing echolon forms and row reduce echolon forms:
M1=Matrix([[1,0],[0,1]])
M2=zeros(2)
M3= Matrix(4,1,[0,1,0,0])
M4= Matrix(1,4,[0,6,3,0])
M5= Matrix([[0,1,7],[0,0,1]])

M1.echelon_form()
M1.rref()

M2.echelon_form()
M2.rref() #not in RREF

M3.echelon_form()
M3.rref() #not in RREF

M4.echelon_form()
M4.rref() #not in RREF

M5.echelon_form()
M5.rref()





#Solutions: 
    
#Unique solution:
#2x-3y+z=-1 ; x-y+2z=-3 ; 3x+y-z=9
augmented_A = Matrix([[2, -3, 1, -1],
                      [1, -1, 2, -3],
                      [3, 1, -1, 9]])
augmented_A.rref()[0]
 
#No solution:
#x-y+4z=-5 ; 3x+z=0 ; -x+y-4z=20
augmented_A = Matrix([[1, -1, 4, -5],
                      [3, 0, 1, 0],
                      [-1, 1, -4, 20]])
augmented_A.rref()[0]


#infinetly many solutions:
#-x+y+2z=0 ; x+2y+z=6 ; -2x-y+z=-6
augmented_A = Matrix([[-1, 1, 2, 0],
                      [1, 2, 1, 6],
                      [-2, -1, 1, -6]])
augmented_A.rref()[0]










