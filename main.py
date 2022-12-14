import random

def caList():
	path = (r"C:\Users\joshu\Labs\comsc140-assignments-Joshua1717\ca2021.txt")
	canames = open('ca2021.txt')
	
	while(True):

		line = canames.readline()

		if not line:
			break

		namelist = []
		for line in canames:
			namelist.append(line.strip().split(' '))

	canames.close
	
	return 	namelist

def flList():
	path = (r"C:\Users\joshu\Labs\comsc140-assignments-Joshua1717\fl2021.txt")
	flnames = open("fl2021.txt")
	
	while(True):

		line = flnames.readline()

		if not line:
			break

		namelist = []
		for line in flnames:
			namelist.append(line.strip().split(' '))

	flnames.close
	
	return 	namelist

ca = caList()
fl = flList()

class Names():
    calnlist = ca
    flanlist = fl
    
    def __init__ (self, nlist):  

        lenofdict = len(ca._nlist)
        assert lenofdict == 200, "Invalid value. Expected 200"

        cnt = len([d for d in ca.nlist if d['Gender'] == 'F'])
        assert cnt == 100, "Invalid value. Expected 100"
        cnt = len([d for d in ca.nlist if d['Gender'] == 'M'])
        assert cnt == 100, "Invalid value. Expected 100"

        #mydict = [{'Name': 'Alexander', 'Count': 1483, 'Gender': 'M'}, {'Name': 'Amelia',
        #'Count': 1363, 'Gender': 'F'}, {'Name': 'Ava', 'Count': 1264, 'Gender': 'F'}]

        keys = ['Name', 'Count', 'Gender']
        mydict = [{k: v for k, v in zip(keys, n)} for n in nlist]
        ca._nlist = mydict
        assert len(ca._nlist) == 3, "Expected 3"

    def __str__():
        ca = Names('ca2021.txt')
        print(ca)
        assert ca.__str__ != None

    def _gt():
        ca = Names('ca2021.txt')
        fl = Names('fl2021.txt')
        result = ca > fl
        assert result == True, 'Expected True'

        #mydict1 = [{'Name': 'Alexander', 'Count': 1483, 'Gender': 'M'}, {'Name': 'Amelia', 'Count': 1363, 'Gender': 'F'}, 
        # {'Name': 'Ava', 'Count': 1264, 'Gender': 'F'}]
        keys = ['Name', 'Count', 'Gender']
        mydict1 = [{k: v for k, v in zip(keys, n)} for n in ca]  
        ca.nlist = mydict1
       
        #mydict2 = [{'Name': 'Oliver', 'Count': 1523, 'Gender': 'M'}, {'Name': 'Luna', 'Count': 1458, 'Gender': 'F'}, 
        # {'Name': 'Elijah', 'Count': 1498, 'Gender': 'M'}, {'Name': 'Amelia', 'Count': 1363, 'Gender': 'F'}]
        keys = ['Name', 'Count', 'Gender']
        mydict2 = [{k: v for k, v in zip(keys, n)} for n in fl] 
        fl.nlist = mydict2
        result = ca > fl
        assert result == False, 'Expected False'

        # getter property
        @property
        def nlist(self):
            return self._nlist

		#setter decorator
        @nlist.setter
        def nlist(self, nlist):
            self._nlist = nlist

    def printName():
        ca = Names('ca2021.txt')
        ret = ca.printName('C', 'Count', True)
        assert ret == 10, 'Expected 10'
        ret = ca.printName('E', 'Gender', False)
        assert ret == 23, 'Expected 23'
        #mydict1 = [{'Name': 'Alexander', 'Count': 1483, 'Gender': 'M'}, {'Name': 'Amelia',
        #'Count': 1363, 'Gender': 'F'}, {'Name': 'Ava', 'Count': 1264, 'Gender': 'F'}]

        keys = ['Name', 'Count', 'Gender']
        mydict1 = [{k: v for k, v in zip(keys, n)} for n in ca]  
        ca.nlist = mydict1
        ret = ca.printName('A', 'Count', True)
        assert ret == 3, 'Expected 3'

    printName()

def main():
    # Test code for your class
    ca = Names('ca2021.txt')
    print(ca)
    fl = Names('fl2021.txt')
    print(fl)
    print(ca.nlist)
    print(fl.nlist)

    if ca > fl:
        print('The name class ca is greater than fl')
    else:
        print('The name class fl is greater than or equal to ca')

    ca.printName('C', 'Count', True)
    ca.printName('D', 'Name', False)
    fl.printName('A', 'Count', True)
    fl.printName('E', 'Name', False)


if __name__ == '__main__':
    main()
