#include<bits/stdc++.h>
using namespace std;

class node{
    public:
    string name;
    string prn;
    node *next;
    node(){
        prn = '0';
        name = "";
        next = NULL;
    }
};

string name,prn;

void insert(**head_ref,string name,string ){

}


node * Entries(node* &head){
   int n;
   cout<<"How many Entries";
   cin>>n;
   int i =n;
   while (i>0)
   {
      if(i==n){
         cout<<"Enter the name of President";
         cin>>name;
         cout<<"Enter the prn of President";
         cin>>prn;
      }
      if(i==1){
         cout<<"Enter the name of sec";
         cin>>name;
         cout<<"Enter the prn of sec";
         cin>>prn;
      }
      else{
         cout<<"Enter the name of member";
         cin>>name;
         cout<<"Enter the prn of member";
         cin>>prn;

      }
      insert(&head,name,prn);
      i--;
   }
   
}


int main(){
   node *head=NULL,*newnode;
   Entries(head)
}