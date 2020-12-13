#include <vector>
#include <string>
#include <iostream>
#include <unordered_map>

using namespace std;

vector<vector<string> > groupAnagrams(vector<string>& input_set) 
{
	unordered_map<string, vector<string> > my_map;
	vector<vector<string> > final_set;

	for (int i = 0; i < input_set.size(); i++)
	{
		string key = input_set[i];

		sort(key.begin(), key.end());

		my_map[key].push_back(input_set[i]);

	}

	for (auto n : my_map)
	{
		final_set.push_back(n.second);
	}

	return final_set;
}

int main(){
	vector<string> a;
	a.push_back("cat");
	groupAnagrams(a);
	return 0;
}