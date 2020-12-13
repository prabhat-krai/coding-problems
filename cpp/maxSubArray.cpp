#include <vector>
#include <iostream>
using namespace std;

class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int len = nums.size();
        if(len == 0){
          return 0;
        }
        int localMax = nums[0];
        int globalMax = nums[0];
        for(int i = 1; i < len; i++){
          localMax = max(nums[i], localMax + nums[i]);
          globalMax = max(globalMax, localMax);
        }
      return globalMax;
    }
};