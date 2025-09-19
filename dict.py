person={
    "name":"Madhu uncle",
        "age":55 
        }
print(person)
print(person["age"])
person["age"]=22
print(person)

person["friends"]=["Akhil power of juvva",
                   "Anjali"]
print(person)

#print(person["addr])
print(person.get("addr"))
del person["age"]
print(person)
print()
#person.pop("age")
print(person)                        
person["marks"]=[28,38,56]
person["age"]=22
print()
person.popitem()
print(person)
  
a=["Name","Age","Gender","Study"]
b=["Me",32,"Female","Btech"]
my_dict={}
for i in range(len(a)):
    my_dict[a[i]]=b[i]
print(my_dict)

k=[1,2,3,4,5,6]
v=[7,8,9,10,11,12]
myDict={}
for i in range(len(k)):
    myDict[k[i]]=v[i]
print(myDict)
for ele in person.keys():
    print(ele)
    print(person[ele])
for elem in person.values():
    print(elem)
    print(person[elem])
