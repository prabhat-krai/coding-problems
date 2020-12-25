#include<vector>
#include<string>
#include<algorithm>
using namespace std;

vector<int> sunsetViews(vector<int> buildings, string direction) {
  vector<int> result;
  if(buildings.size() == 0)
    return result;
  int start = 0;
  int end = buildings.size() - 1;
  int step = 1;

  if(direction == "EAST"){
   start = buildings.size() - 1;
   end = 0;
   step = -1; 
  }

  int biggestYet = INT_MIN;

  while(start != end){
    if(buildings[start] > biggestYet){
      result.push_back(start);
      biggestYet = buildings[start];
    }
    start = start + step;
  }
  if(buildings[start] > biggestYet){
    result.push_back(start);
  }
  if(direction == "WEST")
    return result;
  reverse(result.begin(), result.end());

  return result;
}

int main(){
  int myints[] = {};
  vector<int> a (myints, myints + sizeof(myints) / sizeof(int) );
  sunsetViews(a, "EAST");
}