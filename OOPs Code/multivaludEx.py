# MULTI-LEVEL OR MULTI-VALUED  INHERITANCE


class Grandfather:
    basketball =6
    
class Father(Grandfather):
    dance =1
    basketball = 9
    def isdance(self):
        return f"Yes I dance {self.dance} no of times"

class Son(Father):
    dance =6
    guitar = 1

    def isdance(self):
        return f"Jackson yeah!" \
            f"Yes I dance very awesomely {self.dance} no of times"

honey = Grandfather()
rony = Father()
shony = Son()
print(honey.basketball)
print(rony.basketball)
print(shony.isdance())
print(shony.guitar)