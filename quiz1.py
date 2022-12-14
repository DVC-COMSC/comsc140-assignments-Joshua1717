class Student:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        Student.numbofStudent = Student.numofStudent + 1
  

    @property
    def id(self):
        return self.id
    
    @id.setter
    def id(self,id):
        self._id = id

    @property        
    def name(self):
        return self._name

    @name.setter          
    def name(self,name):
        self._name = name

    

p1 = Point(10,10)
p1._x = -10 
print(p1.x, p1._y)


