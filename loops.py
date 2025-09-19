'''num=int(input('Enter how many times i should repeat it\n'))
for i in range(num):
    print("Namaste! Bonjor! Hola! Namaste!")'''

'''even=101
for i in range(even):
      if i%2==0:
        print(i)'''

'''odd=101
for i in range(odd):
    if i%2!=0 :
        print(i)
'''
'''num=1
while num<=10:
    print(num)
    num+=1'''
    #Goes on forever until your computer shuts down.......hehehe
'''num=1
while True:    
    print(num) 
    num+=1'''
#Star makerr
'''e=int(input('Enter the number of rows of stars:\n'))
f=int(input('Enter the number of columns:\n'))
for i in (0,e+1):
    l=[['*']*e]*f
    print(l)'''

#Bank Balance thingy
'''a=50000
b=int(input("Enter the amount you want to withdraw\n"))
if a>=b and b>0:
    print(f"you can withdraw {b} amount and be left with {a-b}")
elif b<0:
    print('Brother negative')
else:
    print("Insufficient balance")

bankBalance=500
while bankBalance>=0:
    xAmount=int(input("Enter the amount to be withdrawn\n"))
    if bankBalance>=xAmount:
      print(f"Your amount has been withdrawn, your remaining balance is {bankBalance-xAmount}")
        
    else :
        print("Insufficient fundzzzzzz")
        quit()
print("Thank you")'''

'''for i in range(1,10):
    if i==6:
       pass
    print(i)
print('Done with loop')'''

#tablesssss
'''a=int(input("Enter a number to calculate its table\n"))
b=int(input('Enter upto what number you want to multiply\n'))
for i in range(1,b+1):
   print(f"{a}X{i}={a*i}")
'''
# exponent calculator
'''c=int(input('Enter number:\n'))
d=int(input('Enter power:\n'))
for i in range(0,d+1):          #print(f'{c}^{d}={c**d}')
    print(f'{c}^{i}={c**i}')'''


#number checker
'''systemGuess=15
myGuess=0
count=0
while myGuess!=systemGuess:
     myGuess=int(input('Enter a number:\n'))
     
     if  myGuess>systemGuess:
       print("number too high")
     elif  myGuess<systemGuess:
       print('number too low')
     else:
       print('Correct number') 
     count+=1 
     if  count>=3:
        print("Out of guesses , try again please.....")
        break   '''

'''a=str(input("Enter a word:\n")).lower()
b="aeiou"
count=0
for char in a:
    if char in b:
     count+=1
     print(count,end=',')'''
#prototype 1
'''i=0
j=0
for i in (1,11):
    i+=1
    print('*')
    for j in (1,11): 
        j+=1  
        c='*'
        d=j*c
        print(end=d)'''
#prototype 2
'''i=0
j=0
while i>=0 and i<11:
    i+=1
    print('*')
    for j in range(1,11):
        j+=i
        print(end="*")'''
#prototype 3
'''i=1
j=0
for i in (1,11):
    i+=1
    print('*')
    for j in (0,11): 
        j+=1  
        print(end='*')'''
#prototype 4(printing only 2 rows)
'''i=1
j=0
while i in (1,11):
    i+=1
    print('*')
    for j in (0,11): 
        j+=1  
        print(end='*')'''
    
#prototype 5(works?)
'''i=1
j=0
for i in (1,3):
    print('*')
    i+=1
    for j in range(1,i): 
        j+=1  
        print(end='*')'''
#prototype 6(lmao works??)
'''i=1
j=0
for i in (1,2,3,4,5,6,7,8,9,10,11):
    print('*')
    i+=1
    for j in range(1,i): 
        j+=1  
        print(end='*')'''
#prototype 7
userInput=int(input('Enter a number:'))
for i in (0,userInput+1):
    print('*')

    for j in range(i+1): 
        print(end='*') 
    
'''user_input=int(input("Enter a number:"))
for i in range(0,user_input):
     print('*')
for j in range(0,user_input-1):
    print(' *')'''


'''counter=int(input('Enter the number of stars:'))

for i in range(1,counter+1):
    stars='*'*i
    print(f'{stars}')'''
    