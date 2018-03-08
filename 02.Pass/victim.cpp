#include <cstring>
#include <string>
#include <iostream>
using namespace std;
// victim function
bool test_pass(char *user_pass)
{
    //user_pass = "HUtaMtRUAJLsqC2J";
    const char *passwd = "HUtaMtRUAJLsqC2J";
    string in=user_pass;
    string pass=passwd;
    //int passwd_len = strlen(passwd);
 
    /*for (int i = 0; i <= passwd_len; i++)
    {
        if (passwd[i] != user_pass[i])
        {
            return false;
        }
    }*/
    if(strlen(passwd)==strlen(user_pass)){
       /* cout<<pass; 
        cout<<" : ";
        cout<<in;
        cout<<"\n";*/
        if(pass.find(in)!= std::string::npos){
            return true;
        }
    }
    return false;
}

