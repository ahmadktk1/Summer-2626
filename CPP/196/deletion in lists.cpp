// deleting an element from list it has the same as adding an item

#include<iostream>
#include<list>

using namespace std;

int main(){
	list<string> names = {"Alex","Batti","Dushman","Wafadar","inkar"};
	
	// deleting an element from front
	names.pop_front();
	
	// deleting an element from back
	names.pop_back();
	
	// deleting a specific item in this case "Dushman" which will be at 1 after deleting the front item 
	auto it = names.begin();
	advance(it,1);
	names.erase(it);
	
	
	// travering the list here
	
	for (auto tt = names.begin();tt != names.end(); ++tt){
		cout<<*tt<<"  ";
	}
}
