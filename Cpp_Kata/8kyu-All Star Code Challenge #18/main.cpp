#include <iostream>
#include <string>

using namespace std;

int strCount(string word, char letter)
{
    return count(word.begin(), word.end(), letter);
}

void That(int q, int a){
    if(q != a){
        cout << "Q: " << q << " |A: " << a << "\n";
    }
    cout << "IsPass: " << (q == a ? "pass" : "fail") << "\n";
}

int Equals(int b){
    return b;
}

int main()
{
    That(strCount("Hello", 'o'), Equals(1));
    That(strCount("Hello", 'l'), Equals(2));
    That(strCount("Hello", 'q'), Equals(0));
    That(strCount("Pippi", 'p'), Equals(2));
    That(strCount("", 'l'), Equals(0));
}