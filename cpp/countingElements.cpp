class Solution {
public:
    int countElements(vector<int>& arr) {
    int result = 0;
   	std::unordered_set<int> set;
    for (const int &i: arr) {
        set.insert(i);
    }
    for (const int &j: arr){
    	if(set.count(j+1) == 1){
    		result += 1;
    	}
    }
    return result;   
  }
};