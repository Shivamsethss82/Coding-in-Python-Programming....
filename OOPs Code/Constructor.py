class Employee():
    def __init__(self):
        pass
    
    def info(self,name,job,salary,address):
        self.name = name
        self.job = job
        self.salary = salary
        self.address = address
    def detail(self):
        return f"My Name is {self.name} My post of job is {self.job} and salary is {self.salary},and Adress is {self.address}"
  
# shivam = Employee("Shivam Seth","SE",200000,"Farrukhabad")
# amit = Employee("Amit Pal","Wipro Engineer",50000,"Kanpur")
# print(shivam.detail())
# print(amit.detail())
# print(amit.salary)
# print(amit.name)
# print(shivam.leaves)
s = Employee()
s.name = input("enter name: ")
s.job = input("enter designation: ")
s.salary = input("enter salary: ")
s.address = input("enter address: ")

print(s.detail())
print(s.address)