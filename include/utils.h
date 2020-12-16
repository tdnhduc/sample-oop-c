#ifndef _UTILS_H_
#define _UTILS_H_
#include "centrallib.h"
#include <locale>
using namespace std;

string to_lower(string s) 
{
    for(char &c : s)
    {
        c = tolower(c);
    } 
    return s;
}
#endif