list1 = [["harray",1],["Larray",5] , ["Carray",10],["Riyan",20]]
for item,lollypop in list1:
    print(item, "and lollypop is",lollypop )
dict1 = dict(list1)
print(dict1)
list1.append(["Radha",50])
print(list1)


list2 = [1,11,"Rada","Shivam",52,9,72.5,"Seth"]

for items in list2:
    if str(items).isnumeric() and items>9:
        print(items)