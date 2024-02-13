class Base1():
    def function1(self):
        return "This is Base 1 class."
class Base2():
    def function2(self):
        return "This is base 2 class."
class child(Base1,Base2):
    def function3(self):
        return "This'one have all features of base1 and base2"
    
object = child()
print(object.function1())
print(object.function2())
print(object.function3())