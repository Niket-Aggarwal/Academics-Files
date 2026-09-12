class BruteForce:
    def __init__(self,n,C):
        self.__number=n
        self.__sum=C
        l=[]
        for i in range(C+1):
            l.append(i)
        self.__List=l
    
    def Apply(self):
        element=self.__List
        result=[[]]
        n=self.__number
        for i in range(n):
            demo = []
            for temp in result:
                for num in element:
                    demo.append(temp + [num])
            result = demo

        final=[]
        for i in result:
            s=0
            for j in i:
                s+=j
            if s==self.__sum:
                final.append(i)
        return final
    
# Menu driven program
def main():
    n=int(input("Enter number of variable:"))
    while True:
        c=int(input("Enter the sum C:"))
        if c<=10:
            break
        print("Enter C less than equal to 10\n")
    BF=BruteForce(n,c)
    print()

    while True:
        print("\tBruteForce Menu")
        print("1.Change data.\n2.Start.\n3.Exit.")
        x=input("Enter your choice(1/2/3..):")

        if x=="1":
            print("..Changing Polynomial..")
            n=int(input("Enter number of variable:"))
            c=int(input("Enter the sum C:"))
            if c>10:
                print("Enter C less than equal to 10\n")
                continue
            BF=BruteForce(n,c)
            print()

        elif x=="2":
            res=BF.Apply()
            print("The combinations of the variables are:")
            for i in res:
                print(i)
            print()

        elif x=="3":
            print("..Exit..")
            break

        else:
            print("Enter Accordingly\n")
            
if __name__=="__main__":
    main()