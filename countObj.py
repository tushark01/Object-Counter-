class employee :
       counter = 0

       def _init_(self,name,age) :
               self.name = name
               self.age = age
               employee.counter += 1

       def printDetails(self) :
        print(self.name,self.age,"years old")

employee1 = employee('Raj',42)
employee2 = employee('Ash',31)
employee3 = employee('jay',41)
employee4 = employee('harry',30)
print("Total number of objects created: ", employee.counter)
