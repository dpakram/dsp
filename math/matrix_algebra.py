#Matrix Algebra

#import package
import numpy as np 

#define matrices

A = np.matrix([[1, 2, 3],[2, 7, 4]])
B = np.matrix([[1, -1],[0,1]])
C = np.matrix([[5,-1],[9,1],[6,0]])
D = np.matrix([[3,-2,-1],[1,2,3]])
u = np.matrix([6,2,-3,5])
v = np.matrix([3,5,-1,4])
w = np.matrix([[1],[8],[0],[5]])

#1. Matrix Dimensions: write the dimension of each matrix
#print the dimensions of each matrix (m, n)
#where m is the number of rows and n is the number of columns
print "The dimensions of A are:", A.shape
print "The dimensions of B are:", B.shape
print "The dimensions of C are:", C.shape
print "The dimensions of D are:", D.shape
print "The dimensions of u are:", u.shape
print "The dimensions of v are:", v.shape
print "The dimensions of w are:", w.shape

#2. Vector Operations: perform the follow operations
alpha = 6
print "u + v =", u + v
print "u - v =", u - v
print "alpha * u =", alpha * u
print "u * v =", u * np.transpose(v)
print "||u|| =", np.linalg.norm(u)

#3. Matrix Operations
#3.1
print "A + C = Not Defined "
#3.2
print "A - C^T =", A - np.transpose(C)
#3.3
print "C^T + 3D =", np.transpose(C) + (3 * D)
#3.4
print "BA =", B * A
#3.5
print "BA^T = Not Defined"
#3.6
print "BC = Not Defined"
#3.7 
print "CB =", C * B
#3.8
print "B^4 =", B^4
#3.9
print "AA^T = Not Defined"
#3.10
print "D^T * D =", np.transpose(D)*D
