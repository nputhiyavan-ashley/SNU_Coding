#include<bits/stdc++.h>
using namespace std;
bool validate(string input)
{
    stack<char> st;
    for(char s:input)
    {
        if(s=='{' || s=='(' || s=='[')
        {
            st.push(s);
        }
        else if(s=='}' || s==']' || s==')')
        {
            char t=st.top();
            if((s=='}' && t=='{') || (s==')' && t=='(') || (s==']' && t=='['))
            {
                st.pop();
            }
            else{
                return false;
            }
        }
    }
    return true;
}
int main()
{
    string input;
    cin>>input;
    if(validate(input))
    {
       cout<<"Balanced";
    }
    else
    {
       cout<<"Error";
    } 
    
}