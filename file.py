'''
file=open("user.txt.","r")
print(file.read()) 
file.close()
'''
#File opening ke liye x , file reading ke liye r , 



file=open("user.txt.","r")
print(file.read())
file.close

'''file1= open("other.txt","x")'''
file1= open("other.txt","r")
'''
file1.write("Sare mams podam\n")
file1.write("Sare le anthey le\n")
file1.write("kallu dobbinaaya\n")'''
#file1=("other.txt","r")
print(file1.readline(30))  #gives individual lines
print(file1.read())   #gives entire file
#print(file1.read())
file.close()
'''file2= open("other.txt","x")''' #file exists so errorrrrrrr
