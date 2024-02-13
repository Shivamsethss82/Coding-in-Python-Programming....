class Employee:
    no_of_leaves = 15
    def __init__(self,name,salary,role):
        self.name = name
        self.salary = salary
        self.role = role
    def detail(self):
        return f"Person Name is {self.name} his salary is {self.salary},and it is s {self.role}"
    @classmethod
    
    def changeleave(cls,new_leaves):
        cls.no_of_leaves = new_leaves
        no_of_leaves = 20
        return no_of_leaves
    
    @staticmethod
    def isAdult(age):
        return age>18
    ## Some DUNDER METHODS:-
    
    def __add__(self, other):
        return self.salary+other.salary
    def __truediv__(self,other):
        return self.salary/other.salary
    def __repr__(self) -> str:
        return self.detail()
        
shiv = Employee("shivam",2999,"Programmer")
sri = Employee("Srikant",1001,"Analysts")
print(shiv.detail())
print(Employee.detail(sri))

print(Employee.isAdult(19))
print(Employee.changeleave(22))
print("Sum of both salary is ",shiv+sri)
print(shiv/sri)
print(sri)