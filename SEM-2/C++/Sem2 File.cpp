#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

// Ek extra bar run krega

// while(outfile.eof()==0){
//         getline(outfile,data);
//         cout << "Line " << i << ": "<< data << endl;
//         i++;
//     }

// Practise(Self)
void Learn()
{
    // Basic input output calculation

    // cout << "Hello world" << endl;
    // int a=10;
    // cout<<a;
    // float x=100.01;
    // cout<<x;
    // int c,d;
    // cout<<"Enter first"<<endl;
    // cin>>c;
    // cout<<"Enter second"<<endl;
    // cin>>d;
    // cout<< c+d; //here always +-*/ int only not self type casting
    // cout<< (float) c/d; //here always +-*/ int only not self type casting

    // if....else if .....else

    // if(10>11){
    //     cout<<"het";
    // }else{
    //     cout<<"don";
    // }
    // switch (10)
    // {
    // case 20:
    //     cout << "het";
    //     break;
    // case 10:
    //     cout << "hsvdvd";
    //     break;
    // default:
    //     cout << "hetdgdfbf";
    //     break;
    // }

    // loops

    // int i=1;
    // while (i<10){
    //     cout << "hetdgdfbf"<<endl;
    //     i=i+1;
    // }

    // array

    // int arr[]={1,2,3,4,5};
    // cout<<arr[0];
    // int arb[2][3]={{1,2,3},{4,5,8}};
    // cout<<arb[0][0];

    // 2D array coloum wise

    // int arr[2][3];
    // int a;
    // cout<<"Enter"<<endl;
    // for(int i=0;i<3;i++)
    // {
    //     for(int j=0;j<2;j++)
    //     {
    //       cin>>a;
    //       arr[j][i]=a;
    //     }
    // }
    // for(int i=0;i<2;i++)
    // {
    //     for(int j=0;j<3;j++)
    //     {
    //         cout<<arr[i][j]<<" ";
    //     }
    //     cout<<endl;
    // }

    // strings

    // string a="ds";
    // cout<<a;
    // cout<<a.length()<<endl;
    // cout<<a.substr(1,5);
    // cout<<a;

    // return ;
}

// Assignment1
void Assign1()
{
    // cout << "Numbers divisible by 7 and mutiple of 5 between 100 and 400 (included): ";
    // for (int i = 100; i <= 400; i++)
    // {
    //     if (i % 7 == 0 && i % 5 == 0)
    //     {
    //         cout << i << " ";
    //     }
    // }

    // cout << "Pattern" << endl;
    // for (int i = 0; i < 5; i++)
    // {
    //     for (int j = 0; j <= i; j++)
    //     {
    //         cout << "* ";
    //     }
    //     cout << "\n";
    // }
    // for (int i = 4; i > 0; i--)
    // {
    //     for (int j = 0; j < i; j++)
    //     {
    //         cout << "* ";
    //     }
    //     cout << "\n";
    // }

    // int n, even = 0, odd = 0;
    // do
    // {
    //     cout << "Enter a number:";
    //     cin >> n;
    //     if (n % 2 == 0)
    //     {
    //         even++;
    //     }
    //     else
    //     {
    //         odd++;
    //     }
    // } while (n >= 0);
    // cout << "Even number entered: " << even << endl;
    // cout << "Odd number entered: " << odd << endl;

    // int a = 0, b = 1;
    // int c;
    // cout << "Fibonacci series form 0 to 20:" << a << " " << b << " ";
    // while ((a + b) <= 20)
    // {
    //     cout << a + b << " ";
    //     c = a;
    //     a = b;
    //     b = b + c;
    // }

    // float a = 1, b = 3;
    // float term, sum;
    // while ((a < 100) && (b < 100))
    // {
    //     term = a / b;
    //     sum += term;
    //     a += 2;
    //     b += 2;
    // }
    // cout << "sum of series:" << sum;

    // return;
}

// Array and sorting
void sortmerge()
{
    // Printing

    // int a[5] = {1, 2, 3, 4, 5};
    // for (int i = 0; i <= 5; i++)
    // {
    //     cout << a[i] << endl;
    // }

    // Merge two sorted array that keep sorted

    // int a[] = {10, 20, 23, 45, 47, 89};
    // int b[] = {1, 12, 13, 40};
    // int n1 = sizeof(a) / sizeof(a[0]);
    // int n2 = sizeof(b) / sizeof(b[0]);
    // int c[n1 + n2];
    // int i = 0, j = 0, k = 0;
    // while (i < n1 && j < n2)
    // {
    //     if (a[i] < b[j])
    //         c[k++] = a[i++];
    //     else
    //         c[k++] = b[j++];
    // }
    // while (i < n1)
    //     c[k++] = a[i++];
    // while (j < n2)
    //     c[k++] = b[j++];
    // for (int x = 0; x < n1 + n2; x++)
    //     cout << c[x] << " ";

    // Type of sorting

    // (1).Bubble sort-- check adjacent elements largest at lright and repeat each time

    // int a[] = {45, 12, 89, 23, 5};
    // int n = sizeof(a) / sizeof(a[0]);
    // for (int i = 0; i < n - 1; i++) // main loop for each element
    // {
    //     for (int j = 0; j < n - i - 1; j++) // loop for adjacent check
    //     {
    //         if (a[j] > a[j + 1])
    //         {
    //             int temp = a[j];
    //             a[j] = a[j + 1];
    //             a[j + 1] = temp;
    //         }
    //     }
    // }
    // cout << "Sorted array: ";
    // for (int i = 0; i < n; i++)
    //     cout << a[i] << " ";

    // (2). select sort-- find smallest and swap it to its correct position

    // int a[] = {45, 12, 89, 23, 5};
    // int n = sizeof(a) / sizeof(a[0]);
    // for (int i = 0; i < n - 1; i++)
    // {
    //     int min = i;
    //     for (int j = i + 1; j < n; j++)
    //         if (a[j] < a[min])
    //             min = j;

    //     int temp = a[i];
    //     a[i] = a[min];
    //     a[min] = temp;
    // }
    // for (int x : a)
    //     cout << x << " ";

    // (3). insertion sort-- take each element in line and place correctly

    // int a[] = {45, 12, 89, 23, 5};
    // int n = sizeof(a) / sizeof(a[0]);
    // for (int i = 1; i < n; i++)
    // {
    //     int key = a[i];
    //     int j = i - 1;
    //     while (j >= 0 && a[j] > key)
    //     {
    //         a[j + 1] = a[j];
    //         j--;
    //     }
    //     a[j + 1] = key;
    // }
    // for (int i = 0; i < n; i++)
    //     cout << a[i] << " ";

    // (4).this sort automatically choose best one quick sort heap sort insertion sort
    // for thie algorithm is imported

    // int a[] = {45, 12, 89, 23, 5};
    // int n = sizeof(a) / sizeof(a[0]);
    // sort(a, a + n);
    // for (int x : a)
    //     cout << x << " ";

    // return ;
}

// Assignment2 (Prototype)
void Assign2();

// 1D array function
void input1D(int a[],int x){
    cout<<"Enter elements of array:"<<endl;
    int j=1;
    for(int i=0;i<x;i++){
        cout<<"Element "<<j<<":";
        cin>>a[i];
        j++;
    }
}
void display1D(int a[],int x){
    cout<<"Elements in array:";
    for(int i=0;i<x;i++){
        cout<<a[i]<<" ";
    }
}

// 2D array function
void input2D(int a[][5],int y,int z){
    int b=1;
    cout<<"Enter elements of array:"<<endl;
    for(int i=0;i<y;i++){
        int k=1;
        for(int j=0;j<z;j++){
            cout<<"Element ["<<b<<","<<k<<"]:";
            cin>>a[i][j];
            k++;
        }
        b++;
    }
}
void display2D(int a[][5],int y,int z){
    cout<<"Elements of array:"<<endl;
    int k=1;
    for(int i=0;i<y;i++){
        cout<<"Row"<<k<<":";
        for(int j=0;j<z;j++){
            cout<<a[i][j]<<" ";
        }
        cout<<endl;
        k++;
    }
}

// Reccursion
void fibonacci(int arr[],int n,int i=2){
    if (i>=n){
        return;
    }
    if (n<=0){
        cout<<"None";
        return;
    }else if(n==1){
        cout<<"0";
        return;
    }else if(n==2){
        cout<<" 0 1";
        return;
    }else{
        arr[i]=arr[i-1]+arr[i-2];
        fibonacci(arr,n,i+1);
    }
}
void prime(int n,int i=2){
    if (n<=1){
        cout<<"Cannot Check";
        return;
    }else{
        if(i==n){
            cout<<"Prime";
            return;
        }else if(n%i==0 && i!=n){
            cout<<"Not Prime";
            return;
        }
        prime(n,i+1);
    }
}
void GCD(int a,int b,int i=2,int j=1){
    if (a==0 || b==0){
        cout << "Cannot find";
        return;
    }else if (a==1 && b==1){
        cout<<j;
        return;
    }
    if (a<0)
        a=-a;
    if (b<0)
        b=-b;
    if (i>a || i>b){
        cout<<j;
        return;
    }
    if (a%i==0 && b%i==0){
        j=i;
    }
    i++;
    GCD(a,b,i,j);
}
int add(int a[],int n,int i=0){
    if (i==n){
        return 0;
    }else{
        return a[i]+add(a,n,i+1);
    }
}
void linearsearch(int ar[],int n,int x,int i=0){
    if (n==i){
        cout<<"No";
        return;
    }
    int a=ar[i];
    if (a>x){
        cout<<"No";
        return;
    }
    if (a==x){
        cout<<i;
        return;
    }
    linearsearch(ar,n,x,i+1);
}
void recursion(){
    // (1). Fibonacci series
    // int n;
    // cout<<"Enter how many terms:";
    // cin>>n;
    // int arr[n]={0,1};
    // fibonacci(arr,n);
    // display1D(arr,n);

    // (2) Prime no.
    // int n;
    // cout<<"Enter no.";
    // cin>>n;
    // prime(n);


    // (3) GCD
    // int n,m;
    // cout<<"Enter no.";
    // cin>>n;
    // cin>>m;
    // GCD(n,m);

    // (4) adding array of elements
    // int a[5]={1,2,3,4,5};
    // int n=5;
    // cout<<add(a,n);

    // (5) linear serach
    // int a[5]={1,3,5,7,9};
    // int n=5;
    // int y;
    // cin>> y;
    // linearsearch(a,n,y);
}

class base{
    public:
        void display(){
        cout << "base" <<endl;
    }
};

class derived:public base{
    public:
        void display(){
        cout << "derived" <<endl;
    }
};

// main function of all
int main()
{
    // Other
    Learn();
    Assign1();
    sortmerge();
    Assign2();

    // Array practise(1D)
    // int arr[5],x=5;
    // input1D(arr,x);
    // display1D(arr,x);

    // Array practise(2D)
    // int ARR[2][5],a=2,b=5;
    // input2D(ARR,a,b);
    // display2D(ARR,a,b);

    // Recursiuon
    recursion();
    base b;
    b.display();
    derived d;
    d.display();
    b=d;
    b.display();
    return 0;

}

// Assignment2
void Assign2()
{
    // int N, a;
    // int e = 0, o = 0;
    // cout << "Enter the No. of elements in the array: ";
    // cin >> N;
    // int arr[N];
    // for (int i = 0; i < N; i++)
    // {
    //     cout << "Enter element: ";
    //     cin >> a;
    //     if (a % 2 == 0)
    //         e++;
    //     else
    //         o++;
    //     arr[i] = a;
    // }
    // cout << "Array elements: ";
    // for (int i = 0; i < N; i++)
    //     cout << arr[i] << " ";
    // cout << endl;
    // while (true)
    // {
    //     int x;
    //     cout << "\n\tMenu"
    //          << "\n1. Create even & odd array"
    //          << "\n2. Sum and average"
    //          << "\n3. Maximum and minimum"
    //          << "\n4. Remove duplicate"
    //          << "\n5. Reverse array"
    //          << "\n6. Exit"
    //          << "\nEnter your choice: ";
    //     cin >> x;
    //     switch (x)
    //     {
    //     case 1:
    //     {
    //         int Even[e], Odd[o];
    //         int i = 0, j = 0;
    //         for (int k = 0; k < N; k++)
    //         {
    //             if (arr[k] % 2 == 0)
    //                 Even[i++] = arr[k];
    //             else
    //                 Odd[j++] = arr[k];
    //         }
    //         cout << "Even array: ";
    //         for (int i = 0; i < e; i++)
    //             cout << Even[i] << " ";
    //         cout << "\nOdd array: ";
    //         for (int i = 0; i < o; i++)
    //             cout << Odd[i] << " ";
    //         cout << endl;
    //         break;
    //     }
    //     case 2:
    //     {
    //         int sum = 0;
    //         for (int i = 0; i < N; i++)
    //             sum += arr[i];
    //         cout << "Sum: " << sum << endl;
    //         cout << "Average: " << (float)sum / N << endl;
    //         break;
    //     }
    //     case 3:
    //     {
    //         int min = arr[0], max = arr[0];
    //         for (int i = 1; i < N; i++)
    //         {
    //             if (arr[i] < min)
    //                 min = arr[i];
    //             if (arr[i] > max)
    //                 max = arr[i];
    //         }
    //         cout << "Minimum: " << min << endl;
    //         cout << "Maximum: " << max << endl;
    //         break;
    //     }
    //     case 4:
    //     {
    //         int n = N, a;
    //         for (int i = 0; i < n - 1; i++)
    //         {
    //             for (int j = 0; j < n - i - 1; j++)
    //             {
    //                 if (arr[j] > arr[j + 1])
    //                 {
    //                     int temp = arr[j];
    //                     arr[j] = arr[j + 1];
    //                     arr[j + 1] = temp;
    //                 }
    //             }
    //         }
    //         for (int i = 0; i < n - 1; i++)
    //         {
    //             if (arr[i] == arr[i + 1])
    //             {
    //                 for (int j = i; j < n - 1; j++)
    //                     arr[j] = arr[j + 1];
    //                 n--;
    //                 i--;
    //             }
    //         }
    //         cout << "Array elements: ";
    //         for (int i = 0; i < n; i++)
    //             cout << arr[i] << " ";
    //         cout << endl;
    //         break;
    //     }
    //     case 5:
    //     {
    //         int i = 0, j = N - 1;
    //         while (i < j)
    //         {
    //             int T = arr[i];
    //             arr[i] = arr[j];
    //             arr[j] = T;
    //             i++;
    //             j--;
    //         }
    //         cout << "Reversed array: ";
    //         for (int i = 0; i < N; i++)
    //             cout << arr[i] << " ";
    //         cout << endl;
    //         break;
    //     }
    //     case 6:
    //         cout << "Exiting...\n";
    //         return 0;
    //     default:
    //         cout << "Invalid choice!\n";
    //     }
    // }

    // return;
}

