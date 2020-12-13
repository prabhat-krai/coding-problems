#include <vector>
#include<iostream>

using namespace std;

int indexEqualsValueHelper(vector<int> array, int start, int end, int fixed = -1) {
  int mid = (start + end)/2;

  while(start < end){
    if(array[mid] == mid){
      fixed = mid;
      return indexEqualsValueHelper(array, start, mid, fixed);
    } else if (array[mid] < mid) {
      start = mid + 1;
      mid = (start + end)/2;
    } else {
      end = mid - 1;
      mid = (start + end)/2;
    }
  }
  return fixed;
}

int indexEqualsValue(vector<int> array) {
  int start = 0;
  int end = array.size();
  return indexEqualsValueHelper(array, start, end);
}

int main(){
  int myints[] = {-9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 18};
  vector<int> a (myints, myints + sizeof(myints) / sizeof(int) );
  int b = indexEqualsValue(a);

  cout << b << endl;
}