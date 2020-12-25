#include <vector>
using namespace std;

int shiftedBinaryHelper(vector<int> &array, int target, int left, int right){
  while(left <= right) {
    int mid = (left + right)/2;
    int potentialMatch = array[mid];
    int leftNum = array[left];
    int rightNum = array[right];

    if(potentialMatch == target){
      return mid;
    } else if()
  }
}

int shiftedBinarySearch(vector<int> array, int target) {
  return shiftedBinaryHelper(array, target, 0, array.size() - 1);
}
