class Polynomial:
    def __init__(self, coeffs,degree):
        self.__coeffs=coeffs
        self.__degree=degree

    def evaluate(self, x):
        if self.__coeffs==[]:
            print("Polynomial not found\n")
            return
        result = 0
        l=self.__coeffs
        d=self.__degree
        for i in range(len(l)):
            result+=(x**d)*l[i]
            d-=1
        print("Result:",result,"\n")
    
    def display(self):
        if self.__coeffs==[]:
            print("Polynomial not found\n")
            return
        print("Equation: ",end="")
        poly=''
        l=self.__coeffs
        d=self.__degree
        for i in range(len(l)):
            if d>1:
                poly+=str(l[i])+"x^"+str(d)+" + "
            elif d==1:
                poly+=str(l[i])+"x + "
            else:
                poly+=str(l[i])+" + "
            d-=1
        poly=poly[:len(poly)-3]
        print(poly)

# Menu driven program
def main():
    d=int(input("Enter the Degree of polynomial:"))
    l=[]
    for i in range(d,-1,-1):
        a=int(input("Enter the coefficient of x raise to power "+str(i)+" : "))
        l.append(a)
    P=Polynomial(l,d)
    print()

    while True:
        print("\tPolynomial Menu")
        print("1.Change Polynomial.\n2.Enter x.\n3.Exit.")
        P.display()
        x=input("Enter your choice(1/2/3..):")
        if x=="1":
            print("..Changing Polynomial..")
            d=int(input("Enter the Degree of polynomial:"))
            l=[]
            for i in range(d,-1,-1):
                a=int(input("Enter the coefficient of x raise to power "+str(i)+" : "))
                l.append(a)
            P=Polynomial(l,d)
            print()

        elif x=="2":
            y=int(input("Enter x: "))
            P.evaluate(y)

        elif x=="3":
            print("..Exit..")
            break

        else:
            print("Enter Accordingly\n")
            
if __name__=="__main__":
    main()