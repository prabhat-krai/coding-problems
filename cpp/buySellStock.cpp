#include<iostream>
#include<vector>

using namespace std;

class Solution {
public:
    int maxProfit(vector<int>& prices) {
    	int totalProfit = 0;
        for(int i = 1; i < prices.size(); i++){
        	if(prices[i] > prices[i-1]){
        		totalProfit += prices[i] - prices[i-1];
        	}
        }
        return totalProfit;
    }
};

int main() 
{
    int myints[] = {16,2,77,29};
    vector<int> a (myints, myints + sizeof(myints) / sizeof(int) );
    Solution *sol = new Solution();
    cout << sol->maxProfit(a) << endl;
    return 0;
}