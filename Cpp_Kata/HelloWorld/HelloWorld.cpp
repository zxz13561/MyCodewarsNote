#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main()
{
    string msg = "Hello world!";
    cout << msg << endl;

    vector<int> arr = {1, 2, 3, 4, 5}; 
    for(int& i: arr){
        cout << i << " ";
    }
}