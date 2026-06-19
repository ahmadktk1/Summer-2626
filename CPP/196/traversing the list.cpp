#include<iostream>
#include<list>

using namespace std;

int main(){
	// traversing the element
	
	list<int> li = {3,44,25,39,29,291,248,57};
	
	// we will do it using for loop normal for loop structure or while loop structure the for loop is very easy but let us try with while loop
	
	auto it = li.begin();
	while(it != li.end()){
		cout<<*it<<"  ";
		++it;
	}
}