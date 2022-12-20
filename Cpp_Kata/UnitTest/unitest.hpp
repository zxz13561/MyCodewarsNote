#include <string>
#include <iostream>

class unitest
{
private:
    /* data */
public:
    unitest(/* args */);
    ~unitest();
    std::string Equals(std::string b);
    int Equals(int b);
    bool Equals(bool b);
    void That(std::string q, std::string a);
    void That(int q, int a);
    void That(bool q, bool a);
};

unitest::unitest(/* args */)
{
}

unitest::~unitest()
{
}

std::string unitest::Equals(std::string b){
    return b;
}

int unitest::Equals(int b){
    return b;
}

bool unitest::Equals(bool b){
    return b;
}

void unitest::That(std::string q, std::string a){
    if(q != a){
        std::cout << "Q: " << q << " |A: " << a << "\n";
        for (int i = 0; i < q.size(); i++)
        {
            std::cout << "Char: " << q[i] << " | " << a[i] << " " << (q[i] == a[i]) << "\n";
        }
    }
    std::cout << "IsPass: " << (q == a ? "pass" : "fail") << "\n";
}

void unitest::That(int q, int a){
    if(q != a){
        std::cout << "Q: " << q << " |A: " << a << "\n";
    }
    std::cout << "IsPass: " << (q == a ? "pass" : "fail") << "\n";
}

void unitest::That(bool q, bool a){
    if(q != a){
        std::cout << "Q: " << (q ? "True" : "False") << " |A: " << (a ? "True" : "False") << "\n";
    }
    std::cout << "IsPass: " << (q == a ? "pass" : "fail") << "\n";
}