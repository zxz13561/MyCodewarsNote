#include <iostream>
#include <string>

using namespace std;

string swap(string t)
{
    string even, odd;
    bool sw = true;
    for (char c : t)
    {
        if(sw){
            even += c;
        }
        else{
            odd += c;
        }
        sw = !sw;
    }
    return odd + even;
}

string encrypt(string text, int n)
{
    if(text != "" && n > 0){
        return encrypt(swap(text), --n);
    }
    else{
        return text;
    }
}

string decrypt(string encryptedText, int n)
{
    if(encryptedText == "" || n <= 0){
        return encryptedText;
    }
    else{
        int loop = 1;
        string s = swap(encryptedText);
        while(s != encryptedText){
            loop++;
            s = swap(s);
        }
        loop = loop >= n ? loop - n : loop - (n % loop);
        return encrypt(encryptedText, loop);
    }
}

void That(string q, string a){
    //cout << a << "\n";
    if(q != a){
        cout << "Q: " << q << " |A: " << a << "\n";
        for (int i = 0; i < q.size(); i++)
        {
            cout << "Char: " << q[i] << " | " << a[i] << " " << (q[i] == a[i]) << "\n";
        }
    }
    cout << "IsPass: " << (q == a ? "pass" : "fail") << "\n";
}

string Equals(string b){
    return b;
}

int main()
{
    That(encrypt("This is a test!", 0), Equals("This is a test!"));
    That(encrypt("This is a test!", 1), Equals("hsi  etTi sats!"));
    That(encrypt("This is a test!", 2), Equals("s eT ashi tist!"));
    That(encrypt("This is a test!", 3), Equals(" Tah itse sits!"));
    That(encrypt("This is a test!", 4), Equals("This is a test!"));
    That(encrypt("This is a test!", -1), Equals("This is a test!"));
    That(encrypt("This kata is very interesting!", 1), Equals("hskt svr neetn!Ti aai eyitrsig"));
    That(decrypt("This is a test!", 0), Equals("This is a test!"));
    That(decrypt("hsi  etTi sats!", 1), Equals("This is a test!"));
    That(decrypt("s eT ashi tist!", 2), Equals("This is a test!"));
    That(decrypt(" Tah itse sits!", 3), Equals("This is a test!"));
    That(decrypt("This is a test!", 4), Equals("This is a test!"));
    That(decrypt("This is a test!", -1), Equals("This is a test!"));
    That(decrypt("FWS", 5), Equals("WFS"));
    That(decrypt("MHNQ", 5), Equals("NMQH"));
    That(decrypt("hskt svr neetn!Ti aai eyitrsig", 1), Equals("This kata is very interesting!"));
    That(encrypt("", 0), Equals(""));
    That(encrypt("", 3), Equals(""));
    That(decrypt("", 0), Equals(""));
    That(decrypt("", 3), Equals(""));
}