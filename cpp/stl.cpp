#include<vector>
#include<algorithm>
#include<iostream>
#include<set>
#include<map>
using namespace std;

int main(){
  vector<int> nums;
  nums.push_back(10);
  nums.push_back(12);
  nums.push_back(8);
  sort(nums.begin(), nums.end());
  bool there = binary_search(nums.begin(), nums.end(), 8);

  cout << there << endl;

  set<int> sortednums;

  sortednums.insert(-1);
  sortednums.insert(-10);
  sortednums.insert(10);
  sortednums.insert(5);

  for(auto x : sortednums){
    cout << x << endl;
  }

  auto it = sortednums.upper_bound(6);
  cout << *it;

  map<int, int> A;
  A[1] = 1;
  A[2] = 4;
  A[3] = 9;
  A[4] = 16;

  
  cout << A[3] << endl;

  map<char, int> ransom;
        for(char i : "tthis"){
            if(ransom.find(i) != ransom.end()){
                ransom[i] +=1;    
            } else {
                ransom[i] =1;
            }
            cout << ransom[i] <<  i << endl;
        }
}