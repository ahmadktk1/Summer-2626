#include<iostream>
#include<list>

using namespace std;


int main(){
	list<int>li = {3,4};
	
	// appending to list
	li.push_back(7);
	// appending to front
	li.push_front(8);
	
	// inserting to 2nd place which is 1 index
	auto it = li.begin();
	advance(it,1);
	li.insert(it,222);
	
	
	// accessing the 2nd item
	cout<<*next(li.begin(),1);
}