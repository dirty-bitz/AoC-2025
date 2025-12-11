import numpy as np
from scipy import sparse

def isRectangleInside(M,iMin,iMax,jMin,jMax):
    if iMin == iMax:
        rect = M[iMin,jMin+1:jMax]
    elif jMin == jMax:
        rect = M[iMin+1:iMax,jMin]
    else:
        rect = M[iMin+1:iMax,jMin+1:jMax]
    nel = np.prod(rect.shape)
    if rect.nnz == nel: # Only points over the contour
        return True
    elif 0 < rect.nnz < nel: # Rectangle crosses the contour
        return False
    elif rect.nnz == 0: # Ray casting to decide if inside or outside
        return np.sum(M[(iMin+iMax)//2,:(jMin+jMax)//2])%2 == 1

def rectangles(filepath):
    C = np.loadtxt(filepath, delimiter=",",dtype=int)
    nC = len(C)
    n,m = np.max(C,axis=0)
    M = sparse.lil_matrix((n+2,m+2),dtype=int)
    for k in range(nC):
        (i0, j0), (i1, j1) = C[k], C[(k+1)%nC]
        iMin, iMax = sorted((i0, i1))
        jMin, jMax = sorted((j0, j1))
        M[iMin:iMax+1,jMin:jMax+1] = 1
    M = M.tocsc() # optimization
    maxA = 0
    for k in range(nC):
        for l in range(k+1,nC):
            (i0, j0), (i1, j1) = C[k], C[l]
            iMin, iMax = sorted((i0, i1))
            jMin, jMax = sorted((j0, j1))
            if isRectangleInside(M,iMin,iMax,jMin,jMax):
                itA = (abs(i0-i1)+1)*(abs(j0-j1)+1)
                if itA > maxA:
                    maxA = itA
                    print(C[k],C[l],'->',itA)
    return maxA

print(rectangles("input.csv"))