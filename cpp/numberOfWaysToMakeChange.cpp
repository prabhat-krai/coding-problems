#include <vector>
using namespace std;

int numberOfWaysToMakeChange(int n, vector<int> denoms) {
  vector<int> result;
  result.push_back(1);
  for(int i=1; i<=n; i++){
    result.push_back(0);
  }

  for(int x : denoms){
    for(int j = 1; j <= n; j++){
      if(x <= j){
        result[j] += result[j - x];
      }
    }
  }
  return result[n];
}
