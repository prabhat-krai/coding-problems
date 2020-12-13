#include <vector>
using namespace std;

int indexEqualsValue(vector<int> array) {
  for(int i = 0; i < array.size(); i++){
    if(array[i] == i)
      return i;
  }
  return -1;
}
