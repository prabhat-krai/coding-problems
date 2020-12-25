#include<vector>

using namespace std;

int findLengthOfPeak(vector<int> array, int i){
  int left = 0;
  int right = 0;
  int temp = i;

  while(array[temp] > array[temp+1] && temp < array.size() - 1){
    right++;
    temp++;
  }

  temp = i;

  while(array[temp] > array[temp-1] && temp > 0){
    left++;
    temp--;
  }

  return left + right + 1;
}

int longestPeak(vector<int> array) {
  if(array.size() == 0)
    return 0;
  int maxResult = 0;
  int tempResult = 0;

  for(int i = 1; i < array.size() - 1; i++){
    if(array[i] > array[i-1] && array[i] > array[i+1]){
      tempResult = findLengthOfPeak(array, i);
      if(tempResult > maxResult)
        maxResult = tempResult;
    }
  }

  return maxResult;
}
