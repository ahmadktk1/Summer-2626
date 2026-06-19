#include<iostream>
#include<list>

using namespace std;

int main(){
	
	// updating the element
	list <int> li = {2,33,44,67,93};
	// we want to update the item 2 which is 44 to 59
	auto it = li.begin();
	advance(it,2);
	*it = 59;
	
	// updating the first item which is 2 to 12
	li.front() = 12;
	
	// updating the last item which is 93 to 188
	li.back() = 193;
	
	// traversing through every Item
	for(auto i: li){
		cout<<i<<"  ";
	}
}