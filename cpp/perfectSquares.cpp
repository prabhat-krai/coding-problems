#include <iostream>
#include <vector>

using namespace std;

int numSquares(int n) {
    
    vector<int> num;
    int i = 1;
    while(i*i <= n){
        num.push_back(i*i);
        i++;
    }
    
    vector<int> ans(n+1,INT_MAX);
    ans[0] = 0;
    
    for(int i=1 ; i<=n ; i++){
        for(int j=0 ; j<num.size() ; j++){
            if(i-num[j] >=0){
                ans[i] = min(ans[i],ans[i-num[j]]+1);
            }else{
                break;
            }
        }
    }
    
    return ans[n];
}