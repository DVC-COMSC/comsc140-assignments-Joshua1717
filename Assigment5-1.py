
def findProductSum(A,n):
 
    product = 0
    for i in range (n):
        for j in range ( i+1,n):
            product = product + A[i]*A[j]
    return product
  

if __name__=="__main__":
 
    A = [5, 3, 1, 1, 2]
    n = len (A)
  
    print("sum of product of all pairs "
    "of array elements : " ,findProductSum(A, n))