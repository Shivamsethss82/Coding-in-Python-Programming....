'''
class parent_class_Name:
    # parent_class_Code Block
class Child_class_Name(parent_class_Code):
    # Chile_class_Code Block
'''


class Parent():
    def first(self):
        return "Its have parents Properties:"
class Clild(Parent):
    def secound(self):
        return "Its have Both Properties"
srikant = Clild()
print(srikant.first())
print(srikant.secound())
