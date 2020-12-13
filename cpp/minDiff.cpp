#include <cstdlib>
#include <iostream>
#include <vector>
using namespace std;

vector<int> smallestDifference(vector<int> arrayOne, vector<int> arrayTwo) {
  int minDiff = INT_MAX;
  vector<int> result;
  sort(arrayOne.begin(), arrayOne.end());
  sort(arrayTwo.begin(), arrayTwo.end());
  int i = 0;
  int j = 0;
  int left;
  int right;
  int leftT;
  int rightT;

  while(i < arrayOne.size() && j < arrayTwo.size()){
    leftT = arrayOne[i];
    rightT = arrayTwo[j];

    if(abs(leftT - rightT) < minDiff){
      left = leftT;
      right = rightT;
      minDiff = abs(leftT - rightT);
    }
    if (leftT > rightT){
      j++;
    } else if( rightT > leftT){
      i++;
    } else {
      result.push_back(leftT);
      result.push_back(rightT);
      return result;
    }
  }
  result.push_back(left);
  result.push_back(right);
  return result;
}


int main(){
  int a[] = {1,9,1004};
  int b[] = {100, 150, 6, -1};
  vector<int> c (a, a + sizeof(a) / sizeof(int) );
  vector<int> d (b, b + sizeof(b) / sizeof(int) );

  vector<int> e;
  e = smallestDifference(c, d);
  for(int x : e ){
    cout << x << endl;
  }
}