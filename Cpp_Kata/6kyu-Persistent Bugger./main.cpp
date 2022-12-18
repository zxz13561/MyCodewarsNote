#include <iostream>
#include <sstream>
#include <iterator>

using namespace std;

int persistence(long long n){
  cout << n << ":\n";
  
  stringstream temp_str;
  temp_str << n;
  
  char const *n_arr = temp_str.str().c_str();
  cout << "arr: " << n_arr << endl;
  
  auto len_arr = sizeof n_arr / sizeof n_arr[0];
  cout << "arr size:" << len_arr << "\n";
    
  for(int i = 0; i < len_arr; i++){
    cout << n_arr[i] << "\n";
  }
  cout << "End\n";
  return 0;
}

int main()
{
    persistence(39);
    persistence(4);
    persistence(25);
    persistence(999);
    persistence(444);     
};