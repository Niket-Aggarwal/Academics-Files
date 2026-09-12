# Class set
class SET:
    Universal=[]

    def __init__(self,elements):
        self.__member=SET.unique(elements)
        self.__cardianality=len(self.__member)
        SET.Universal.extend(self.__member)
        SET.Universal=SET.unique(SET.Universal)

    def Ismember(self,element):
        if element in self.__member:
            return True
        else:
            return False
        
    def Powerset(self):
        element=self.__member
        if element==[]:        
            return SET([]).__member
        empty=SET([])
        dummypowerset=[empty]
        while element!=[]:
            num=element[0]
            element=element[1:]
            subset=[]
            for sub in dummypowerset:
                dump=sub.Union(SET([num])).__member
                subset.append(SET(list(dump)))
            dummypowerset=dummypowerset+subset
        powerset=[]
        for all in dummypowerset:
            powerset.append(all.__member)
        return powerset
    
    def Subset(self,Set):
        if Set in self.Powerset():
            return True
        else:
            return False
        
    def Union(self,B):
        data1=self.__member
        data2=B.__member
        union=[]
        for i in data1:
            if i not in union:
                union.append(i)
        for j in data2:
            if j not in union:
                union.append(j)
        return SET(union)
    
    def Intersection(self,B):
        data1=self.__member
        data2=B.__member
        l1=self.__cardianality
        l2=B.__cardianality
        intersection=[]
        if l1>l2:
            A=data1
            C=data2
            x=l1
        else:
            A=data2
            C=data1
            x=l2
        for i in range(x):
            if A[i] not in intersection and A[i] in C:
                intersection.append(A[i])
        return SET(intersection)
    
    def Compliment(self):
        data1=self.__member
        compliment=[]
        for i in SET.Universal:
            if i not in data1:
                compliment.append(i)
        return SET(compliment)
    
    def Difference(self,B):
        data1=self.__member
        data2=B.__member
        differ=[]
        for i in data1:
            if i not in data2:
                differ.append(i)
        return SET(differ)
    
    def SymmetricDifference(self,B):
        data1=SET(self.Difference(B).__member)
        data2=SET(B.Difference(self).__member)
        sym=SET(data1.Union(data2).__member)
        return sym
    
    def CartesianProduct(self,second):
        A=self.__member
        B=second.__member
        if A==[] or B==[]:
            return SET([])
        product=[]
        for i in range(len(A)):
            for j in range(len(B)):
                product.append((A[i],B[j]))
        return SET(product)
    
    # Extra Function
    def unique(data):
        el=[]
        for i in data:
            if i not in el:
                el.append(i)
        return el
    
    def getelement(self):
        return self.__member
    
    def getcardianality(self):
        return self.__cardianality

# Taking input
def inp(n):
    while True:
        a=input("Enter the elements of "+n+" separated by single space(Ex:1 2 3 4 5..)")
        l=a.split()
        for i in range(len(l)):
            if l[i].isdigit():
                l[i]=int(l[i])
        else:
            return l
        
# Menu driven program
def main():
    A=SET(inp("Set A"))
    B=SET(inp("Set B"))
    print("Universal Set:",SET.Universal)
    print("Set A:",A.getelement(),"\t","Cardianality of A",A.getcardianality())
    print("Set B:",B.getelement(),"\t","Cardianality of B",B.getcardianality(),"\n")

    while True:
        print("\tSET Menu")
        print("1.Check a element exist in sets.\n2.Find Powerset of sets.\n3.Check subset in the sets.\n4.Union of two set.\n5.Intersection of two set.\n6.Difference of two set.\n7.Symmetric Difference of two set.\n8.Compliment of both set.\n9.Cartesian Product of set.\n10.Quit")
        x=input("Enter your choice(1/2/3..):")

        if x=="1":
            a=input("Enter element:")
            if a.isdigit():
                a=int(a)
            print(a,"in A:",A.Ismember(a))
            print(a,"in B:",B.Ismember(a),"\n")

        elif x=="2":
            print("Powerset of A:\n",A.Powerset())
            print("Powerset of B:\n",B.Powerset(),"\n")

        elif x=="3":
            a=inp("Subset")
            print("Subset:",a)
            print("Powerset of A:",A.Subset(a))
            print("Powerset of B:",B.Subset(a),"\n")

        elif x=="4":
            print("Union:",A.Union(B).getelement(),"\n")

        elif x=="5":
            print("Intersection:",A.Intersection(B).getelement(),"\n")

        elif x=="6":
            print("Differnce(A-B):",A.Difference(B).getelement())
            print("Differnce(B-A):",B.Difference(A).getelement(),"\n")

        elif x=="7":
            print("Symmetric Difference(A⊕B):",A.SymmetricDifference(B).getelement())
            print("Symmetric Difference(B⊕A):",B.SymmetricDifference(A).getelement(),"\n")

        elif x=="8":
            print("Compliment of A:",A.Compliment().getelement())
            print("Compliment of B:",B.Compliment().getelement(),"\n")

        elif x=="9":
            print("Cartesian Product (AXB):\n",A.CartesianProduct(B).getelement())
            print("Cartesian Product (BXA):\n",B.CartesianProduct(A).getelement(),"\n")

        elif x=="10":
            print("..Exit..")
            break

        else:
            print("Enter Accordingly\n")
            
if __name__=="__main__":
    main()