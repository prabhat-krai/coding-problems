#include <vector>
using namespace std;

int minNumberOfCoinsForChange(int n, vector<int> denoms) {
  vector<int> result(n+1, INT_MAX);
	result[0] = 0;  
  int k;

  for(int x : denoms){
    for(int j = 1; j <=n; j++){
      if(x <= j){
        if(result[j - x] == INT_MAX){
          k = INT_MAX;
        }else{
          k = result[j - x] + 1;
        }
        result[j] = min(result[j], k);
      }
    }
  }

  if (result[n] == INT_MAX)
    return -1;
  
  return result[n];
}
