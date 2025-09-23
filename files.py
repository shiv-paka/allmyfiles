'''
file=open("user.txt.","r")
print(file.read()) 
file.close()

#File opening ke liye x , file reading ke liye r , 



file=open("user.txt.","r")
print(file.read())
file.close

file1= open("other.txt","x")
file1= open("other.txt","r")

file1.write("Sare mams podam\n")
file1.write("Sare le anthey le\n")
file1.write("kallu dobbinaaya\n")
#file1=("other.txt","r")
print()

print(file1.readlines(10))
print()
print(file1.readline(30))  #gives individual lines
print()
print(file1.read())   #gives entire file

#print(file1.read())
file.close()
file2= open("other.txt","x") #file exists so errorrrrrrr 
file=open("new_other.txt","r")
lst=['Hello there','Hi there','Ho ho ho']
file.writelines(lst)
print(file.read())
print(file.tell())
print(file.seek(20))
print(file.read(10))
'''

file=open("Somefile.txt","r")
'''file.write("hello\n")
file.write("hi\n")
file.write("how are you\n")
file.write("I am fine\n")
file.write("i am hungry\n")
file.write("please save me\n")
file.write("woooowwwww\n")
'''
for i in range(1,6):
    print(file.readlines(i))

file=open("pythonfile.txt","r")
'''file.write("python is fun\n")
file.write("they said\n")
file.write("youll have fun coding on python they said\n")
file.write("python==woowwww\n")
file.write("python antey enti saar?\n")'''
''' 
counter=0
for ele in file:
    if "python" in ele:
        counter+=1'''
print(file.read())


#develop a program that copies the contents of one file to another

file1=("hjtrw.txt","w")
data=file.read()
file1.write(data)