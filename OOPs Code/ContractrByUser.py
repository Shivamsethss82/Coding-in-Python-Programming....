class Employee():
    def __init__(self):
        self.name = input("enter name: ")
        self.sal = input("enter Salary: ")
        self.post = input("enter Position: ")
        self.mob = input("enter Mobile: ")
        
    def detail(self):
        return f"My name is {self.name} and my salary is {self.sal} My post is {self.post} finallay my mobile number is {self.mob}"
    # @staticmethod
    # def printgood 
# shivam = Employee("Seth ji","200","ASE",9793338682)

s = Employee()
print(s.detail())