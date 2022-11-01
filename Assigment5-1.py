# A naive python3 program to find sum of product
  
# Returns sum of pair products
def findProductSum(A,n):
 
    product = 0
    for i in range (n):
        for j in range ( i+1,n):
            product = product + A[i]*A[j]
    return product
  
# Driver code
if __name__=="__main__":
 
    A = [1, 3, 4]
    n = len (A)
  
    print("sum of product of all pairs "
    "of array elements : " ,findProductSum(A, n))