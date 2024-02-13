# DIAMOND PROBLEM (CONFUSING) OF INHERITANCE:-

class A:
    def meth(self):
        return "You are in class A"
class B(A):
    def meth(self):
        return "You are in class B"
class C(A):
    def meth(self):
        return "You are in class C"
class D(C,B):
    pass
    
a = A()
b = B()
c = C()
d = D()
print(d.meth())