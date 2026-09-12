# class Complete graph
class Complete_Graph_Adjacent_matrix:
    def __init__(self):
        self.__matrix=[]
        self.__no_of_vertex=0
    
    def is_complete(self):
        mat=self.__matrix

        if self.__no_of_vertex==1:
            print("Given graph is a Complete Graph")
            return
        
        if mat==[]:
            print("No Graph Feeded")
            return
            
        for i in range(self.__no_of_vertex):
            for j in range(self.__no_of_vertex):
                if i==j and mat[i][j]!=0:
                        print("Given graph is not a Complete Graph")
                        return
                elif i!=j and mat[i][j]!=1:
                        print("Given graph is not a Complete Graph")
                        return
        print("Given graph is a Complete Graph")
    
    def setgraph(self,v):
        mat=[]
        if v==1:
            print("Graph not needed")
            self.__no_of_vertex=v
            return
        
        for i in range(1,v+1):
            row=[]
            for j in range(1,v+1):
                n=int(input("Enter the value(0/1) vertex("+str(i)+","+str(j)+"):"))
                row.append(n)
            mat.append(row)

        self.__matrix=mat
        self.__no_of_vertex=v
    
    # Display function
    def getadjacentmatrix(self):
        return self.__matrix
                
def main():
    G=Complete_Graph_Adjacent_matrix()

    # Menu Driven Program
    while True:
        print("\n\tCheck on Graph by Adjacent Matrix")
        print("1.Enter Graph by Matrix.\n2.Check Complete Graph. \n3.Quit.")
        x=input("Enter your choice(1/2/3..):")

        if x=="1":
            n=int(input("Enter Number of vertex:"))
            if n<=0:
                print("Cannot process")
                continue
            print()
            G.setgraph(n)
            print()
            if n==1:
                continue
            m=G.getadjacentmatrix()
            print("Graph in form of Adjacent Matrix:")
            print("[",end="")
            for i in range(n):
                print(" ",m[i],",")
            print("]\n")

        elif x=="2":
            G.is_complete()

        elif x=="3":
            print("..Exit..")
            break

        else:
            print("Enter Accordinly")

if __name__=="__main__":
    main()