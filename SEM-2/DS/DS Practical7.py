# class Directed Graph
class DirectedGraph:
    def __init__(self):
        self.__vertex=0
        self.__adjacent=[]

    def setgraph(self,v):
        if v==0:
            print("Enter Graph first\n")
            return
        self.__vertex=v
        for i in range(1,self.__vertex+1):
            row=[]
            for j in range(1,self.__vertex+1):
                n=int(input("Does edge between vertex "+str(i)+" to "+str(j)+":"))
                row.append(n)
            self.__adjacent.append(row)

    def compute_degrees(self):
        if self.__vertex==0:
            print("Enter Graph first\n")
            return
        in_degree=[0]*self.__vertex
        out_degree=[0]*self.__vertex
        for i in range(self.__vertex):
            for j in range(self.__vertex):
                if self.__adjacent[i][j]==1:
                    out_degree[i]+=1
                    in_degree[j]+=1
        return in_degree, out_degree
    
    # Display function
    def getadjacentmatrix(self):
        return self.__adjacent
    
    def getvertex(self):
        return self.__vertex
    
def main():
    G=DirectedGraph()

    # Menu driven program
    while True:
        print("\n\tFinding Degree in Directed Graph")
        print("1.Enter Graph by Matrix.\n2.Find degree. \n3.Quit.")
        x=input("Enter your choice(1/2/3..):")

        if x=="1":
            n=int(input("Enter Number of vertex:"))
            if n<=0:
                print("Cannot process")
                continue
            print()
            G.setgraph(n)
            print()

            m=G.getadjacentmatrix()
            print("Graph in form of Adjacent Matrix:")
            print("[",end="")
            for i in range(n):
                print(" ",m[i],",")
            print("]\n")

        elif x=="2":
            t=G.compute_degrees()
            v=G.getvertex()
            a=1

            for i in range(v):
                print("Vertex",a,"have indegree:",t[0][i],"and outdegree:",t[1][i])
                a+=1

        elif x=="3":
            print("..Exit..")
            break

        else:
            print("Enter Accordinly")
            
if __name__=="__main__":
    main()