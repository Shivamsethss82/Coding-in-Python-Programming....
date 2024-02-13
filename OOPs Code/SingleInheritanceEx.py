# Single inheritace:-


class Millioner():
    no_of_holidays = 10
    def __init__(self,name,work,company):
        self.name = name
        self.work = work
        self.company = company
    def Millionerdetail(self):
        return f"Millioner Name is {self.name} Its working on {self.work},Thats working on {self.company}"
class Billioner(Millioner):
    no_of_leaves = 5
    def __init__(self,name,work,company,location):
        self.name = name
        self.work = work
        self.company = company
        self.location = location
    def BillionerDetail(self):
        return f"Billioner name is {self.name} and work as a {self.work},company is {self.company},location is {self.location}"
        

shivam = Millioner("Nicky Goel","Software Engineer","Ahana System")
Srikant = Billioner("Srikant P","Lead Software Engineer","Google","USA")

print("srikants Leaves: ", Srikant.no_of_leaves)
print(Srikant.BillionerDetail())
print(shivam.Millionerdetail())
print("Shivam Holidayes is ",shivam.no_of_holidays)