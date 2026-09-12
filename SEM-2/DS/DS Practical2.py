# Class Relation
class RELATION:
    def __init__(self,relation,Set):
        self.__Set=RELATION.unique(Set)
        self.__Cardinality=len(self.__Set)
        self.__relation=RELATION.unique(relation)
        Mtr=RELATION.creatematrix(self.__relation,self.__Set,self.__Cardinality)
        self.__Mtr=Mtr

    def isReflexive(self):
        for i in range(self.__Cardinality):
                if self.__Mtr[i][i]!=1:
                    return False
        return True
    
    def isSymmtric(self):
        for i in range(self.__Cardinality):
            for j in range(self.__Cardinality):
                if self.__Mtr[i][j]==1 and self.__Mtr[j][i]!=1:
                    return False
        return True
    
    def isAntisymmtric(self):
        for i in range(self.__Cardinality):
            for j in range(self.__Cardinality):
                if self.__Mtr[i][j]==1 and self.__Mtr[j][i]==1 and i!=j:
                    return False
        return True
    
    def isTransitive(self):
        for i in range(self.__Cardinality):
            for j in range(self.__Cardinality):
                if self.__Mtr[i][j]==1:
                    for k in range(self.__Cardinality):
                        if self.__Mtr[j][k]==1 and self.__Mtr[i][k]!=1:
                            return False
        return True
    
    def Type(self):
        if self.isReflexive() and self.isSymmtric() and self.isTransitive():
            return "Equivalent Relation"
        elif self.isReflexive() and self.isAntisymmtric() and self.isTransitive():
            return "Partial Order Relation"
        else:
            return "None"
    
    # Extra Functions
    def unique(data):
        el=[]
        for i in data:
            if i not in el:
                el.append(i)
        return el
    
    def creatematrix(relation,Set,card):
        mtr=[]
        for i in range(card):
            row=[]
            for j in range(card):
                row.append(0)
            mtr.append(row)
        for a,b in relation:
            i=Set.index(a)
            j=Set.index(b)
            mtr[i][j]=1
        return mtr
    
    def getset(self):
        return self.__Set
    
    def getrelation(self):
        return self.__relation
    
    def getmatrixform(self):
        return self.__Mtr
    
    def getCardinality(self):
        return self.__Cardinality

def main():
    # Taking value
    s=eval(input("Enter the Set on which relation is declared:"))
    while True:
        r=eval(input("Enter the relation:"))
        for a,b in r:
            if a not in s or b not in s:
                print("Entered element does not match with set\n")
                break
        else:
            break
    
    # Display
    R=RELATION(r,s)
    print("Set:",R.getset())
    print("Relation:",R.getrelation())
    print("Relation in form of matrix(R):")
    m=R.getmatrixform()
    c=R.getCardinality()
    print("[",end="")
    for i in range(c):
        print(" ",m[i],",")
    print("]\n")
    
    # Menu Driven Program
    while True:
        print("\tRELATION Menu")
        print("1.Check Reflexive.\n2.Check Symmtric.\n3.Check Anti-Symmtric.\n4.Check Transitive.\n5.Type of Relation.\n6.Quit")
        x=input("Enter your choice(1/2/3..):")

        if x=="1":
            if R.isReflexive():
                print("It is a Reflexive Relation","\n")
            else:
                print("It is not a Reflexive Relation","\n")

        elif x=="2":
            if R.isSymmtric():
                print("It is a Symmtric Relation","\n")
            else:
                print("It is not a Symmtric Relation","\n")

        elif x=="3":
            if R.isAntisymmtric():
                print("It is a Anti-Symmtric Relation","\n")
            else:
                print("It is not a Anti-Symmtric Relation","\n")

        elif x=="4":
            if R.isTransitive():
                print("It is a Transitive Relation","\n")
            else:
                print("It is not a Transitive Relation","\n")

        elif x=="5":
            print("Type of Relation:",R.Type(),"\n")

        elif x=="6":
            print("..Exit..")
            break

        else:
            print("Enter Accordinly\n")

if __name__=="__main__":
    main()