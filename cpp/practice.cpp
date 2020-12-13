#include<vector>
using namespace std;

bool isValidSubsequence(vector<int> array, vector<int> sequence) {
  int found = -1;
  for(int i : sequence){
    if(found + 1 >= array.size()){
      return false;
    }
    for(int j = found + 1; j < array.size(); j++) {
      if(i == array[j]){
        found = j;
        break;
      }
      if(j == array.size() - 1 && i != array[j]){
        return false;
      }
    }
  }
  return true;
}
