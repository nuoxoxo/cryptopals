#include "iostream"
#include "string"
#include "bitset"
#define endline "\n"

std::string HexStr = "49276d206b696c6c696e6720796f757220\
627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d";

std::string binStr_to_base64(std::string);
std::string asciiStr_to_base64(std::string);
std::string hexStr_to_base64(std::string);

int main()
{
    {
        std::cout << "Block 1/ \n";
        std::string r1 = asciiStr_to_base64("And");
        std::cout << "r1/ " << r1 << endline;

        std::string r2 = asciiStr_to_base64("g");
        std::cout << "r2/ " << r2 << endline;

        std::string r3 = asciiStr_to_base64("gm");
        std::cout << "r3/ " << r3 << endline << endline;
    }
    {
        std::cout << "Block 2/ \n";
        std::cout << "res/ " << hexStr_to_base64(HexStr) << endline;
        
    }
}

std::string binStr_to_base64(std::string bs)
{
    std::string b64;
    b64 = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/";
    std::string res;
    int N = bs.length();
    if (N % 6)
        bs.append(6 - N % 6, '0');
    N = bs.length();
    int i = 0;
    while (i < N)
    {
        int idx = std::stoi(bs.substr(i, 6), nullptr, 2);
        res += b64[idx];
        i += 6;
    }
    while (res.length() % 4)
        res += '=';
    return res;
}

std::string hexStr_to_base64(std::string s)
{
    assert(s.length() % 2 == 0);
    std::string bs;
    int i = 0;
    while (i < s.length())
    {
        bs += std::bitset<8>(std::stoi(s.substr(i, 2), nullptr, 16)).to_string();
        i += 2;
    }
    return binStr_to_base64(bs);
}

std::string asciiStr_to_base64(std::string s)
{
    std::string bs;
    for (char c : s)
        bs += std::bitset<8>(c).to_string();
    return binStr_to_base64(bs);
}

