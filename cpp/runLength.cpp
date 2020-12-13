using namespace std;

string runLengthEncoding(string str) {
	string result;
	
	int count = 1;
	for(int i = 0; i < str.size(); i++){
		if(count == 9 || str[i] != str[i+1]){
			result += to_string(count) + str[i];
			count = 0;
		}
		count++;
	}
	
	if(count > 1){
		result += to_string(count) + str[str.size() - 1];	
	}
	
  return result;
}