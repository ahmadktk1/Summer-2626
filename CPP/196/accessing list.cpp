#include<iostream>
#include<list>

using namespace std;

int main(){
	list<int> li = {4,5,8,9,28,29};
	// for accessing a specific element
	cout<<*next(li.begin(),1)<<" ";
}