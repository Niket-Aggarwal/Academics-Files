 #practical questons
#1
'''
from math import sqrt
print('To find root of quadratic equation enter a,b,c')
while True:
    try:
        a=eval(input('Enter a:'))
        if type(a) not in [int,float] or a==0 :
            print('Entered data is not correct acc. to a')
        else:
            while True:
                b=eval(input('Enter b:'))
                c=eval(input('Enter c:'))
                if type(b) in [int,float] and type(c) in [int,float]:
                    break
                else:
                    print('Enter a integer')
            break
    except:
        print('Enter Numbers only')
D=b**2-(4*a*c)
if D>=0:
    print('so roots of Equation:',(-b+sqrt(D))/(2*a),end=',')
    print((-b-sqrt(D))/(2*a))
else:
    print('as D<0 so no real roots')
'''

#2
'''
def prime(n):
    for i in range(2,n):
        if n%i==0:
            return False
    return True
while True:
    try:
        n=int(input('Enter a number n so to perform some prime number task:'))
        if n<=0:
            print('Enter interger greater than 0')
        else:
            break
    except:
        print('Enter interger greater than 0')
#a
if prime(n):
    print('a)',n,'is prime')
else:
    print('a)',n,'is not prime')
#b
print('b) All prime number till',n,'is:',end='')
for i in range(2,n+1):
    if prime(i):
        print(i,end=' ')
print()
#c
print('c) first',n,'prime number are:',end='')
c=0;a=2
while c!=n:
    if prime(a):
        print(a,end=' ')
        c+=1
    a+=1
'''

#3
'''
print('pyramid of "*"\n')
n=2
for i in range(3):
    print(" "*(6-i*2),end='')
    for j in range(1,n):
        print("*",end=' ')
    n=n+2
    print()
for i in range(3,8):
    print(" "*(i*2-6),end='')
    for j in range(1,n):
        print('*',end=' ')
    n=n-2
    print()
'''

#4
'''
print('To check the type and details of entered character')
d={1:'One',2:'Two',3:'Three',4:'Four',5:'Five',6:'Six',7:'Seven',8:'Eight',9:'Nine',0:'Zero'}
a=input('Enter:')
if a.isdigit():
    print(a,'is numeric digit')
    if len(a)==1:
       print(a,'is',d[int(a)])
elif a.isalpha():
    print(a,'is a letter')
    if a.isupper():
       print(a,'is in uppercase')
    elif a.islower():
       print(a,'is in lowercase')
    else:
        print('Mix of both lower and upper')
elif a.isalnum()!=True and a.isspace()!=True:
    print(a,'is a special character')
else:
    print('Not recognised')
'''

#5
'''
print('To perform some string opeartion enter string and a character from that string')
a=input('Enter a String:')
c=input('Enter character:')
#a
print('a) Frequency of',c,'in',a,'is:',a.count(c),'\n')
#b
b=input('b) By which character you want to replace '+c+':')
print('New string is;',a.replace(c,b),'\n')
#c
print('c)Removing first occurence')
print('Original string',a)
x=a.find(c)
if x==-1:
    print('Character is not in string')
    print('No change\n')
else:
    print('New string:',a[:x]+a[x+len(c):],'\n')
#d
print('d)Removing all occurrence')
y=0;d=a
for i in range(a.count(c)):
    x=a.find(c)
    a=a[:x]+a[x+len(c):]
    y+=1
if y==0:
    print('Same is old string:',a)
else:
    print('Old string:',d)
    print('New string:',a)
'''

#6
'''
print('Swaping first n character from two string')
a=input('Enter string1:')
b=input('Enter string2:')
while True:
    try:
        n=int(input('Enter n character to be swap:'))
        if n<0:
            print('Enter positive number')
        else:
            break
    except:
        print('Enter number only')
x=b[:n]+a[n:]
b=a[:n]+b[n:]
a=x
print('\nNEW after swaping')
print('String1:',a)
print('String2:',b)
'''

#7
'''
print('Enter two string to check that the second string occur in first or not')
def checkstr(a,b):
    l=[]
    if a.count(b)==0:
        return -1
    else:
        c=len(b)
        for i in range(len(a)):
            if a[i:i+c].lower()==b.lower():
                l.append(i)
        return l
a=input('Enter first string:')
b=input('Enter second string:')
l=checkstr(a,b)
if l==-1:
    print('No occurence of',b,'in',a,'(-1)')
else:
    print(b,'occurs in',a,'on indices:',l)
'''

#8
'''
print('Enter a list of number and a second list is generated with the cube of even in given list')
while True:
    l=eval(input('Enter a list:'))
    if type(l)==list:
        break
    else:
        print('Enter list only\n')
#a
cl=[]
for i in l:
    if type(i)==int and i%2==0:
        a=i**3
        cl.append(a)
print('Cube of even number in given list:',cl)
#b
ccl=[a**3 for a in l if type(a)==int]
print('Cube of even number in given list:',ccl)
'''

#9
'''
print('File Name:Text.txt')
try:
    f=open("Text.txt",'r')
    f.close()
except:
    print('\nFile doesnot exist first create it')
    n=eval(input('How many lines do you want to add:'))
    f=open('Text.txt','a')
    for i in range(1,n+1):
        a=input('Enter line'+str(i)+':')
        f.write(a+'\n')
    print('File created\n')
    f.close()
#a
print("a)Total no. of character,words and lines in the file")
f=open("Text.txt",'r')
r=f.read()
print('Total number of character:',len(r))
l1=r.split()
print("Total number of words",len(l1))
l2=r.split("\n")
print(l2)
print('Total number of lines',len(l2)-1,'\n')
f.close()
#b
print('b)Calculating the frequency of each character in form of dictionary')
f=open("Text.txt",'r')
r=f.read()
freq={}
for i in r:
    if i in " \n":
        continue
    a=r.count(i)
    freq[i]=a
print('Frequency of each character is:',freq,'\n')
f.close()
#c
print('c)Printing words of file in reverse order')
f=open("Text.txt",'r')
rev=f.readlines()[::-1]
for i in rev:
    l=i.split()[::-1]
    for j in l:
        print(j,end=' ')
    print()
f.close()
#d
print('\nd)Copy even lines to File1.txt and odd lines to File2.txt')
f=open('Text.txt','r')
f1=open('File1.txt','w+')
f2=open('File2.txt','w+')
r=f.readlines()
c=1
for i in r:
    if c%2==0:
        f1.write(i)
    else:
        f2.write(i)
    c+=1
print('Copy Done')
f.seek(0)
f1.seek(0)
f2.seek(0)
print('Text.txt:')
print(f.read())
print('File1.txt:')
print(f1.read())
print('File2.txt:')
print(f2.read())
f.close()
f1.close()
f2.close()
'''

#10
'''
def dict_cube():
    d={}
    for i in range(1,6):
        d[i]=i**3
    print("Dictionary:",d)
print('A dictionary that habe key between 1 and 5 and value as cube of key')
dict_cube()
'''

#11
'''
print('Tuple Operations:',end="")
t1=(1,2,5,7,9,2,4,6,8,10)
print(t1)
#a
print("a)Half in one line and other half in second line")
l=len(t1)//2
print("First half:",t1[:l])
print("second half:",t1[l:],'\n')
#b
print("b)Another Tuple with even values")
t=()
for i in t1:
    if i%2==0:
        t=t+(i,)
print('New tuple:',t,"\n")
#c
t2=(11,13,15)
print("c)Concatenate")
print("Original:",t1)
print("To add:",t2)
print("Cancatenated:",t1+t2,"\n")
#d
print("d)Max and Min value of the Tuple")
print("Max:",max(t1))
print("Min:",min(t1))
'''

#12
'''
print("Class Employee is created to store information of Employee\n")
class Employee:
    count=0
    def __init__(self,empno,name,dept,basic,da,hra):
        if basic<0 or da<0 or hra<0:
            raise ValueError("Basic,DA and HRA must be non-negative values.")
        self.empno = empno
        self.name = name
        self.dept = dept
        self.basic = basic
        self.da = da
        self.hra = hra
        Employee.count+= 1
    def get_salary(self):
        return self.basic+self.da+self.hra
    def __del__(self):
        Employee.count-=1
    def __str__(self):
        return f"EmployeeNo:{self.empno}\nName:{self.name}\nDepartment:{self.dept}\nBasic Pay:{self.basic}\nDA:{self.da}\nHRA:{self.hra}\nTotal Salary:{self.get_salary()}"
try:
    E1=Employee(101,"Niket","AI Research",50000,10000,5000)
    E2=Employee(102,"Riya","Data Science",60000,12000,6000)
    print("Total Employee:",Employee.count)
    print(E1.__str__(),'\n')
    print(E2.__str__())
    del E1
    print('\nEmployee with id 101 id deleted')
    print("Remaining Employees:",Employee.count)
    print(E2.__str__(),'\n')
    print(E1.__str__())
except ValueError as e:
    print("Error:", e)
except:
    print("Object not found")
'''

#13
'''
print("Working with 2D Plan:")
import math
class Point2D:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def get_coordinates(self):
        return f"({self.x},{self.y})"
    def dist_between(self,other):
        return math.sqrt((self.x-other.x)**2+(self.y-other.y)**2)
def main():
    P1=Point2D(1,2)
    P2=Point2D(3,4)
    print("Point1:",P1.get_coordinates())
    print("Point2:",P2.get_coordinates())
    print("Distance between point1 and point2:",P1.dist_between(P2))
if __name__=="__main__":
    main()
'''

#14
'''
print("Working with 3D Plan:")
class Point3D(Point2D):
    def __init__(self,x,y,z):
        super().__init__(x,y)
        self.z=z
    def get_coordinates(self):
        return f"Point({self.x},{self.y},{self.z})"
    def distance(self,other):
        return math.sqrt((self.x-other.x)**2+(self.y-other.y)**2+(self.z-other.z)**2)
def main():
    P3=Point3D(1,2,3)
    P4=Point3D(4,6,9)
    print("Point3:",P3.get_coordinates())
    print("Point4:",P4.get_coordinates())
    print("Distance between point3 and point4:",P3.distance(P4))
if __name__=="__main__":
    main()
'''

#15
'''
print('To check that the user enter name in correct format or not')
try:
    a=input("Enter Username:")
    if a=="" or a==" ":
        raise ValueError("Username field cannot be empty")
    for i in a:
        if i.isspace():
            pass
        elif i.isalpha()==False:
            raise ValueError("Given username is not correct it will not contain number/special character")
    print("Entered username is correct that is:",a)
except ValueError as e:
    print("\nError:",e)
'''
