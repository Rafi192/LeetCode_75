#include <iostream>
#include <string>
#include <numeric> // For std::gcd

using namespace std;
class Solution {
public:
    string gcdOfStrings(string str1, string str2) {
        if (str1 +str2 != str2+ str1){
            return "";
        }
        else{
            int gcd_length = std::gcd(str1.size(), str2.size());
            string gcd_string = str1.substr(0, gcd_length);

            if((str1.size() % gcd_length==0) && (str2.size()% gcd_length==0)){
                return gcd_string;
            }
            else{
                return "";
            }
        }
    }
};
