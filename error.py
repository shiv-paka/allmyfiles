print(10//0.5)
# you can catch errors only if the error throwing lines are in try
num=10
num1=0
try:
 print(num/num1)
 num2=int("abc")
 num3=10+"as"
# file1=open("Idkwhattonameit.txt","x")
 file=open("somefile.txt","r")
except ZeroDivisionError:
  print("You can't divide by 0")
except Exception as e:
  print(e)
finally:
  print("I run even if there is an error cuz like why not")
'''
except ZeroDivisionError:
    print("Can't divide a number with 0")
except ValueError:
    print("can't convert string...........") 
except TypeError:
    print("Can't add str to int")
except FileNotFoundError:
    print("That file doesn't exist")
except FileExistsError:
    print("File already exists.")
    '''
print("Done")