#DOUBT
'''
for i in range(1,11):
    print(format(i,'4d'),end='')
print()
print('-'*45)
for i in range(1,11):
    for j in range(1,11):
        print(format(i*j,'4d'),end='')
    print()
'''

#BASIC QUESTIONS
#PRIME
'''
print('Enter 2 numbers and generate all prime numbers between them\n')
while True:
    n1=int(input('Enter first number'))
    if n1<=0:
        print('Number should be greater than 0')
        continue
    else:
        while True:
            n2=int(input('Enter second number'))
            if n2>n1:
                break
            else:
                print('second number must be greater than first number')
    break
print()
print('so prime number between',n1,'and',n2,'is:')
for i in range(n1,n2+1):
    if i==1:
        continue
    for j in range(2,i):
        if i%j==0:
            break
    else:
        print(i,end=' ')
'''
#PYRAMID
'''
print('pyramid trial\n')
while True:
    a=input('Enter a odd number or "*" :')
    if a=='*' or (a.isdigit() and int(a)%2!=0):
        break
    else:
        print('Enter accordingly\n')
if a!='*':
    a=int(a)
    n=2
    for i in range(a//2):
        print(" "*(((a//2)*2)-i*2),end='')
        for j in range(1,n):
            print(j,end=' ')
        n=n+2
        print()
    for i in range(a//2,a+1):
        print(" "*(i*2-((a//2)*2)),end='')
        for j in range(1,n):
            print(j,end=' ')
        n=n-2
        print()
else:
    n=2
    for i in range(3):
        print(" "*(6-i*2),end='')
        for j in range(1,n):
            print(a,end=' ')
        n=n+2
        print()
    for i in range(3,8):
        print(" "*(i*2-6),end='')
        for j in range(1,n):
            print(a,end=' ')
        n=n-2
        print()
print('\nTHANKYOU :)')
'''
#PRIMEFACTORS
'''
def primeFactor(x):
    n=x
    print(1,end='*')
    for k in range(2,x+1):
        while x%k==0:
            x//=k
            if x==1:
                print(k,'=',n)
            else:
                print(k,end='*')
x=int(input('Enter prime factor:'))
primeFactor(x)
'''
#HCF
'''
def  factor(x):
   n=x
   l=[]
   for k in range(2,x+1):
      while x%k==0:
         x//=k
         l.append(k)
   return l
a=int(input('enter number'))
print(factor(a))
'''
#N PRIME NUMBER
'''
n=int(input('how many prime number:'))
c=0
a=2
while c!=n:
    for i in range(2,a):
        if a%i==0:
            break
    else:
        print(a,end=' ')
        c+=1
    a+=1
'''

#OBJECT AND CLASSES
'''
import math
class Circle:
    def __init__(self,r):#self dena important hai
        self.radius=r
        self.type="Circle"
    def perimeter(self):
        a=2*self.radius*math.pi
        return a
    def area(self):
        a=self.radius**2*math.pi
        return a
C1=Circle(7)
print(C1.radius)
C1=Circle(10)
print(C1.radius)
'''
'''
C2=Circle(10)
print(Circle,type(Circle))
print('C1')
print(C1,type(C1))
print(C1.radius,C1.type)
print(C1.perimeter())
print(C1.area())
print('C2')
print(C2,type(C2))
print(C2.radius,C2.type)
print(C1.perimeter())
print(C1.area())
'''
#private
'''
import math
class Circle:
    def __init__(self,r):
        self.__radius=r
        self.__type="Circle"
    def __perimeter(self):
        a=2*self.__radius*math.pi
        return a
    def privateperi(self):
         return self.__perimeter()
C1=Circle(7)
print(C1.privateperi())
C1.__radius=10
print(C1.__radius)
print(C1.privateperi())
'''
'''
print(C1.privateperi())
C1._Circle__radius=10
print(C1.privateperi())
'''
#inhertence
'''
import math
class Circle:
    def __init__(self,r):
        self.radius=r
        self.type="Circle"
    def perimeter(self):
        a=2*self.radius*math.pi
        return a
    def area(self):
        a=self.radius**2*math.pi
        return a
class Comp(Circle):
    name='l'
    def __init__(self,so,r):
        #super().__init__(r) #both will work
        Circle.__init__(self,r)
        self.so=so
    @staticmethod
    def hello():
        print('hello')
    @classmethod
    def change(cls):
        cls.name='o'
    @property
    def namaste(self):
        print('namse',self.so*2)
C1=Circle(7)
comp1=Comp(1,7)
print(comp1.so)
print(comp1.radius)
print(comp1.hello())
print(Comp.hello())
print(comp1.name)
print(Comp.name)
comp1.change()
print(Comp.name)
print(Comp.namaste)
print(comp1.namaste)
comp1.so=3
print(comp1.namaste)
'''
