#include<iostream>
#include<list>
#include<algorithm>
using namespace std;

int main(){
	list<int> li = {4,35,67,23,299,221};
	
	// finding the element 23 we will use the 
	
	auto it = find(li.begin(),li.end(),23);
	
	if (it != li.end()){
	
		cout<<*it;
	}
	else{
		cout<<"Element not found";
	}
}