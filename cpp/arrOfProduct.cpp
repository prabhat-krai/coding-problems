#include <vector>
#include <deque>
#include<iostream>
using namespace std;

vector<int> arrayOfProducts(vector<int> array) {
	int l = array.size() - 1;
  vector<int> l2r;
	l2r.push_back(array[0]);
	deque<int> r2l;
	r2l.push_front(array[l]);
	vector<int> result;

	for(int i = 1; i < array.size(); i++){
		l2r.push_back(array[i] * l2r[i-1]);
	}
  reverse(array.begin(), array.end());

  for(int i = 1; i < array.size(); i++){
		r2l.push_back(array[i] * r2l[i-1]);
	}
  reverse(r2l.begin(), r2l.end());
  for(int k = 0; k <=l ; k++){
    if(k - 1 < 0){
      result.push_back(r2l[k+1]);
    } else if(k+1 > l){
      result.push_back(l2r[k-1]);
    } else {
      result.push_back(l2r[k-1] * r2l[k+1]);
    }
  }
  return result;
}

int main() 
{
    int myints[] = {5,1,4,2};
    vector<int> a (myints, myints + sizeof(myints) / sizeof(int) );
    arrayOfProducts(a);
    return 0;
}