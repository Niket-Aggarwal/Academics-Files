# Class Permutation
class Permutation:
    def __init__(self,digits):
        self.__List=Permutation.unique(digits)
        self.__Length=len(self.__List)
    
    def with_repetition(self,n):
        element=self.__List
        result=[""]
        for i in range(n):
            demo=[]
            for temp in result:
                for num in element:
                    demo.append(temp+str(num))
            result=demo
        return result
    
    def without_repetition(self,n):
        element=self.__List
        result = [""]
        for _ in range(n):
            demo=[]
            for temp in result:
                for num in element:
                    if str(num) not in temp:
                        demo.append(temp+str(num))
            result=demo
        return result
    
    # Extra Functions
    def unique(data):
        el=[]
        for i in data:
            if i not in el:
                el.append(i)
        return el
    
    def getdigits(self):
        return self.__List
    
    def getlen(self):
        return self.__Length

def main():
    # Taking digits
    while True:
        digits=eval(input("Enter the list of digits that will participate in Permutation:"))
        if digits==[]:
            print("Atleast have 1 element")
            continue
        break

    # Create
    Perm=Permutation(digits)

    # Menu Driven Program
    while True:
        print("\n\tPERMUTATION Menu")
        print("Digits in permutation are:",Perm.getdigits())
        print("1.With Repetition.\n2.Without Repetition. \n3.Quit.")
        x=input("Enter your choice(1/2/3..):")

        if x=="1":
            n=int(input("Enter Number of places in permutaion:"))
            if n<=0:
                print("Cannot process permutation")
                continue
            result=Perm.with_repetition(n)
            print("\nPermutations are:")
            for i in result:
                print(i)

        elif x=="2":
            n=int(input("Enter Number of places in permutaion:"))
            if n>Perm.getlen() or n<=0:
                print("Cannot process permutation")
                continue
            result=Perm.without_repetition(n)
            print("\nPermutations are:")
            for i in result:
                print(i)

        elif x=="3":
            print("..Exit..")
            break

        else:
            print("Enter Accordinly")

if __name__=="__main__":
    main()