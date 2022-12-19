/*
Kata Task
I have a cat and a dog.

I got them at the same time as kitten/puppy. That was humanYears years ago.

Return their respective ages now as [humanYears,catYears,dogYears]

NOTES:
    humanYears >= 1
    humanYears are whole numbers only

    Cat Years:
        15 cat years for first year
        +9 cat years for second year
        +4 cat years for each year after that

    Dog Years:
        15 dog years for first year
        +9 dog years for second year
        +5 dog years for each year after that
*/

#include <iostream>
#include <vector>

using namespace std;

vector<int> humanYearsCatYearsDogYears(int humanYears) {
  int cat = 15;
  int dog = 15;
  for(int i = 2; i <= humanYears; i++){
    cat += i == 2 ? 9 : 4;
    dog += i == 2 ? 9 : 5;
  }
  return {humanYears, cat, dog};
}

void dump_vector(vector<int> v){
    for(int e: v){
        cout << e << " ";
    }
    cout << "\n" << endl;
}

int main()
{
    dump_vector(humanYearsCatYearsDogYears(1));
    dump_vector(humanYearsCatYearsDogYears(2));
    dump_vector(humanYearsCatYearsDogYears(10));
};