#include <vector>
#include <string>
#include <iostream>
using namespace std;

bool isValid(string number){
  int numberInt = stoi(number);
  if (numberInt > 255){
    return false;
  }
  return number.length() == to_string(numberInt).length();
}

string join(vector<string> ips){
  string s;

  for(int i = 0; i < ips.size(); i++){
    s += ips[i];

    if(i < ips.size() - 1){
      s += ".";
    }
  }
  return s;
}

vector<string> validIPAddresses(string str) {
  vector<string> validIPs;
  
  for(int i = 1; i < min((int)str.length(), 4); i++){
    vector<string> IPsFound;
    IPsFound.push_back("");IPsFound.push_back("");IPsFound.push_back("");IPsFound.push_back("");

    IPsFound[0] = str.substr(0, i);
    if(!isValid(IPsFound[0])){
      continue;
    }

    for(int j = i + 1; j < i + min((int)str.length() - i, 4); j++){
      IPsFound[1] = str.substr(i, j - i);
      if(!isValid(IPsFound[1])){
        continue;
      }

      for(int k = j + 1; k < j + min((int)str.length() - j, 4); k++){
        IPsFound[2] = str.substr(j, k - j);
        IPsFound[3] = str.substr(k);

        if(isValid(IPsFound[2]) && isValid(IPsFound[3])){
          validIPs.push_back(join(IPsFound));
        }
      }
    }
  }

  return validIPs;
}

int main(){
  string s = "1921680";
  vector<string> b;
  b = validIPAddresses(s);

  for (string k : b){
    cout << k << endl;
  }
}