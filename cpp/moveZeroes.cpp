#include <vector>

using namespace std;

class Solution {
public:
    void moveZeroes(vector<int>& nums) {
    	int arr_size = nums.size();
        for(int i = 0; i < arr_size; i++){
        	if(nums[i] == 0){
        		for(int j = i + 1; j < arr_size ; j++){
        			if(nums[j] != 0){
        				nums[i] = nums[j];
        				nums[j] = 0;
        				break;
        			}
        		}
        	}
        }
    }
};