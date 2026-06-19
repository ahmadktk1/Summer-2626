#include<iostream>
#include<list>

using namespace std;

int main(){
	list<int>li= {4,6};
	
//	auto it = li.begin();
//	advance(it,1);
//	li.insert(it,9);

// the below way doesn't work so you have to speciefically access a certain element using begin then specify its location
//	int it = 1;
//	li.insert(it,9)
//	

// lets us check if it can work for first element with begin function
	auto it = li.begin();
	li.insert(it,88);
	// the above thing also work I think my brain is now working fine
	
	
	for (auto i:li){
		cout<<i<<endl;
	}
}