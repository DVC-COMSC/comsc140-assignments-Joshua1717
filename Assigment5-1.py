list1 = [5, 3, 1, 1, 2]
list2 = [1, 2, 2, 9, 5]

def sumProduct(l1, l2):
    products = []
    sumP=0
    for num1, num2 in zip(list1, list2):
	    products.append(num1 * num2)
    sumP=sum(products)
    #print(products)
    return sumP

result =sumProduct(list1,list2)
print(result)
