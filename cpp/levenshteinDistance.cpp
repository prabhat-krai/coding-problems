#include<iostream>
#include<string>
#include<map>
using namespace std;

int levenshteinDistanceHelper(string str1, string str2, map<string, int> &mapOfStrings){
  string key = str1 + "," + str2;
  if(mapOfStrings.find(key) != mapOfStrings.end())
    return mapOfStrings[key];
  if (str2.size() == 0){
    mapOfStrings[key] = str1.size();
    return mapOfStrings[key];
  }
  if (str1.size() == 0){
    mapOfStrings[key] = str2.size();
    return mapOfStrings[key];
  }

  string chopped_str1 = str1.substr(0,str1.size() - 1);
  string chopped_str2 = str2.substr(0,str2.size() - 1);
  int addThis = str1.back() == str2.back() ? 0 : 1;
  int result = min(
    min(
      levenshteinDistanceHelper(chopped_str1, str2, mapOfStrings) + 1,
      levenshteinDistanceHelper(str1, chopped_str2, mapOfStrings) + 1
    ),
    levenshteinDistanceHelper(chopped_str1, chopped_str2, mapOfStrings) + addThis
  );

  mapOfStrings[key] = result;
  return result;
}

int levenshteinDistance(string str1, string str2) {
  map<string, int> mapOfStrings;
  return levenshteinDistanceHelper(str1, str2, mapOfStrings);
}

int main(){
  string a = "PRABHATKUMARRAI";
  string b = "PRABHATKUMAARRAI";
  int c = levenshteinDistance(a, b);
  cout << c << endl;
}