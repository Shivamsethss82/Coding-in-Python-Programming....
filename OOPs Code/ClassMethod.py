class Employee():
    leaves = 10
    def __init__(self,name,salary,adress):
        self.name = name
        self.salary = salary
        self.adress = adress
    def detailemp(self):
        return f"Name is {self.name}.My sallery is {self.salary} and my adress is {self.adress}"
    
    @classmethod
    def change_leaves(cls,newleaves):
        cls.leaves = newleaves
    
    @classmethod
    def from_str(cls,string):
        div = string.split("-")    
        return cls(div[0],div[1],div[2])
    
    @staticmethod
    def printgood(string):
        print("This is staic name : " + string)
    

shivam = Employee("Mafia",10000,"Nalanda")
srikanth= Employee("Srikath P",20000,"Mysore")
karan = Employee.from_str("Karan-30000-Shivni MP") # in one Strings

print("Before the change Leaves: ",srikanth.leaves)
srikanth.change_leaves(18)
print(srikanth.salary)
print("After changing leaves",srikanth.leaves)
print(shivam.detailemp())
print(srikanth.detailemp())
print(karan.detailemp())
Employee.printgood("Shivam")