#include<iostream>
#include<unordered_map>
#include<list>
#include<string>
using namespace std;




int main(){
	unordered_map<std::string,string> account; 
	list<string> lis ;
	
	lis.push_back("Ahmad");
	lis.push_back("22");
	lis.push_back("Saving");
	lis.push_back("1909");
	lis.push_back("Latamber Karak");
	lis.push_back("0");
	
	int c = 0;
	for (string n : lis){
		cout<<n<<endl;
	}
	
	return 0;
}