#include <iostream>
#include <cmath>
#include <fstream>
#include <string>
using namespace std;


// Some common functions
void inp(int arr[], int n){
    int j = 1;
    for (int i = 0; i < n; i++){
        cout << "Element " << j << ":";
        cin >> arr[i];
        j++;
    }
    return;
}
void display(int a[], int x){
    cout << "Array:";
    for ( int i = 0; i < x; i++)
    {
        cout << a[i] << " ";
    }
    cout << endl;
    return;
}


// Q1
// int main(int argc, char *a[]){
//     cout << "To calculate sum of the given series of n terms" << endl;
//     int n;
//     if (argc > 1){
//         n = stoi(a[1]);
//         if (n <= 0){
//             cout << "Command line argument is negative" << endl;
//             do{
//                 cout << "Enter the number of terms (must be integer greater than 0):";
//                 cin >> n;
//             } while (n <= 0);
//         }
//     }else{
//         do{
//             cout << "Enter the number of terms (must be integer greater than 0):";
//             cin >> n;
//         } while (n <= 0);
//     }
//     cout << endl;
//     double sum = 0, term = 0;
//     int m = 1;
//     for (int i = 1; i <= n; i++){
//         term = (1.0 / pow(i, i)) * m;
//         m *= -1;
//         sum += term;
//     }
//     cout << "Sum of first " << n << " terms of series is: " << sum;
//     return 0;
// }


// Q2
// int main(){
//     cout << "To remove the duplicate elements from an array" << endl;
//     int n;
//     do{
//         cout << "Enter the no. of elements in array (must be integer greater than 0):";
//         cin >> n;
//     } while (n <= 0);
//     int arr[n];
//     inp(arr, n);
//     cout << endl;
//     cout << "Initial Array:" << endl;
//     display(arr, n);
//     int a;
//     for (int i = 0; i < n; i++){
//         for (int j = i + 1; j < n; j++){
//             if (arr[j] == arr[i]){
//                 for (int k = j; k < n - 1; k++)
//                     arr[k] = arr[k + 1];
//                 n--;
//                 j--;
//             }
//         }
//     }
//     cout << endl;
//     cout << "Array after removing duplicate elements:" << endl;
//     display(arr, n);
//     return 0;
// }


// Q3
// int main(int argc, char* argv[]){
//     cout << "Finding occurence of alphabet in command line argument"<<endl;
//     char* str;
//     if (argc ==  1){
//         cout << "No Command line argument given"<<endl;
//         return 1;
//     }else {
//         str = argv[1];
//     }
//     cout << "Given String: " << argv[1] << endl << endl;
//     int c;
//     for (int i = 0; str[i]!='\0'; i++){
//         c=0;
//         for(int j = 0; str[j]!='\0'; j++){
//             if (str[i] == str[j]){
//                 c++;
//             }
//         }
//         cout << "Alphabet " << str[i] <<" occur " << c << " time in string" << endl;        
//     }
//     return 0;
// }


// Q4
// void address(char str[]){
//     cout << "For String :" << str;
//     for (int i = 0; str[i]!='\0'; i++){
//         cout << "Address of the character " << str[i] << " is:" << (void*)&str[i] << endl;
//     }
//     return;
// }
// void concat(char str1[], char str2[]){
//     char str3[50];
//     int i;
//     for (i = 0; str1[i]!='\0'; i++){
//         str3[i] = str1[i];
//     }
//     for (int j = 0; str2[j]!='\0'; j++){
//         str3[i] = str2[j];
//         i++;
//     }
//     str3[i]='\0';
//     cout << "New string:" << str3;
//     return;
// }
// void compare(char str1[], char str2[]) {
//     int i = 0;
//     while (str1[i] != '\0' && str2[i] != '\0') {
//         if (str1[i] < str2[i]) {
//             cout << str1 << " comes first in dictionary";
//             return;
//         }else if(str1[i] > str2[i]){
//             cout << str2 << " comes first in dictionary";
//             return;
//         }
//         i++;
//     }
//     cout << "Bothe are equal";
//     return;
// }
// int length(char str[]){
//     char *pr = str;
//     int c=0;
//     while (*pr!='\0'){
//         c++;
//         pr++;
//     }
//     return c;
// }
// void upper(char str[]){
//     char res[20];
//     int j;
//     for (j = 0; str[j]!='\0'; j++){
//         if (str[j] >= 'a' && str[j] <= 'z'){
//             res[j]=str[j]-32;
//         }else{
//             res[j]=str[j];
//         }
//     }
//     res[j]='\0';
//     cout << str << " after Uppercase " << res;
//     return;
// }
// void reverse(char str[]){
//     char res[20];
//     int i=0;
//     for (int j = (length(str)-1);j != -1; j--){
//         res[i]=str[j];
//         i++;
//     }
//     res[i]='\0';
//     cout << str << " after Reversing " << res;
//     return ;
// }
// void insert(char str1[], char str2[], int x){
//     char str3[50];
//     int i=0;
//      for (int k = 0; str1[k] != '\0'; k++){
//         if (k == x){
//             for (int j = 0; str2[j] != '\0'; j++){
//                 str3[i++] = str2[j];
//             }
//         }
//         str3[i++] = str1[k];
//     }
//     str3[i]='\0';
//     cout << "New string:" << str3;
//     return;
// }
// int main(){
//     cout << "Enter string for string operations" << endl;
//     char str1[20];
//     cout << "Enter a string1: ";
//     cin >> str1;
//     char str2[20];
//     cout << "Enter a string2: ";
//     cin >> str2;
//     cout << endl;
//     while (true){
//         cout << "\tMenu for string operation" << endl;
//         cout << "1.Show address of each character in string\n2.Concatenate two strings\n3.Compare two strings\n4.Calculate length of the string (use pointers)\n5.Convert all lowercase characters to uppercase\n6.Reverse the string\n7.Insert a string in another string at a user specified position\n8.Exit";
//         int x;
//         cout << endl;
//         cout << "Enter your choice:";
//         cin >> x;
//         switch (x){
//             case 1:
//                 address(str1);
//                 cout << endl;
//                 address(str2);
//                 break;
//             case 2:
//                 concat(str1,str2);
//                 break;
//             case 3:
//                 compare(str1,str2);
//                 break;
//             case 4:
//                 cout << "Length of " << str1 << " is:" << length(str1);
//                 cout << endl;
//                 cout << "Length of " << str2 << " is:" << length(str2);
//                 break;
//             case 5:
//                 upper(str1);
//                 cout << endl;
//                 upper(str2);
//                 break;
//             case 6:
//                 reverse(str1);
//                 cout << endl;
//                 reverse(str2);
//                 break;
//             case 7:
//                 int y;
//                 cout << "Enter the index:";
//                 cin >> y;
//                 insert(str1,str2,y);
//                 break;
//             case 8:
//                 cout << "..EXIT..";
//                 break;
//             default:
//                 cout << "Enter Accordinly";
//                 break;
//         }
//         if (x==8){
//             break;
//         }
//         cout << endl << endl;
//     }
//     return 0;
// }


// Q5
// int main(){
//     cout << "To merge two ordered Arrays" << endl;
//     int n1, n2;
//     do{
//         cout << "Enter the no. of elements in array1 (must be integer greater than 0):";
//         cin >> n1;
//     } while (n1 <= 0);
//     int arr1[n1];
//     inp(arr1, n1);
//     cout << endl;
//     do{
//         cout << "Enter the no. of elements in array2 (must be integer greater than 0):";
//         cin >> n2;
//     } while (n2 <= 0);
//     int arr2[n2];
//     inp(arr2, n2);
//     cout << endl;
//     cout << "Two ordered arrays are:" <<endl;
//     display(arr1, n1);
//     display(arr2, n2);
//     cout << endl;
//     int merge[n1 + n2];
//     int i = 0, j = 0, k = 0;
//     while (i < n1 && j < n2){
//         if (arr1[i] < arr2[j]){
//             merge[k++] = arr1[i++];
//         }else{
//             merge[k++] = arr2[j++];
//         }
//     }
//     while (i < n1){
//         merge[k++] = arr1[i++];
//     }
//     while (j < n2){
//         merge[k++] = arr2[j++];
//     }
//     cout << "Array after merge:" << endl;
//     cout << "Array:";
//     for (i = 0; i < n1 + n2; i++){
//         cout << merge[i] << " ";
//     }
//     return 0;
// }


// Q6
// (a) With Recursion
// void Binarysearch(int arr[], int a, int l, int h){
//     int mid = (l + h) / 2;
//     if (l > h){
//         cout << "Element not found";
//         return;
//     }
//     if (arr[mid] == a){
//         cout << "Element " << a << " found at index " << mid << endl;
//         return;
//     }else if (arr[mid] > a){
//         h = mid - 1;
//     }else{
//         l = mid + 1;
//     }
//     Binarysearch(arr, a, l, h);
// }
// int main(){
//     cout << "To find an element by Binary Search" << endl;
//     int n, a;
//     do{
//         cout << "Enter the no. of elements in array(must be integer greater than 0 and sorted in ascending order):";
//         cin >> n;
//     } while (n <= 0);
//     int arr[n];
//     inp(arr, n);
//     cout << endl;
//     display(arr, n);
//     cout << endl;
//     cout << "Enter elements to search:";
//     cin >> a;
//     int l = 0;
//     int h = n - 1;
//     Binarysearch(arr, a, l, h);
//     return 0;
// }
// (b) Without Recursion 
// int main(){
//     cout << "To find an element by Binary Search" << endl;
//     int n, a;
//     do{
//         cout << "Enter the no. of elements in array(must be integer greater than 0 and sorted in ascending order):";
//         cin >> n;
//     } while (n <= 0);
//     int arr[n];
//     inp(arr, n);
//     cout << endl;
//     display(arr, n);
//     cout << endl;
//     cout << "Enter elements to search:";
//     cin >> a;
//     int l = 0;
//     int h = n - 1;
//     int mid = (l + h) / 2;
//     while (l <= h){
//         if (arr[mid] == a){
//             cout << "Element " << a << " found at index " << mid << endl;
//             break;
//         }else if (arr[mid] > a){
//             h = mid - 1;
//         }else{
//             l = mid + 1;
//         }
//         mid = (l + h) / 2;
//     }
//     if (l > h){
//         cout << "Element not found";
//     }
//     return 0;
// }


// Q7
// (a) With Recursion
// void GCD(int a, int b, int i = 2, int j = 1){
//     if (a == 1 && b == 1){
//         cout << "GCD of the number " << a << " and " << b << " is:" << j;
//         return;
//     }
//     if (a < 0)
//         a = -a;
//     if (b < 0)
//         b = -b;
//     if (i > a || i > b){
//         cout << "GCD of the number " << a << " and " << b << " is:" << j;
//         return;
//     }
//     if (a % i == 0 && b % i == 0){
//         j = i;
//     }
//     GCD(a, b, i + 1, j);
// }
// int main(){
//     cout << "To calculate the GCD of two numbers (number cannot be zero)" << endl;
//     int a, b;
//     do{
//         cout << "Enter number1:";
//         cin >> a;
//     } while (a == 0);
//     do{
//         cout << "Enter number2:";
//         cin >> b;
//     } while (b == 0);
//     cout << endl;
//     GCD(a, b);
//     return 0;
// }
// (b) Without Recursion 
// int main(){
//     cout << "To calculate the GCD of two numbers (number cannot be zero)" << endl;
//     int a, b;
//     do{
//         cout << "Enter number1:";
//         cin >> a;
//     } while (a == 0);
//     do{
//         cout << "Enter number2:";
//         cin >> b;
//     } while (b == 0);
//     cout << endl;
//     if (a < 0)
//         a = -a;
//     if (b < 0)
//         b = -b;
//     int i = 2, j = 1;
//     while (i <= a && i <= b){
//         if (a == 1 && b == 1){
//             break;
//         }
//         if (a % i == 0 && b % i == 0){
//             j = i;
//         }
//         i++;
//     }
//     cout << "GCD of the number " << a << " and " << b << " is:" << j;
//     return 0;
// }


// Q8
// class Matrix {
//     private:
//         int row, col;
//         int mat[10][10];
//     public:
//         Matrix(int r, int c, bool skip=false) {
//             row = r;
//             col = c;
//             if (skip){
//                 return;
//             }
//             for(int i = 0; i < r; i++){
//                 for(int j = 0; j < c; j++){
//                     cout << "Enter element (" << i+1 << "," << j+1 << "): ";
//                     cin >> mat[i][j];
//                 }
//             }
//             cout << "Matrix Created!!" << endl << endl;
//         }
//         void Sum(Matrix other){
//             if (this->row == other.row && this->col == other.col){
//                 int r = other.row;
//                 int c = other.col;
//                 Matrix S(r, c, true);
//                 for(int i = 0; i < r; i++){
//                     for(int j = 0; j < c; j++){
//                         S.mat[i][j] = (this->mat[i][j] + other.mat[i][j]);
//                     }
//                 }
//                 S.Display();
//             }else {
//                 throw "Not Compatible";
//                 // cout << "Not compatible" << endl << endl;
//             }
//         }
//         void Product(Matrix other){
//             if (this->col == other.row){
//                 int r1 = this->row;
//                 int k = other.row;
//                 int c2 = other.col;
//                 Matrix S(r1, c2,true);
//                 for(int i = 0; i < r1; i++){
//                     for(int j = 0; j < c2; j++){
//                         S.mat[i][j]=0;
//                         for(int K = 0; K < k; K++){
//                             S.mat[i][j] += this->mat[i][K] * other.mat[K][j];
//                         }
//                     }
//                 }
//                 S.Display();
//             }else {
//                 throw "Not Compatible";
//                 // cout << "Not compatible" << endl << endl;
//             }
//         }
//         void Transpose(){
//             int r = this->row;
//             int c = this->col;
//             Matrix S(c, r, true);
//             for(int i = 0; i < r; i++){
//                 for(int j = 0; j < c; j++){
//                     S.mat[j][i] = this->mat[i][j];
//                 }
//             }
//             S.Display();
//         }
//         void Display(){
//             int r = this->row;
//             int c = this->col;
//             cout << "[ " << endl;
//             for(int i = 0; i < r; i++){
//                 for(int j = 0; j < c; j++){
//                     cout << this->mat[i][j] << " ";
//                 }
//                 cout << endl;
//             }
//             cout << "]" << endl << endl;
//         }
// };
// int main(){
//     cout << "Enter the Matrix for Matrix Operation" << endl << endl;
//     int r,c;
//     cout << "Enter Row for Matrix 1:";
//     cin >> r;
//     cout << "Enter Column for Matrix 1:";
//     cin >> c;
//     Matrix m1(r,c);
//     cout << "Enter Row for Matrix 2:";
//     cin >> r;
//     cout << "Enter Column for Matrix 2:";
//     cin >> c;
//     Matrix m2(r,c);
//     cout << "m1:" << endl;
//     m1.Display();
//     cout << "m2:" << endl;
//     m2.Display();
//     while (true){
//         cout << "\tMatrix Operations" << endl;
//         cout << "1.Sum\n2.Product\n3.Transpose\n4.Exit";
//         int x;
//         cout << endl;
//         cout << "Enter your choice:";
//         cin >> x;
//         switch (x){
//             case 1:
//                 try{
//                     m1.Sum(m2);
//                 }catch(const char *msg){
//                     cout << msg << endl << endl;
//                 }
//                 break;    
//             case 2:
//                 try{
//                     m1.Product(m2);    
//                 }catch(const char *msg){
//                     cout << msg << endl << endl;
//                 }
//                 break;    
//             case 3:
//                 cout << "Transpose of m1";
//                 m1.Transpose();
//                 cout << "Transpose of m2";
//                 m2.Transpose();
//                 break;
//             case 4:
//                 cout << "..EXIT..";
//                 break;
//             default:
//                 cout << "Enter Accordinly";
//                 break;
//         }
//         if (x==4){
//             break;
//         }
//         cout << endl << endl;
//     }
//     return 0;
// }


// Q9
// class Person{
//     protected:
//         string Name;
//     public:
//         Person(string nam){
//             Name=nam;
//         }
//         void Display(){
//             cout << "Name: " << Name << endl;
//             cout << "From Person Class..." << endl;
//             return;
//         }
// };
// class Student: public Person{
//     private:
//         string Course;
//         float Marks;
//         int Years;
//     public:
//         Student(string nam, string co, float m, int y):Person(nam){
//             Course=co;
//             Marks=m;
//             Years=y;
//         }
//         void Display(){
//             cout << "Name: " << Name << endl;
//             cout << "Course: " << Course << endl;
//             cout << "Marks: " << Marks << endl;
//             cout << "Years: " << Years << endl;
//             cout << "From Student Class..." << endl;
//             return;
//         }
// };
// class Employee: public Person{
//     private:
//         string Department;
//         float Salary;
//     public:
//         Employee(string nam, string dep, float sal):Person(nam){
//             Department=dep;
//             Salary=sal;
//         }
//         void Display(){
//             cout << "Name: " << Name << endl;
//             cout << "Department: " << Department << endl;
//             cout << "Salary: " << Salary << endl;
//             cout << "From Employee Class..." << endl;
//             return;
//         }
// };
// int main(){
//     cout << "Anaylsis Ploymorphism" << endl;
//     Person P1("Niket");
//     P1.Display();
//     cout << endl;
//     Student S1("Niket","B.Sc. (H) CS",99.9,1);
//     S1.Display();
//     cout << endl;
//     Employee E1("Niket","Tech Department",100000.00);
//     E1.Display();
//     cout << endl;
//     return 0;
// }


// Q10
// class Triangle{
//     private:
//         int a, b, c;
//     public:
//         Triangle(int x, int y, int z){
//             if (x <= 0 || y <= 0 || z <= 0){
//                 throw "Sides must be greater than 0";
//             }
//             if (!(x+y>z && y+z>x && z+x>y)){
//                 throw "Invalid triangle (triangle inequality failed)";
//             }
//         a=x;
//         b=y;
//         c=z;
//     }
//     void area(bool x){
//         cout << "Area of right angles triangle with" << endl;
//         cout << "Base:" << b << endl;
//         cout << "Height:" << a << endl;
//         cout << "Area:" << 0.5*a*b << endl;
//         return;
//     }
//     void area(){
//         double s=(a+b+c)/2.0;
//         cout << "Area:" << sqrt(s*(s-a)*(s-b)*(s-c)) << endl;
//     }
// };
// int main(){
//     cout << "Enter the side of triangle to compute the area" << endl;
//     int x, y, z;
//     cout << "Enter side1:";
//     cin >> x;
//     cout << "Enter side2:";
//     cin >> y;
//     cout << "Enter side3:";
//     cin >> z;
//     try{
//         char u;
//         Triangle T(x, y, z);
//         cout << "Is the triangle is Right angles?(T/any):";
//         cin >> u;
//         cout << endl;
//         if(u=='T'){
//             T.area(true);
//         }else{
//             T.area();
//         }
//     }
//     catch (const char* msg){
//         cout << "Exception: " << msg << endl;
//     }
//     return 0;
// }


// Q11
// class Student{
//     public:
//         int Rollno;
//         string Name;
//         int Class;
//         float Total_Marks;
//         int Years;
//         Student(){}
//         Student(int r,string nam, int c, float m, int y){
//             Rollno=r;
//             Name=nam;
//             Class=c;
//             Total_Marks=m;
//             Years=y;
//         }
//         void Display(){
//             cout << "Rollno: " << Rollno << endl;
//             cout << "Name: " << Name << endl;
//             cout << "Class: " << Class << endl;
//             cout << "Total Marks: " << Total_Marks << endl;
//             cout << "Years: " << Years << endl;
//             return;
//         }
// };
// int main(){
//     Student S1;
//     int r,c,y;
//     string nam;
//     float m;
//     ofstream infile("C:\\Users\\Niket\\Documents\\B.Sc. (H) C.S\\SEM-2\\C++\\students.txt");
//     cout << "Entering data of 5 students and storing in text file" << endl;
//     for (int i=1; i<6; i++){
//         cout << "Enter details of student " << i << endl;
//         cout << "Rollno: ";
//         cin >> r;
//         cout << "Name: ";
//         cin >> nam;
//         cout << "Class: ";
//         cin >> c;
//         cout << "Total Marks: ";
//         cin >> m;
//         cout << "Years: ";
//         cin >> y;
//         Student S1(r,nam,c,m,y);
//         infile << S1.Rollno << " " << S1.Name << " " << S1.Class << " " << S1.Total_Marks << " " << S1.Years << "\n";
//         cout << "Details of Student " << i << " is added" << endl << endl;
//     }
//     infile.close();
//     cout << "Getting back Student Records from text file" << endl;
//     ifstream outfile("C:\\Users\\Niket\\Documents\\B.Sc. (H) C.S\\SEM-2\\C++\\students.txt");
//     int i=1;
//     while (outfile >> S1.Rollno >> S1.Name >> S1.Class >> S1.Total_Marks >> S1.Years){
//         cout << "Details of student " << i << endl;
//         S1.Display();
//         cout << endl;
//         i++;
//     }
//     outfile.close();
//     return 0;
// }


// Q12
// int main(){
//     cout << "Simple file Handling" << endl;
//     cout << "Entering data and saving in text file one" << endl;
//     ofstream infile1("C:\\Users\\Niket\\Documents\\B.Sc. (H) C.S\\SEM-2\\C++\\sample1.txt");
//     string data;
//     cout << "Enter:";
//     getline(cin, data);
//     infile1 << data;
//     cout << "Data stored" << endl << endl;
//     infile1.close();
//     cout << "Copy data from one to another after removing space" << endl;
//     ifstream outfile1("C:\\Users\\Niket\\Documents\\B.Sc. (H) C.S\\SEM-2\\C++\\sample1.txt");
//     ofstream infile2("C:\\Users\\Niket\\Documents\\B.Sc. (H) C.S\\SEM-2\\C++\\sample2.txt");
//     string updated;
//     getline(outfile1, data);
//     for( char ch : data){
//         if (ch !=' '){
//             updated = updated + ch;
//         }
//     }
//     infile2 << updated;
//     cout << "Updated Data stored" << endl << endl;
//     return 0;
// }