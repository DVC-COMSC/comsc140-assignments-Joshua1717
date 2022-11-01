#Returning Multiple Values using Data Classes
from dataclasses import dataclass

@dataclass
class multiplevalues():
    operation: str
    num1: int = 0
    num2: int = 0
    def values(self) -> float:
        return self.num1 + self.num2   

#passing arguments into the Data Class 
all_values = multiplevalues("Addition", 5, 10)
v = all_values.values() 

print(v)
print(all_values)
#Output
#15
#multiplevalues(operation='Addition', num1=5, num2=10)